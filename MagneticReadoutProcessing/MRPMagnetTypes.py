from enum import Enum





class MagnetType(Enum):

    # GENERAL NOTATION <type>_<shape>_size
    # CUBIC_XxYxZ # dimensions in mm
    NOT_SPECIFIED = 0
    N45_CUBIC_12x12x12 = 1
    N45_CUBIC_15x15x15 = 2
    N45_CUBIC_9x9x9 = 3

    N45_CYLINDER_5x10 = 4


    def __init__(self):
        pass


    @staticmethod
    def from_int(_val: int):
        try:
            return MagnetType(_val).name
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

    def is_cylinder(self):
        if 'cylinder' in str(self.name).lower():
            return True
        return False
    def get_dimension(self) -> (int, int, int):
        if self.is_cubic():
            sp = str(self.name).split('_')[2].split("x")
            return (sp[0], sp[1], sp[2])
        elif self.is_cubic():
            sp = str(self.name).split('_')[2].split("x")
            return (sp[0], sp[1])

        return None

