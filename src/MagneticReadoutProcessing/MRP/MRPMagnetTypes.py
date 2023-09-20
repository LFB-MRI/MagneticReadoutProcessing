""" collection of magnet specifications for different magnet types such as cubic n45,... """
from enum import Enum

class MRPMagnetTypeException(Exception):
    def __init__(self, message="MRPMagnetTypeException thrown"):
        self.message = message
        super().__init__(self.message)

class MagnetType(Enum):
    """
    Enum class for holding some basic information about a measured magnet.
    Please add further magnet definition here.
    """
    # GENERAL NOTATION <type>_<shape>_size
    # CUBIC_XxYxZ # dimensions in mm
    NOT_SPECIFIED = 0
    RANDOM_MAGNET = 1
    # CUBE
    N45_CUBIC_12x12x12 = 2
    N45_CUBIC_15x15x15 = 3
    N45_CUBIC_9x9x9 = 4

    # CYLINDER
    N45_CYLINDER_5x10 = 5

    # SPHERE
    N45_SPHERE_10 = 6 # 10mm sphere




    @staticmethod
    def from_int(_val: int):
        try:
            return MagnetType(_val)
        except:
            return None


    def __int__(self):
        return self.value
    def to_int(self) -> int:
        return int(self.value)
    def is_invalid(self) -> bool:
        if self.name == 'NOT_SPECIFIED' or self.value <= 0:
            return True
        else:
            return False

    def is_cubic(self) -> bool:
        if 'cubic' in str(self.name).lower():
            return True
        return False

    def is_cylindrical(self):
        if 'cylinder' in str(self.name).lower():
            return True
        return False
    def get_dimension(self) -> (int, int, int):
        """
        Returns the dimension in mm from the selected magnet type

        :returns: Returns (x, y, z)  on a cubic magnet, (d h, 0) on a cylindrical magnet
        :rtype: tuple
        """
        if self.is_cubic():
            sp = str(self.name).split('_')[2].split("x")
            return (int(sp[0]), int(sp[1]), int(sp[2]))
        elif self.is_cylindrical():
            sp = str(self.name).split('_')[2].split("x")
            return (int(sp[0]), int(sp[1]), 0)


        raise MRPMagnetTypeException("get_dimension for this MagnetType not implemented")

    def get_height(self) -> int:
        """
        Returns the maximum height of the selected magnet type.
        The function returns the max value of (x,y,z) or (d,h)

        :returns: max value of the dimension vector
        :rtype: int
        """

        dim = self.get_dimension()
        if dim is None:
            raise MRPMagnetTypeException("get_height returned None")

        return max([dim[0], dim[1], dim[2]])