# https://chatgpt.com/share/66e4269a-1fbc-8008-a8fa-979a2dfd4025
import math

from MagneticReadoutProcessing.src.MagneticReadoutProcessing.MRP import MRPMagnetTypes

class MRPPhysics:

    MAGNETIC_VACUUM_PERMEABILITY: float = 4 * math.pi * 10**-6


    @staticmethod
    def calculate_remancence_value(_magnettype: MRPMagnetTypes.MagnetType, _sensor_distance_mm: float, _magnetic_vacuum_permeability: float = MAGNETIC_VACUUM_PERMEABILITY) -> float:

        volume_m: float = _magnettype.get_volume()
        pass
