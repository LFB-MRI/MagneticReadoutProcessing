import magpylib
from solid import *
import vector
import matplotlib.pyplot as plt
import numpy as np

from MagneticReadoutProcessing import MRPReading, MRPReadingEntry, MRPAnalysis, MRPMeasurementConfig, MRPMagnetTypes, MRPHelpers

class MRPHallbachArrayGeneratorException(Exception):
    def __init__(self, message="MRPHallbachArrayGeneratorException thrown"):
        self.message = message
        super().__init__(self.message)

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


        min_x, min_y, min_z = (-2, -2, -2)
        max_x, max_y, max_z = (2, 2, 2)

        colors = ["red", "green", "blue", "yellow", "black"]
        for idx, v in enumerate(_vectors):

            x = float(v.x)
            y = float(v.y)
            z = float(v.z)


            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            min_z = min(min_z, z)
            max_z = max(max_z, z)
            # ADD VECTOR
            ax.quiver(0, 0, 0, x, y, z, color=colors[idx % len(colors)], arrow_length_ratio=0.1)

        ax.plot(0, 0, marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")

        ax.set_xlim([min_x, max_x])
        ax.set_ylim([min_y, max_y])
        ax.set_zlim([min_z, max_z])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title(_name)

        if _file is None:
            plt.show()
        else:
            if '.png' not in _file:
                _file = _file + ".png"
            plt.savefig(_file)

    @staticmethod
    def magpylib_magnet_to_openscad(_magnet: magpylib.magnet):
        pass


    @staticmethod
    def generate_1k_hallbach_using_polarisation_direction(_readings: [MRPReading.MRPReading]):
        """
        Generates a Hallbach OpenSCAD file of a given list of readings using calculate_center_of_gravity algorithm to rotate the magnet into the right direction

        :param _readings: a list of readings to generate a 1k hallbach array
        :type _readings: MRPReading.MRPReading

        """
        if _readings is None or len(_readings) <= 0:
            raise MRPHallbachArrayGeneratorException("get_magnet_type is not set for reading: {}".format(idx))

        for idx, reading in enumerate(_readings):
            if reading.get_magnet_type() is None or reading.get_magnet_type().is_invalid():
                raise MRPHallbachArrayGeneratorException("get_magnet_type is not set for reading: {}".format(idx))


        # PROCESS EACH MAGNET TO A MAGPYLIB INSTANCE
        # USING GRAVITY OF CENTER
        magpylib_instances = []
        for idx, reading in enumerate(_readings):
            magtype = reading.get_magnet_type()

            magnetization_vector = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(reading)
            # CHECK
            if magnetization_vector is None or magnetization_vector[0] is None:
                raise MRPHallbachArrayGeneratorException("calculation of calculate_center_of_gravity failed: {}".format(idx))

            dimension_vector = magtype.get_dimension()

            # CREATE MAGPYLIB INSTANCES
            if magtype.is_cubic():
                magpylib_instances.append(magpylib.magnet.Cuboid(magnetization=magnetization_vector, dimension=dimension_vector))
            elif magtype.is_cylindrical():
                magpylib_instances.append(magpylib.magnet.Cylinder(magnetization=magnetization_vector, dimension=(dimension_vector[0], dimension_vector[1])))
            else:
                raise MRPHallbachArrayGeneratorException("magnet type not implemented: {}".format(idx))

        # ON A 2d PLANCE
        target_orientation = vector.obj(x=1.0, y=0.0, z=0.0)

        for idx, magnet in enumerate(magpylib_instances):

            # 1 step roate magnet so the mag_vecotr is aligned to a XY PLANE
            mag = magnet.magnetization
            orientation = magnet.orientation # CURRENT MAGNET ORIENTATION

            mag_vector = MRPHelpers.normalize_3d_vector(vector.obj(x=mag[0], y=mag[1], z=mag[2]))

            rot = mag_vector.deltaangle(target_orientation)
            print("{}".format(mag))
            MRPHallbachArrayGenerator.plot_vectors([target_orientation, mag_vector])





        # ROTATE MAGNETS AROUND
        # 1st -> ROTATE THAT MAGNETISATION DIRECTION LOOKS UP
        # 2nd -> CALCULATE ROATION FOR EACH MANGET

    def __init__(self):
        pass

