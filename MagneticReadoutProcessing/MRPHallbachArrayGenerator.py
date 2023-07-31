from MRPReading import MRPReading, MRPReadingEntry
from solid import *
import magpylib as magpy

from MagneticReadoutProcessing import MRPAnalysis


class MRPHallbachArrayGeneratorException(Exception):
    def __init__(self, message="MRPHallbachArrayGeneratorException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPHallbachArrayGenerator:

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
            type = reading.get_magnet_type()

            magnetization_vector = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(reading)
            # CHECK
            if magnetization_vector is None or magnetization_vector[0] is None:
                raise MRPHallbachArrayGeneratorException("calculation of calculate_center_of_gravity failed: {}".format(idx))

            dimension_vector = type.get_dimension()

            # CREATE MAGPYLIB INSTANCES
            if type.is_cubic():
                magpylib_instances.append(magpy.magnet.Cuboid(magnetization=magnetization_vector, dimension=dimension_vector))
            elif type.is_cylinder():
                magpylib_instances.append(magpy.magnet.Cylinder(magnetization=magnetization_vector, dimension=(dimension_vector[0], dimension_vector[1])))
            else:
                raise MRPHallbachArrayGeneratorException("magnet type not implemented: {}".format(idx))


        # ROTATE MAGNETS AROUND
        # 1st -> ROTATE THAT MAGNETISATION DIRECTION LOOKS UP
        # 2nd -> CALCULATE ROATION FOR EACH MANGET

    def __init__(self):
        pass

