import magpylib
import openpyscad as ops

class MRPOpenSCADGeneratorException(Exception):
    def __init__(self, message="MRPOpenSCADGeneratorException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPOpenSCADGenerator():

    def create_magnet(_magnet: magpylib.magnet, _safety_margin_mm:float = 0.1) -> ops.Union:
        if _magnet is None:
            raise MRPOpenSCADGeneratorException("_magnet is None")

        if _safety_margin_mm is None:
            _safety_margin_mm = 0.0

        u = ops.Union()


        return u

    def create_cylinder_with_cutout(self, _inner_diameter_mm:float = None, _outher_diameter_mm:float = None, _thickness_mm: float = None):
        if _thickness_mm is None:
            raise MRPOpenSCADGeneratorException("_thickness cant be none")
        if _inner_diameter_mm > _outher_diameter_mm:
            raise MRPOpenSCADGeneratorException("_inner_diameter is bigger than _outher_diameter")


        cylinder_base = ops.Cylinder(d=_outher_diameter_mm, h=_thickness_mm, center=True)

        if _inner_diameter_mm is not None and _inner_diameter_mm > 0.0:
            cylinder_innser = ops. _inner_diameter_mm


        #ops.cylinder(20, d=20, center=true);

    def __init__(self):
        pass


