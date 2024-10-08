from enum import Enum

"""  one datapoint for a reading """
class MRPReadingEntryException(Exception):
    def __init__(self, message="MRPReadingEntryException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPReadingEntryUnit(Enum):
    UNIT_UNSPECIFIED = 0
    UNIT_uT = 1
    UNIT_mT = 2
    UNIT_T = 3

    @staticmethod
    def from_int(_val: int):
        try:
            return MRPReadingEntryUnit(_val)
        except:
            return MRPReadingEntryUnit.UNIT_UNSPECIFIED

class MRPReadingEntry:
    """ Class holds all values for one read entry such as value and position"""
    _value: float = None # [mT]
    _phi: float = None
    _theta: float = None
    _reading_index_phi: int = None
    _reading_index_theta: int = None
    _is_valid: bool = False
    _id: int = None
    _temperature: float = -254.0
    _unit: MRPReadingEntryUnit = MRPReadingEntryUnit.UNIT_UNSPECIFIED


    @property
    def unit(self) -> MRPReadingEntryUnit:
        return self._unit

    @unit.setter
    def unit(self, p_value: MRPReadingEntryUnit):
        self._unit = p_value


    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, p_value: float):
        self._temperature = p_value

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, p_value: float):
        self._value = p_value

    @property
    def phi(self) -> float:
        return self._phi

    @phi.setter
    def phi(self, p_value: float):
        self._phi = p_value

    @property
    def theta(self) -> float:
        return self._theta

    @theta.setter
    def theta(self, p_value: float):
        self._theta = p_value




    @property
    def reading_index_phi(self) -> int:
        return self._reading_index_phi

    @reading_index_phi.setter
    def reading_index_phi(self, p_value: int):
        self._reading_index_phi = p_value

    @property
    def reading_index_theta(self) -> int:
        return self._reading_index_theta

    @reading_index_theta.setter
    def reading_index_theta(self, p_value: int):
        self._reading_index_theta = p_value

    @property
    def is_valid(self) -> bool:
        return self._is_valid

    @is_valid.setter
    def is_valid(self, p_value: bool):
        self._is_valid = p_value

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, p_value: int):
        self._id = p_value


    def __init__(self, p_id: int = None, p_value: float = None, p_phi: float = None, p_theta: float = None, p_rip: int = None, p_rit: int = None, p_is_valid: bool = False, p_temperature: float = -254.0, p_unit: MRPReadingEntryUnit = MRPReadingEntryUnit.UNIT_UNSPECIFIED):
            self._id = p_id
            self._value = p_value
            self._phi = p_phi
            self._theta = p_theta
            self._reading_index_phi = p_rip
            self._reading_index_theta = p_rit
            self._is_valid = p_is_valid
            self._temperature = p_temperature
            self._unit = p_unit

    def from_dict(self, _dict: dict, _import_scale_factor: float = 1.0):
        errors: int = 0
        try:
            if 'value' in _dict:
                self._value = float(_dict.get('value', 0.0)) * _import_scale_factor
                errors = errors + 1

            if 'phi' in _dict:
                v = _dict.get('phi', 0.0)
                if v is None:
                    v = 0.0
                self._phi = float(v)
                errors = errors + 1

            if 'theta' in _dict:
                v = _dict.get('theta', 0.0)
                if v is None:
                    v = 0.0
                self._theta = float(v)
                errors = errors + 1

            if 'reading_index_phi' in _dict:
                v = _dict.get('reading_index_phi', 0)
                if v is None:
                    v = 0.0
                self._reading_index_phi = int(v)
                errors = errors + 1

            if 'reading_index_theta' in _dict:
                v = _dict.get('reading_index_theta', 0)
                if v is None:
                    v = 0.0
                self._reading_index_theta = int(v)
                errors = errors + 1

            if 'is_valid' in _dict:
                v = _dict.get('is_valid', False)
                if v is None:
                    v = True
                self._is_valid = bool(v)
                errors = errors + 1

            if 'id' in _dict:
                v = _dict.get('id', -1)
                if v is None:
                    v = 0
                self._id = int(v)
                errors = errors + 1

            if 'temperature' in _dict:
                v = _dict.get('temperature', 25.0)
                if v is None:
                    v = 0.0
                self._temperature = float(v)
                errors = errors + 1

            if 'unit' in _dict:
                self._unit = MRPReadingEntryUnit.UNIT_UNSPECIFIED
                try:
                    self._unit = MRPReadingEntryUnit.from_int(_dict.get('unit', MRPReadingEntryUnit.UNIT_UNSPECIFIED.value))
                except:
                    self._unit = MRPReadingEntryUnit.UNIT_UNSPECIFIED

                errors = errors + 1
        except Exception as e:
            print(e)
            raise MRPReadingEntryException("from_dict import failed {}".format(e))
        
        
    def __dict__(self) -> dict:
        try:
            return {
                'value': self._value,
                'phi': self._phi,
                'theta': self._theta,
                'reading_index_phi': self._reading_index_phi,
                'reading_index_theta': self._reading_index_theta,
                'is_valid': self._is_valid,
                'id': self._id,
                'temperature': self._temperature,
                'unit': self._unit.value
            }
        except Exception as e:
            raise MRPReadingEntryException("__dict__ import failed {}".format(e))
    

    def to_dict(self) -> dict:
        return self.__dict__()
