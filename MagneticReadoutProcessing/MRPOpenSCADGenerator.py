import magpylib
import openpyscad as ops
import os
from pathlib import Path
class MRPOpenSCADGeneratorException(Exception):
    def __init__(self, message="MRPOpenSCADGeneratorException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPOpenSCADGenerator():


    CUTOUT_MARGIN:float = 0.00001
    MAGNET_ANNOTATION_MARKER_SIZE = 1 # SEE create_magnet_cutout

    objects_to_subtract: [ops.Union] = []
    objects_to_add: [ops.Union] = []
    object_command_order_info: [str] = [] # STORE SOME INFO ABOUT THE ORDER OF FUNCTION CALLS
    def create_magnet_cutout(self, _magnet: magpylib.magnet, _magnet_trajectory: float, _rotation_drg_x:float, _cube_rotation_itself:int, _annotation: str= None, _safety_margin_mm: float = 0.05):
        if _magnet is None:
            raise MRPOpenSCADGeneratorException("_magnet is None")

        if _safety_margin_mm is None:
            _safety_margin_mm = self.CUTOUT_MARGIN

        ops_magnet = ops.Union()


        # APPLY POSITION OFFSET USING .translate
        ## HERE THE POSITION OFFSET IS THE NOT THE FINAL POSITION ON THE CYLINDER
        ## POSITON ARGUMENT IS USED TO FINE ADJUST THE POSITION ON THE CYLINDRIC BASE TRAJECTORIE

        ## THEN APPLY THE ROTATION
        if isinstance(_magnet, magpylib.magnet.Cuboid):
            pos = [_magnet_trajectory + _magnet.position[0],_magnet.position[1],_magnet.position[2]] # X Y Z
            rot = [0, 0, _rotation_drg_x]
            in_magnet_rotation = [0, 0, _cube_rotation_itself]
            dim = [_magnet.dimension[0]+2*_safety_margin_mm, _magnet.dimension[1]+2*_safety_margin_mm, _magnet.dimension[2]+ 2*_safety_margin_mm] # X Y Z

            # FIRST APPLY CUBE ROTATION
            ## TRANSLATE TO ORBIT
            ## ROTATE AROUND ORBIT
            cube= ops.Cube(size=dim,center=True).rotate(in_magnet_rotation).translate(pos).rotate(rot)
            ops_magnet.comment("create_magnet_pos{}rot{}".format(pos, rot)) # ADD COMMENT TO PARENT OBJECT

            # APPEND ANOTHER SMALL CUTOUT TO INDICATE THE INSERTION DIRECTION
            max_w = max(dim)
            cube.append(ops.Cylinder(d=max([max_w/3, 2]), h=self.BASE_SLICE_THICKNESS*2).translate([_magnet_trajectory+ dim[0]/2,0,-dim[2]]).comment("annotation_cube_d{}_h{}".format(max_w, self.BASE_SLICE_THICKNESS)))

            # ADD INFORMATION TEXT
            if _annotation is not None and len(_annotation) > 0:
                # PLEASE NOTE '"<TEXT>"' IS NEEDED HERE TO AVOID THAT <TEXT> WILL BE PARSED AS VARIABLE
                text_size= 2
                text_offset:float = len(_annotation) * text_size*0.3
                # 1 linear extrude a 2d textobject
                ## the text needs to be rotated 90° and movec above the indication cube
                ## finally mirror the text itself to make the text readable in 2d and 3d export mode
                cube.append(ops.Linear_Extrude(self.BASE_SLICE_THICKNESS).append(ops.Text(size=text_size, text='"{}"'.format(_annotation)).mirror([1,0,0]).rotate([0,0,90])).translate([5+_magnet_trajectory + dim[0]/2,text_offset,0]))
            # APPEND TO MAGNET ASSEMBLY
            ops_magnet += cube


        else:
            raise MRPOpenSCADGeneratorException("not implemented cutout function")



            # APPEND TO OBJECTS
        self.objects_to_subtract.append(ops_magnet)
        self.object_command_order_info.append("{}_{}".format(len(self.object_command_order_info), ops_magnet._comment))

    def append_mounting_holes_to_base_slice(self, _hole_distance:float = 100):
        # USING INTERSECT
        pass


    def create_cylinder_with_cutout(self, _inner_diameter_mm:float = None, _outer_diameter_mm:float = None, _thickness_mm: float = None) -> ops.Union:
        """
        Create the hallbach cylindrical baseplate (for the later magnet cutouts)

        :param _add_2d_projection: adds a projection(cut=True) command before the object string to allow the creation of a 2D dfx drawing of the final object
        :type _add_2d_projection: bool

        :returns: OpenSCAD script as string
        :rtype: str
        """
        if _thickness_mm is None:
            raise MRPOpenSCADGeneratorException("_thickness cant be none")
        if _inner_diameter_mm > _outer_diameter_mm:
            raise MRPOpenSCADGeneratorException("_inner_diameter is bigger than _outher_diameter")

        cylinder_base:ops.Union = ops.Union()
        # here the comment section is reused as step identifier
        cylinder_base.comment("create_cylinder_with_cutout_inner_{}mm_outer{}mm_thickness{}mm".format(_inner_diameter_mm, _outer_diameter_mm, _thickness_mm))
        cylinder_outer: ops.Cylinder = ops.Cylinder(d=_outer_diameter_mm, h=_thickness_mm, center=True)

        if _inner_diameter_mm is not None and _inner_diameter_mm > 0.0:
            cylinder_inner: ops.Cylinder = ops.Cylinder(d=_inner_diameter_mm, h=_thickness_mm+self.CUTOUT_MARGIN, center=True)
            cylinder_base.append(cylinder_outer - cylinder_inner)
        else:
            cylinder_base.append(cylinder_outer)



        self.object_command_order_info.append("{}_{}".format(len(self.object_command_order_info), cylinder_base._comment))

        return cylinder_base



    def __init__(self, _inner_diameter_mm:float, _outer_diameter_mm: float, _thickness_mm: float):
        self.openscad_objects: ops.Union = ops.Union()
        self.BASE_SLICE = self.create_cylinder_with_cutout(_inner_diameter_mm, _outer_diameter_mm, _thickness_mm)
        self.BASE_SLICE_THICKNESS =_thickness_mm
        self.openscad_objects.append(self.BASE_SLICE)




    def to_scad(self, _add_2d_projection: bool = True) -> str:
        """
        Returns a openSCAD string of the objects created by other class functions

        :param _add_2d_projection: adds a projection(cut=True) command before the object string to allow the creation of a 2D dfx drawing of the final object
        :type _add_2d_projection: bool

        :returns: OpenSCAD script as string
        :rtype: str
        """

        # FIRST CREATE THE SLICE
        # WITH CYLINDER - ALL CREATED MAGNETS
        diff = ops.Difference()
        diff.append(self.BASE_SLICE) # SUBTRACT FROM THE BASE SLICE ALL OBJECT IN THE SUBTRACT LIST (e.g. all created Magnets)


        for diffobj in self.objects_to_subtract:
            diff.append(diffobj)

        # HERE WE CAN ADD SOME STUFF TO THE DIFF OBJECT
        # E.G. ADD MOUNTING HOLES
        add = ops.Union()
        add.append(diff)


        for addobj in self.objects_to_add:
            add.append(addobj)


        final_obj = ops.Union()
        final_obj.append(diff)


        scad_script =final_obj.dumps()

        if scad_script is None:
            scad_script = "//EMPTY SCAD SCRIPT"
            return scad_script




        if _add_2d_projection:
            scad_script = "projection(cut = true) {}\n".format(scad_script)

        for line in self.object_command_order_info:
            scad_script = scad_script + "// {} \n".format(line)
        return scad_script

    def get_ops_baseobject(self) -> ops.Union:
        return self.BASE_SLICE

    def export_scad(self, _filename:str = None, _add_2d_projection: bool = True) -> str:
        """
        Returns a openSCAD string of the objects created by other class functions

        :param _filename: abs or rel filepath including filename of the destination file
        :type _filename: str

        :param _add_2d_projection: adds a projection(cut=True) command before the object string to allow the creation of a 2D dfx drawing of the final object
        :type _add_2d_projection: bool

        :returns: filepath of the created .scad file
        :rtype: str
        """
        if _filename is None or len(_filename) <= 0:
            raise MRPOpenSCADGeneratorException("_filename cant be none or empty")
        # CREATE FOLDER STRUCTURE IF NOT EXISTS
        try:
            if not os.path.dirname(_filename):
                Path(_filename).parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise MRPOpenSCADGeneratorException(str(e))

        # EXPORT OBEJCTS TO OPENSCAD SCRIPT
        scad_script = self.to_scad(_add_2d_projection)

        # EXPORT TO FILE
        if '.scad' not in _filename:
            _filename = _filename + '.scad'
        with open(_filename, 'w') as fp:
            fp.write(scad_script)
        # RETURN FILEPATH
        return _filename



