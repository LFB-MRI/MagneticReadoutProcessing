# https://chatgpt.com/share/66e4269a-1fbc-8008-a8fa-979a2dfd4025
import math


import sys
from os.path import dirname
t = dirname(__file__)
sys.path.append(t)


from MRP import MRPMagnetTypes, MRPAnalysis, MRPReading, MRPReadingEntry



class MRPPhysics:

    MAGNETIC_VACUUM_PERMEABILITY: float = 4 * math.pi * 10**-7 # A/m


    @staticmethod
    def calculate_remancence_value(_reading: MRPReading, _sensor_distance_mm: float, _magnetic_vacuum_permeability: float = MAGNETIC_VACUUM_PERMEABILITY) -> float:
        """
        Calculates the remancence of a magnet, by a given sensor measurement with a known distance.

        :returns: returns remancence in mT
        :rtype: float
        """
        magnet_type: MRPMagnetTypes.MagnetType = _reading.get_magnet_type()

        if magnet_type == MRPMagnetTypes.MagnetType.NOT_SPECIFIED:
            raise Exception("Magnet type not specified")


        v_volume_magnet: float = magnet_type.get_volume()
        d_distance_sensor_magnet: float = _sensor_distance_mm * (magnet_type.get_height()/2)





        # Solving for M (which relates to Br):
        b_magnetic_field_measured_at_distance: float = MRPAnalysis.calculate_mean(_reading)
        magnetization_of_material: float = (b_magnetic_field_measured_at_distance * pow(d_distance_sensor_magnet, 3) * 4 * math.pi) / (2 * _magnetic_vacuum_permeability * v_volume_magnet)

        # Convert M to BR
        br: float = _magnetic_vacuum_permeability * magnetization_of_material # T
        br = br * 1000.0 # T -> mT





        return br
