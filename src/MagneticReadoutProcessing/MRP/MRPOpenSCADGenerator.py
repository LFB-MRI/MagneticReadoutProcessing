"""  generates openscad structures """

import math
import magpylib
import openpyscad as ops
import os
from pathlib import Path
import scipy


class MRPOpenSCADGeneratorException(Exception):
    def __init__(self, message="MRPOpenSCADGeneratorException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPOpenSCADGenerator():


    CUTOUT_MARGIN:float = 0.001 #mm
    CUTOUT_TOLERANCE_MARGIN: float = 0.1 #mm depending you 3d printer/lasercutter tolerances
    MAGNET_ANNOTATION_MARKER_SIZE = 1 # SEE create_magnet_cutout
    BASE_SLICE_THICKNESS: float = 10
    objects_to_subtract: [ops.Union] = []
    objects_to_add: [ops.Union] = []
    object_command_order_info: [str] = [] # STORE SOME INFO ABOUT THE ORDER OF FUNCTION CALLS
    def create_magnet_cutout(self, _magnet: magpylib.magnet, _annotation:str = None): #_magnet_trajectory: float, _rotation_drg_x:float, _cube_rotation_itself:float, _annotation: str= None, _safety_margin_mm: float = 0.05):
        if _magnet is None:
            raise MRPOpenSCADGeneratorException("_magnet is None")



        ops_magnet = ops.Union()


        # APPLY POSITION OFFSET USING .translate
        ## HERE THE POSITION OFFSET IS THE NOT THE FINAL POSITION ON THE CYLINDER
        ## POSITON ARGUMENT IS USED TO FINE ADJUST THE POSITION ON THE CYLINDRIC BASE TRAJECTORIE

        pos = [_magnet.position[0], _magnet.position[1], _magnet.position[2]]  # X Y Z
        mrot: scipy.spatial.transform.rotation.Rotation = _magnet.orientation.as_rotvec(degrees=True)
        rot = [mrot[0], mrot[1], mrot[2]]
        # ANNOTATION TEXT SETTINGS
        if _annotation is None:
            _annotation = ""
        text_size = 2
        text_offset: float = len(_annotation) * text_size * 0.3


        if isinstance(_magnet, magpylib.magnet.Cuboid):
            dim = [_magnet.dimension[0]+2*self.CUTOUT_TOLERANCE_MARGIN, _magnet.dimension[1]+2*self.CUTOUT_TOLERANCE_MARGIN, _magnet.dimension[2]+ 2*self.CUTOUT_TOLERANCE_MARGIN] # X Y Z
            # CREATE CUBE
            cube = ops.Cube(size=dim, center=True).comment("magpylib.magnet.Cuboid")
            ops_magnet.append(cube)
            # APPEND CUTOUT INDICATOR
            max_w = max(dim)
            max_w_mag = math.sqrt(max_w*max_w)
            ops_magnet.append(ops.Cylinder(d=max([max_w/2, 3]), h=self.BASE_SLICE_THICKNESS*2).translate([dim[0]/2,0,-self.BASE_SLICE_THICKNESS/2]).comment("annotation_cube"))


            # ADD ANNOTATION TEXT
            if _annotation is not None and len(_annotation) > 0:
                 ops_magnet.append(ops.Linear_Extrude(self.BASE_SLICE_THICKNESS).append(ops.Text(size=text_size, text='"{}"'.format(_annotation)).mirror([1,0,0]).translate([3*text_offset, (text_size/2/3)+(max_w_mag/2), -self.BASE_SLICE_THICKNESS]).rotate([0, 0 , 0])).comment("annotation_text"))

            # APPLY FINAL TRANSLATE TO DESTINATION POSITION AND ROTATION
            #ops_magnet = ops_magnet.translate(pos).rotate(rot).comment("ops_magnet_{}".format(_annotation))

            self.objects_to_subtract.append(ops.Union().append( ops_magnet.translate(pos).rotate(rot).comment("ops_magnet_{}".format(_annotation))))

        elif isinstance(_magnet, magpylib.magnet.Cylinder):

            # [r_inner, r_outer, h, section_angle_1, section_angle_2]
            r = _magnet.dimension[1] + 2 * self.CUTOUT_TOLERANCE_MARGIN # outer radius of the
            h = _magnet.dimension[2] + 2 * self.CUTOUT_TOLERANCE_MARGIN #

            cylinder = ops.Cylinder(r=r, h=h, center=True)
            ops_magnet.append(cylinder)
            raise MRPOpenSCADGeneratorException("Cylinder: not implemented cutout function")



        else:
            raise MRPOpenSCADGeneratorException("not implemented cutout function")




        self.object_command_order_info.append("{}_{}".format(len(self.object_command_order_info), ops_magnet._comment))

    def append_mounting_holes_to_base_slice(self, _outer_diameter_mm: float = None, _thickness_mm:float = None, _hole_width: float = 10, _hole_distance:float = 100, _add_both_side_bars = False):
        if _outer_diameter_mm is None:
            raise MRPOpenSCADGeneratorException("_outer_diameter_mm cant be none")
        if _thickness_mm is None:
            raise MRPOpenSCADGeneratorException("_thickness_mm cant be none")
        # USING INTERSECT
        mount = ops.Union()
        diameter_addition = 2
        dim = [_hole_distance,_hole_width*2,_thickness_mm]  # X Y Z
        # APPEN A BIT BIGGER CYLINDER FOR PLACING THE MOUNT CONSTRUCTION
        mount.append(ops.Difference().append(ops.Cylinder(d=_outer_diameter_mm-1, h=_thickness_mm, center=True)).append(ops.Cylinder(d=_outer_diameter_mm+diameter_addition, h=_thickness_mm, center=True)).comment("mount_contruction_helper_cylinder"))

        # ADD MOUNTING BARS
        mount_base = ops.Cube(dim, center=True).comment("mount_base")
        mount_hole_a = ops.Cylinder(d=_hole_width, h=1.5*_thickness_mm+ 2*self.CUTOUT_TOLERANCE_MARGIN).translate([(_hole_distance/2)-_hole_width, 0, -_thickness_mm]).comment("mount_hole_a")
        mount_hole_b = ops.Cylinder(d=_hole_width, h=1.5*_thickness_mm+ 2*self.CUTOUT_TOLERANCE_MARGIN).translate([-(_hole_distance/2)+_hole_width, 0,-_thickness_mm]).comment("mount_hole_a")

        # DISTANCE FROM CENTER TO MOUNTING BARS
        bar_distance = (_outer_diameter_mm/2) + diameter_addition
        ## TOP first BAR then SCREW HOLE
        mount.append(ops.Difference().append(mount_base).append(ops.Union().append(mount_hole_a).append(mount_hole_b)).translate([0, -bar_distance, 0]).comment("mount_bar_top"))
        ## BOTTOM
        if _add_both_side_bars:
            mount.append(ops.Difference().append(mount_base).append(ops.Union().append(mount_hole_a).append(mount_hole_b)).translate([0, bar_distance, 0]).comment("mount_bar_bottom"))

        mount.comment("append_mounting_holes_to_base_slice_{}_{}".format(_hole_width, _hole_distance))
        self.BASE_SLICE.append(mount)

    def create_cylinder_with_cutout(self, _inner_diameter_mm:float = None, _outer_diameter_mm:float = None, _thickness_mm: float = None) -> ops.Union:
        """
        Creates the cylindrical hallbach slice baseplate (for the later magnet cutouts)

        :param _add_2d_projection: adds a projection(cut=True) command before the object string to allow the creation of a 2D dfx drawing of the final object
        :type _add_2d_projection: bool

        :returns: OpenSCAD script as string
        :rtype: str
        """
        if _thickness_mm is None:
            raise MRPOpenSCADGeneratorException("_thickness cant be none")
        if _inner_diameter_mm > _outer_diameter_mm:
            raise MRPOpenSCADGeneratorException("_inner_diameter is bigger than _outher_diameter")
        _thickness_mm = _thickness_mm + 2*self.CUTOUT_TOLERANCE_MARGIN
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


        # APPEND CYLINDRICAL BASE WITH OUTOUT
        self.BASE_SLICE = ops.Union()
        self.BASE_SLICE.append(self.create_cylinder_with_cutout(_inner_diameter_mm, _outer_diameter_mm, _thickness_mm))
        self.BASE_SLICE_THICKNESS = _thickness_mm


        self.openscad_objects = []
        self.openscad_objects.append(self.BASE_SLICE)

        self.objects_to_subtract = []
        self.objects_to_add = []

    def __del__(self):
        self.BASE_SLICE = ops.Union()
        self.openscad_objects: ops.Union = ops.Union()
        self.openscad_objects = []
        self.objects_to_subtract = []
        self.objects_to_add = []

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



