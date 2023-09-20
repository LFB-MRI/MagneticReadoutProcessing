""" The MRPReadoutSource class is a BaseSource for the Python magpylib (https://magpylib.readthedocs.io/en/latest/)"""
import numpy as np
from magpylib._src.fields.field_BH_sphere import magnet_sphere_field

# https://github.com/magpylib/magpylib/blob/main/magpylib/_src/fields/field_BH_cuboid.py#L10

from magpylib._src.obj_classes.class_BaseExcitations import BaseSource, BaseMagnet



from MRP import MRPReading, MRPAnalysis

class MRPReadoutSource(BaseMagnet):
    """User-defined custom source.

    Can be used as `sources` input for magnetic field computation.

    When `position=(0,0,0)` and `orientation=None` local object coordinates
    coincide with the global coordinate system.

    Parameters
    ----------
    field_func: callable, default=`None`
        The function for B- and H-field computation must have the two positional arguments
        `field` and `observers`. With `field='B'` or `field='H'` the B- or H-field in units
        of [mT] or [kA/m] must be returned respectively. The `observers` argument must
        accept numpy ndarray inputs of shape (n,3), in which case the returned fields must
        be numpy ndarrays of shape (n,3) themselves.

    position: array_like, shape (3,) or (m,3), default=`(0,0,0)`
        Object position(s) in the global coordinates in units of [mm]. For m>1, the
        `position` and `orientation` attributes together represent an object path.

    orientation: scipy `Rotation` object with length 1 or m, default=`None`
        Object orientation(s) in the global coordinates. `None` corresponds to
        a unit-rotation. For m>1, the `position` and `orientation` attributes
        together represent an object path.

    parent: `Collection` object or `None`
        The object is a child of it's parent collection.

    style: dict
        Object style inputs must be in dictionary form, e.g. `{'color':'red'}` or
        using style underscore magic, e.g. `style_color='red'`.

    Returns
    -------
    source: `CustomSource` object

    Examples
    --------
    With version 4 `CustomSource` objects enable users to define their own source
    objects, and to embedded them in the Magpylib object oriented interface. In this example
    we create a source that generates a constant field and evaluate the field at observer
    position (1,1,1) given in [mm]:

    #>>> import numpy as np
    #>>> import magpylib as magpy
    #>>>
    #>>> funcBH = lambda field, observers: np.array([(100 if field=='B' else 80,0,0)]*len(observers))
    #>>> src = magpy.misc.CustomSource(field_func=funcBH)
    #>>> H = src.getH((1,1,1))
    #>>> print(H)
    [80.  0.  0.]

    We rotate the source object, and compute the B-field, this time at a set of observer positions:

    #>>> src.rotate_from_angax(45, 'z')
    CustomSource(id=...)
    #>>> B = src.getB([(1,1,1), (2,2,2), (3,3,3)])
    #>>> print(B)
    [[70.71067812 70.71067812  0.        ]
     [70.71067812 70.71067812  0.        ]
     [70.71067812 70.71067812  0.        ]]

    The same result is obtained when the rotated source moves along a path away from an
    observer at position (1,1,1). This time we use a `Sensor` object as observer.

    #>>> src.move([(-1,-1,-1), (-2,-2,-2)])
    CustomSource(id=...)
    #>>> sens = magpy.Sensor(position=(1,1,1))
    #>>> B = src.getB(sens)
    #>>> print(B)
    [[70.71067812 70.71067812  0.        ]
     [70.71067812 70.71067812  0.        ]
     [70.71067812 70.71067812  0.        ]]
    """




    _editable_field_func = True


    _field_func = staticmethod(magnet_sphere_field) # TODO REPLACE
    _field_func_kwargs_ndim = {"magnetization": 2, "diameter": 1}
    # HERE A VISAL REPRESENTATION IS NOT NESSESSARY DUE TO THE READING ONLY CONTAINS POINTDATA, SO WE ARE USING A SIMPLE SPHERE
    #_draw_func = make_Sphere



    def __init__(self, _reading: MRPReading.MRPReading, _position: tuple=(0, 0, 0), _orientation:tuple=None, _style=None, **kwargs,):
        # init inheritance

        # TODO CALC MAGNETIZATION VECTOR
        # MITTELS ID LUT FÜR READING DATA MACHEN ?
        magnetization = MRPAnalysis.MRPAnalysis.calculate_magnetization(_reading)

        style = None

        if 'sensor_distance_radius' in _reading.measurement_config:
            self._field_func_kwargs_ndim['diameter'] = _reading.measurement_config['sensor_distance_radius']


        super().__init__(_position, _orientation, magnetization, style, **kwargs)
