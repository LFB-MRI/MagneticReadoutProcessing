import magpylib
from solid import *
import vector
import matplotlib.pyplot as plt
import numpy as np

from MagneticReadoutProcessing import MRPReading, MRPReadingEntry, MRPAnalysis, MRPMeasurementConfig, MRPMagnetTypes

class MRPHallbachArrayGeneratorException(Exception):
    def __init__(self, message="MRPHallbachArrayGeneratorException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPHallbachArrayGenerator:

    @staticmethod
    def plot_vectors(_vectors: [vector.Vector3D]):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        v1 = np.array([1, 2, 3])
        v2 = np.array([-2, 1, 4])

        # VECTOR 1
        ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', arrow_length_ratio=0.1)
        # VECTOR 2
        ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', arrow_length_ratio=0.1)

        ax.set_xlim([-3, 3])
        ax.set_ylim([-3, 3])
        ax.set_zlim([-3, 3])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title('3D Vector Plot')

        plt.show()

    @staticmethod
    def magpylib_magnet_to_openscad(_magnet: magpylib.magnet):
        pass
    @staticmethod
    def generate_1k_hallbach_using_polarisation_direction(_reading: [MRPReading]):

        if _reading is None or len(_reading) <= 0:
            raise MRPHallbachArrayGeneratorException("get_magnet_type is not set for reading: {}".format(idx))

        for idx, reading in enumerate(_reading):
            if reading.get_magnet_type() is None or reading.get_magnet_type().is_invalid():
                raise MRPHallbachArrayGeneratorException("get_magnet_type is not set for reading: {}".format(idx))


        # PROCESS EACH MAGNET TO A MAGPYLIB INSTANCE
        # USING GRAVITY OF CENTER
        magpylib_instances = []
        for idx, reading in enumerate(_reading):
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
            orientation = magnet.orientation

            print("{}".format(mag))
            MRPHallbachArrayGenerator.plot_vectors([target_orientation, vector.Vector3D(x=mag[0], y=mag[1], z=mag[2]), ])





        # ROTATE MAGNETS AROUND
        # 1st -> ROTATE THAT MAGNETISATION DIRECTION LOOKS UP
        # 2nd -> CALCULATE ROATION FOR EACH MANGET

    def __init__(self):
        pass

