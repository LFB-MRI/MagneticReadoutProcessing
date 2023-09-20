""" generates magnet structures out of given readings and export hallbach rings """

import math
import magpylib
from magpylib import Collection, getB
import vector
import matplotlib.pyplot as plt

from scipy.spatial.transform import Rotation as R
import numpy as np


from MRP import MRPReading, MRPAnalysis, MRPMagnetTypes, MRPHelpers, MRPOpenSCADGenerator



class MRPHallbachArrayGeneratorException(Exception):
    def __init__(self, message="MRPHallbachArrayGeneratorException thrown"):
        self.message = message
        super().__init__(self.message)



class MRPHallbachArrayResult():
    """ contains the generated data returned after calling a generation method e.g. generate_1k_hallbach_using_polarisation_direction"""
    description: str = "---"
    slice_inner_diameter: float = 0.0
    slice_outer_diameter: float = 0.0
    max_magnet_height: float = 0.0

    magnets: [magpylib.magnet] = [] # PROCESSED MAGNETS WITH SET POS, ROT, DIM, MAG

    annotations: [str] = [] # HOLDS THE MAGNET NAME + TYPE ANNOTATION TO CREATE THE OPENSCAD MODEL
    def __int__(self):
        pass


class MRPHallbachArrayGenerator:
    """ Contains static functions to generate a 3D CAD Model of a Hallbach-Magnet using given readings."""
    @staticmethod
    def plot_vectors(_vectors: [vector.Vector3D], _name: str = "Vector Plot", _file: str = None):
        """
        Helperfunction to plot a list of 3D vectors using matplotlib

        :param _vectors: reading
        :type _vectors: [vector.Vector3D]

        :param _name: headline of the plot
        :type _name: str

        :param _file: if set, saves the plot as png to given path
        :type _file: str


        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # DEFAULT GRID SIZE
        min_x, min_y, min_z = (-2, -2, -2)
        max_x, max_y, max_z = (2, 2, 2)

        colors = ["red", "green", "blue", "yellow", "black"]
        for idx, v in enumerate(_vectors):

            x = float(v.x)
            y = float(v.y)
            z = float(v.z)

            # EXPAND GRID IF NEEDED
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            min_z = min(min_z, z)
            max_z = max(max_z, z)
            # ADD VECTOR
            ax.quiver(0, 0, 0, x, y, z, color=colors[idx % len(colors)], arrow_length_ratio=0.1)

        # ADD ORIGIN AS BLACK DOT
        ax.plot(0, 0, marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")

        ax.set_xlim([min_x, max_x])
        ax.set_ylim([min_y, max_y])
        ax.set_zlim([min_z, max_z])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        if _name is None:
            _name = "Vector Plot"

        plt.title(_name)

        if _file is None:
            plt.show()
        else:
            if '.png' not in _file:
                _file = _file + ".png"
            plt.savefig(_file)

    @staticmethod
    def generate_openscad_model(_computed_magnet_data: [MRPHallbachArrayResult], _save_filename: str = None, _2d_object_code: bool = True, _add_mounting_holes: bool = True, _add_annotations:bool = True):
        """
        Generates a Hallbach OpenSCAD file of a given MRPHallbachArrayResult object

        :param _computed_magnet_data: a list of magnet result object MRPHallbachArrayResult containing computed magnets
        :type _computed_magnet_data: [MRPHallbachArrayResult.MRPHallbachArrayResult]

        :param _save_filename: save .scad file to filepath e.g. ./tmp/export.scad
        :type _save_filename: str

        :param _2d_object_code: adds openscad projection(cut = true) to allow the generation of dxf files
        :type _2d_object_code: bool

        :param _add_mounting_holes: adds additional mounting holes
        :type _add_mounting_holes: bool

        :param _add_annotations: adds text annotations using magnet_id and type
        :type _add_annotations: bool

        """
        # CHECK USER INPUT
        if _computed_magnet_data is None or len(_computed_magnet_data) <= 0:
            raise MRPHallbachArrayGeneratorException("_computed_magnet_data: is empty")

        for res in _computed_magnet_data:
            if _add_annotations and len(res.magnets) != len(res.annotations):
                raise MRPHallbachArrayGeneratorException("generate_openscad_model: magnets and annotations len are not equal")

        # FIND BIGGEST OUTER DIAMETER AND SMALLEST INNER DIAMETER
        slice_inner_diameter: float = 999
        slice_outer_diameter: float = -999
        max_magnet_height: float = -999

        for res in _computed_magnet_data:
            if slice_inner_diameter is None:
                slice_inner_diameter = res.slice_inner_diameter
            else:
                slice_inner_diameter = min([slice_inner_diameter, res.slice_inner_diameter])

            if slice_outer_diameter is None:
                slice_inner_diameter = res.slice_outer_diameter
            else:
                slice_outer_diameter = max([slice_outer_diameter, res.slice_outer_diameter])

            if max_magnet_height is None:
                max_magnet_height = res.max_magnet_height
            else:
                max_magnet_height = max([max_magnet_height, res.max_magnet_height])

        # CONSTRUCTOR CREATES A SLICE BODY
        hallbach_slice = MRPOpenSCADGenerator.MRPOpenSCADGenerator(slice_inner_diameter, slice_outer_diameter, max_magnet_height)

        # ADD MOUNTING HOLES
        if _add_mounting_holes:
            hole_distance = round(slice_outer_diameter / 10) * 10
            hallbach_slice.append_mounting_holes_to_base_slice(slice_outer_diameter, max_magnet_height, _hole_distance=hole_distance)


        # GENERATE MAGNET CUTOUTS
        # HERE FOR EACH MAGNET THE SET PROPERTIES dim, pos, rot is USED TO GENERATE THE CUTOUT
        for res in _computed_magnet_data:
            for idx, _ in enumerate(res.magnets):
                # CREATE MAGNET CUTOUT WITH ANNOTATION
                if _add_annotations:
                    hallbach_slice.create_magnet_cutout(res.magnets[idx], res.annotations[idx])
                else:
                    hallbach_slice.create_magnet_cutout(res.magnets[idx], None)

        # EXPORT OPNESCAD OBJECT
        hallbach_slice.export_scad(_save_filename, _add_2d_projection=_2d_object_code)
        hallbach_slice.__del__()



    @staticmethod
    def generate_magnet_streamplot(_computed_magnet_data: [MRPHallbachArrayResult], _save_filename:str = None):
        """
        Generates a Hallbach Stream-Field Line Plot of a given MRPHallbachArrayResult object

        :param _computed_magnet_data: a list of magnet result object MRPHallbachArrayResult containing computed magnets
        :type _computed_magnet_data: [MRPHallbachArrayResult.MRPHallbachArrayResult]

        :param _save_filename: save .scad file to filepath e.g. ./tmp/export.scad
        :type _save_filename: str
        """

        # CHECK USER INPUT
        if _computed_magnet_data is None or len(_computed_magnet_data) <= 0:
            raise MRPHallbachArrayGeneratorException("_computed_magnet_data: is empty")

        for res in _computed_magnet_data:
            if len(res.magnets) <= 0:
                raise MRPHallbachArrayGeneratorException(
                    "generate_openscad_model: magnets is empty")

        slice_outer_diameter:float = None
        for res in _computed_magnet_data:
            if slice_outer_diameter is None:
                slice_outer_diameter = res.slice_outer_diameter
            else:
                slice_outer_diameter = max([slice_outer_diameter, res.slice_outer_diameter])
        # CREATE FIGURE
        fig, ax1 = plt.subplots(figsize=(9, 8))
        #CREATE GRID
        xy_size: int = int(slice_outer_diameter * 1.5) #mm
        ts = np.linspace(-xy_size, xy_size, xy_size)
        grid = np.array([[(x, 0, z) for x in ts] for z in ts])

        # POPULATE COLLECTION
        magnet_collection:Collection = Collection(style_label="generate_magnet_streamplot")

        # ADD ALL THE MAGNETS
        for res in _computed_magnet_data:
            for magnet in res.magnets:
                magnet_collection.add(magnet)

        # COMPUTE PLOT OF magnet_collection
        B = getB(magnet_collection, grid)
        Bamp = np.linalg.norm(B, axis=2)
        Bamp /= np.amax(Bamp)

        sp = ax1.streamplot(
            grid[:, :, 0], grid[:, :, 2], B[:, :, 0], B[:, :, 2],
            density=2,
            color=Bamp,
            linewidth=np.sqrt(Bamp) * 3,
            cmap='coolwarm',
        )

        ax1.set(
            title='Magnetic field of coil1',
            xlabel='x-position [mm]',
            ylabel='z-position [mm]',
            aspect=1,
        )
        plt.colorbar(sp.lines, ax=ax1, label='[mT]')



        # SHOW MAGNET CONFIGURATION IN PLOT 2
        for res in _computed_magnet_data:
            for magnet in res.magnets:
                if isinstance(magnet, magpylib.magnet.Cuboid):
                    pass
                #x_start, x_end, y_start, y_end = #TODO magnet_to_points(magnet)
                #ax1.add_patch(plt.Rectangle((x_start, y_start), x_end - x_start, y_end - y_start, facecolor=to_rgba('crimson', 0.01), edgecolor='black', lw=2))


        plt.tight_layout()


        if _save_filename is None or len(_save_filename) <= 0:
            plt.savefig(_save_filename)
        else:
            plt.show()

    @staticmethod
    def generate_1k_hallbach_using_polarisation_direction(_readings: [MRPReading.MRPReading], _min_slice_inner_diameter:float = 20, _slice_outer_diameter_safety_margin:float = 10) -> MRPHallbachArrayResult:
        """
        Generates a 1K hallbach array out of given readings. The result is a set of magpylib magnets with set rotation, position and dimension.
        The magnetization is calculated using the calculate_center_of_gravity function.
        Magnets are aligned on their Z axis.

        :param _readings: a list of readings to generate a 1k hallbach array, length needs to be multiply of 4
        :type _readings: MRPReading.MRPReading

        :param _min_slice_inner_diameter: minimum hallbach ring inner diameter can be bigger depending the magnet size
        :type _min_slice_inner_diameter: float

        :param _slice_outer_diameter_safety_margin: additional
        :type _slice_outer_diameter_safety_margin: float

        :returns: returns magnet (magpylib) instances with set dimensions, rotation and position
        :rtype: MRPHallbachArrayGenerator.MRPHallbachArrayResult
        """
        # CHECK USER INPUT
        if _min_slice_inner_diameter <= 0:
            raise MRPHallbachArrayGeneratorException("_min_slice_inner_diameter cant be smaller than zero :)")

        if _readings is None or len(_readings) <= 0:
            raise MRPHallbachArrayGeneratorException("_readings is None or len is <= 0")

        if len(_readings) % 4 != 0:
            raise MRPHallbachArrayGeneratorException("_readings len is odd or needs to be a multiple of 4")

        for idx, reading in enumerate(_readings):
            if reading.measurement_config.magnet_type is None or reading.measurement_config.magnet_type.is_invalid():
                raise MRPHallbachArrayGeneratorException("get_magnet_type is not set for reading: {}".format(idx))


        # RETURN OBJECT
        result: MRPHallbachArrayResult = MRPHallbachArrayResult()

        # PROCESS EACH MAGNET TO A MAGPYLIB INSTANCE
        # USING GRAVITY OF CENTER
        magpylib_instances: magpylib.magnet = []
        for idx, reading in enumerate(_readings):
            magtype: MRPMagnetTypes.MagnetType = reading.get_magnet_type()

            magnetization_vector = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(reading)
            # CHECK
            if magnetization_vector is None or magnetization_vector[0] is None:
                raise MRPHallbachArrayGeneratorException("calculation of calculate_center_of_gravity failed: {}".format(idx))

            dimension_vector = magtype.get_dimension()

            # CREATE MAGPYLIB INSTANCES
            if magtype.is_cubic():
                magpylib_instances.append(magpylib.magnet.Cuboid(magnetization=magnetization_vector, dimension=dimension_vector))
            elif magtype.is_cylindrical():
                # dimension is (D,H)
                magpylib_instances.append(magpylib.magnet.Cylinder(magnetization=magnetization_vector, dimension=(dimension_vector[0], dimension_vector[1])))
            else:
                raise MRPHallbachArrayGeneratorException("magnet type not implemented: {}".format(idx))

        # ON A 2d PLANCE
        target_orientation = vector.obj(x=1.0, y=0.0, z=0.0)
        # TODO
        for idx, magnet in enumerate(magpylib_instances):

            # 1 step roate magnet so the mag_vecotr is aligned to a XY PLANE
            mag = magnet.magnetization
            orientation = magnet.orientation # CURRENT MAGNET ORIENTATION

            mag_vector = MRPHelpers.normalize_3d_vector(vector.obj(x=mag[0], y=mag[1], z=mag[2]))

            needed_rotation = mag_vector.cross(target_orientation)
            # TODO ONLY MODIFY Z ALIGNMENT
            # ALIGN RESET TO XY
            #R.from_rotvec(in_mag_rotation_applied, degrees=True)

            print("{}".format(mag))
            #MRPHallbachArrayGenerator.plot_vectors([target_orientation, mag_vector, needed_rotation], "Magnet {} CURRENT STATE".format(idx))

            # ROTATE MAGNET TO TARGET DIRECTION
            # ADD orientation
            nr_x: float = needed_rotation.x
            nr_y: float = needed_rotation.y
            nr_z: float = needed_rotation.z
            # APPLY ROTATION DIRECTLY TO INSTANCE REFERENCE
            magpylib_instances[idx].rotate_from_rotvec((nr_x, nr_y, nr_z), degrees=True)
            print(magnet.orientation)


        for idx, magnet in enumerate(magpylib_instances):
            # CHECK RESULTS
            # ALL VECTORS SHOULD ALIGN
            magnetization = vector.obj(x=magnet.magnetization[0], y=magnet.magnetization[1], z=magnet.magnetization[2])
            print(magnet.orientation)
            #position = vector.obj(x=magnetization.)
            mag_vector = MRPHelpers.normalize_3d_vector(vector.obj(x=magnetization.x, y=magnetization.y, z=magnetization.z))
            needed_rotation = mag_vector.cross(target_orientation)
            #MRPHallbachArrayGenerator.plot_vectors([target_orientation, mag_vector], "Magnet {} ROTATED STATE".format(idx))


        # GET MAX MAGNET HEIGHT TO DETERM THE SLICE THICKNESS
        max_magnet_height: float = 0.0  # thickness of the slide = max value of the thickness
        for magnet in _readings:
            t = magnet.get_magnet_type()
            mh = t.get_height()
            max_magnet_height = max([mh, max_magnet_height])
        max_magnet_height_mag = math.sqrt(max_magnet_height * max_magnet_height+max_magnet_height * max_magnet_height+max_magnet_height * max_magnet_height)
        print("max_magnet_height:{} max_magnet_height_mag:{}".format(max_magnet_height, max_magnet_height_mag))


        # GENERATE A SLICE INCLUDING CUTOUTS FOR THE MAGNET
        ## CALCULATE THE OUTER DIAMETER OF THE CYLINDRICAL DISC
        no_magnets_per_quadrant: int = max([len(_readings) / 4, 2])
        min_magnet_spacing = max([_min_slice_inner_diameter, max_magnet_height*(no_magnets_per_quadrant-1)])
        magnet_trajectory: float = min_magnet_spacing*1.5 # add a bit more space between the magnet to ensure material stability

        slice_inner_diameter: float = (magnet_trajectory*2) - max_magnet_height_mag*1.2 # mtrajectory is R for the slices diameter is needed - the max magnet size
        slice_outer_diameter: float = _slice_outer_diameter_safety_margin + slice_inner_diameter + 2*max_magnet_height_mag*1.2 # same for outer diameter but adding 2 times the max magnet size
        #slice_inner_diameter: float = max([_min_slice_inner_diameter, max_magnet_height * no_magnets_per_quadrant])
        #slice_outer_diameter: float = slice_inner_diameter + no_magnets_per_quadrant * max_magnet_height_mag  # *1.5 = add some additinal space #  to add 2 time the magnet size on each side
        #magnet_trajectory: float =  (slice_inner_diameter)/2+max_magnet_height_mag*1.5#+slice_inner_diameter #+ 2#(slice_inner_diameter / 2) + max_magnet_height_mag  # PLACE MAGNETS IN A CIRCLE BETWEEN






        ## ONE HALF OF THE HALLBACH ARRAY IS A 360-DEGREE ROTATION OF HALF OF THE AMOUNTS OF THE MAGNETS
        no_magnets: int = len(_readings)
        rotation_per_magnet: float = 2*(360 / no_magnets / 2) # ROTATION PER MAGNET IN A HALLBACH ARRAY
        print("no_magnets:{} rotation_per_magnet:{} ".format(no_magnets, rotation_per_magnet))

        # SECOND ROTATION FOR THE MAGNET ITSELF IS A 180-DEGREE ROTATION FOR EACH OF THE 4 QUADRANTS
        magnet_initial_rotation: float = 180
        quadrants: int = 4
        magnet_rotation_per_quadrant: float = 180

        inner_magnets_per_quadrant = int((no_magnets/quadrants))# defines the inner magnets per quadrant for a n=8 array with 4 quadrants n=8 =1 inner magnet, due the outer ones are sharing the same quadrant
        rotation_per_magnet_per_quadrant: float = magnet_rotation_per_quadrant/inner_magnets_per_quadrant

        I = 0
        for idx, magnet in enumerate(magpylib_instances):
            reading: MRPReading.MRPReading = _readings[idx]

            # CALCULATE NEW POSITION OF THE MAGNET
            ## MOVE MAGNET TO TO MAGNET_TRAJECTORY
            # ROTATE MAGNET AROUND TRAJECTORY
            magnet_rotation: float = (idx * rotation_per_magnet)
            magnet_rotation_rad: float = math.radians(magnet_rotation % 360) # ROTATION TO RADIANS
            magnet.position = [magnet_trajectory * math.cos(magnet_rotation_rad), magnet_trajectory * math.sin(magnet_rotation_rad), 0]
            print("magnet_rotation:{}".format(magnet.position))

            # CALCULATE ROTATION OF THE MAGNET
            ## => APPLY IN MAGNET ROTATION FOR HALLBACH CANCEL OUT=> Z AXIS ROTATION
            magnet_rotation_itself: float = (magnet_initial_rotation - rotation_per_magnet_per_quadrant * idx) % 360 # 0-180 DEGREE PER QUADRANT
            old_rot = magnet.orientation.as_rotvec(degrees=True) * np.array([0, 0, 1]) # ONLY EXTRACT Z AXIS ROTATION
            in_mag_rotation_applied = old_rot + (magnet_rotation_itself * np.array([0, 0, 1])) # ADD NEW TO OLD ONE = OPTIMIZED ROTATION
            magnet.orientation = R.from_rotvec(in_mag_rotation_applied, degrees=True)


            # ADD MAGNET ID AS ANNOTATION ON TOP OF THE CAD SURFACE
            annotation = "mag{}".format(idx)
            if _readings[idx] is not None:
                annotation = "t{}:i{}".format(reading.measurement_config.magnet_type.to_int(), reading.measurement_config.id)


            # ADD GENERATED DATA TO THE RESULT SET
            result.magnets.append(magnet)
            result.annotations.append(annotation)

        result.description = "generate_1k_hallbach_using_polarisation_direction"
        result.max_magnet_height = max_magnet_height # SLICE THICKNESS ON Z AXIS
        result.slice_inner_diameter = slice_inner_diameter
        result.slice_outer_diameter = slice_outer_diameter

        return result



















        # ROTATE MAGNETS AROUND
        # 1st -> ROTATE THAT MAGNETISATION DIRECTION LOOKS UP
        # 2nd -> CALCULATE ROATION FOR EACH MANGET

    def __init__(self):
        pass

