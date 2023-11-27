"""  stores basic metadata about a reading """

import math

from MRP import MRPMagnetTypes

class MRPReadingEntryException(Exception):
    def __init__(self, message="MRPReadingEntryException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPMeasurementConfig:
    """ Class holds all information about the measurement such as values per axis, half/fullsphere or sensordistance"""

    _n_phi: int = 0
    _n_theta: int = 0
    _phi_radians: float = 0.0
    _theta_radians: float = 0.0
    _sensor_distance_radius: float = 1.0
    _sensor_id: int = 0
    _magnet_type: MRPMagnetTypes.MagnetType = MRPMagnetTypes.MagnetType.NOT_SPECIFIED
    _id: str = 0

    @property
    def n_phi(self) -> int:
        return self._n_phi

    @n_phi.setter
    def n_phi(self, value: int):
        self._n_phi = value

    @property
    def n_theta(self) -> int:
        return self._n_theta

    @n_theta.setter
    def n_theta(self, value: int):
        self._n_theta = value

    @property
    def phi_radians(self) -> float:
        return self._phi_radians

    @phi_radians.setter
    def phi_radians(self, value: float):
        self._phi_radians = value

    @property
    def theta_radians(self) -> float:
        return self._theta_radians

    @theta_radians.setter
    def theta_radians(self, value: float):
        self._theta_radians = value

    @property
    def sensor_distance_radius(self):
        return self._sensor_distance_radius

    @sensor_distance_radius.setter
    def sensor_distance_radius(self, value: float):
        self._sensor_distance_radius = value

    @property
    def sensor_id(self) -> int:
        return self._sensor_id

    @sensor_id.setter
    def sensor_id(self, value: int):
        self._sensor_id = value

    @property
    def magnet_type(self) -> MRPMagnetTypes.MagnetType:
        return self._magnet_type

    @magnet_type.setter
    def magnet_type(self, value: MRPMagnetTypes.MagnetType):
        self._magnet_type = value

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    def __init__(self,p_id: int = 0, p_magnettype: MRPMagnetTypes.MagnetType = MRPMagnetTypes.MagnetType.NOT_SPECIFIED, p_nphi: int = None, p_ntheta: int = None, p_phiradians: float = None,
                 p_thetaradians: float = None, p_sensordistanceradius: float = 1.0, p_sensorid: int = 0):

        self._n_phi: int = p_nphi
        self._n_theta: int = p_ntheta
        self._phi_radians: float = p_phiradians
        self._theta_radians: float = p_thetaradians
        self._sensor_distance_radius: float = p_sensordistanceradius
        self._sensor_id: int = p_sensorid
        self._magnet_type: MRPMagnetTypes.MagnetType = p_magnettype
        self._id: int = p_id



    def set_resolution(self, _n_theta:int, _n_phi:int):
        self._n_theta = _n_theta
        self._n_phi = _n_phi

    def configure_fullsphere(self):
        self._n_theta = 18
        self._n_phi = 36
        self._theta_radians = math.radians(180)
        self._phi_radians = math.radians(360)

    def configure_fullsphere_custom(self, _measurement_points: int = 1, _theta_phi_equal: bool = False):
        self.configure_fullsphere()

        if _measurement_points <= 0:
            _measurement_points = 1

        #if not (_measurement_points % 2) == 0:
        #    _measurement_points = _measurement_points + 1

        self._n_theta = _measurement_points

        if not _theta_phi_equal:
            self._n_phi = _measurement_points * 2
        else:
            self._n_phi = self._n_theta


    def configure_halfsphere(self):
        self._n_theta = 9
        self._n_phi = 36
        self._theta_radians = math.radians(90)
        self.phi_radians = math.radians(360)


    def __dict__(self) -> dict:
        return {
            'id': self._id,
            'n_phi': self._n_phi,
            'n_theta': self._n_theta,
            'theta_radians': self._theta_radians,
            'phi_radians': self._phi_radians,
            'sensor_distance_radius': self._sensor_distance_radius,
            'sensor_id': self._sensor_id,
            'magnet_type': self._magnet_type.value
        }

    def to_dict(self) -> dict:
        return self.__dict__()

    def from_dict(self, _dict: dict):
        errors = 0
        if 'id' in _dict:
            self._id = str(_dict['id'])
            errors = errors + 1
        if 'n_phi' in _dict:
            self._n_phi = int(_dict['n_phi'])
            errors = errors + 1
        if 'n_theta' in _dict:
            self._n_theta = int(_dict['n_theta'])
            errors = errors + 1
        if 'phi_radians' in _dict:
            self._phi_radians = float(_dict['phi_radians'])
            errors = errors + 1
        if 'theta_radians' in _dict:
            self._theta_radians = float(_dict['theta_radians'])
            errors = errors + 1
        if 'sensor_distance_radius' in _dict:
            self._sensor_distance_radius = float(_dict['sensor_distance_radius'])
            errors = errors + 1
        if 'sensor_id' in _dict:
            self._sensor_id = int(_dict['sensor_id'])
            errors = errors + 1
        if 'magnet_type' in _dict:
            self._magnet_type = MRPMagnetTypes.MagnetType.from_int(_dict['magnet_type'])
            errors = errors + 1
