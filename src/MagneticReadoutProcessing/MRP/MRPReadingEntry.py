"""  one datapoint for a reading """
class MRPReadingEntryException(Exception):
    def __init__(self, message="MRPReadingEntryException thrown"):
        self.message = message
        super().__init__(self.message)

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

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        self._temperature = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    @property
    def phi(self):
        return self._phi

    @phi.setter
    def phi(self, value: float):
        self._phi = value

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, value: float):
        self._theta = value




    @property
    def reading_index_phi(self):
        return self._reading_index_phi

    @reading_index_phi.setter
    def reading_index_phi(self, value: int):
        self._reading_index_phi = value

    @property
    def reading_index_theta(self):
        return self._reading_index_theta

    @reading_index_theta.setter
    def reading_index_theta(self, value: int):
        self._reading_index_theta = value

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value: bool):
        self._is_valid = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value


    def __init__(self, p_id: int = None, p_value: float = None, p_phi: float = None, p_theta: float = None, p_rip: int = None, p_rit: int = None, p_is_valid: bool = False, p_temperature: float = -254.0):
            self._id = p_id
            self._value = p_value
            self._phi = p_phi
            self._theta = p_theta
            self._reading_index_phi = p_rip
            self._reading_index_theta = p_rit
            self._is_valid = p_is_valid
            self._temperature = p_temperature

    def from_dict(self, _dict: dict, _import_scale_factor: float = 1.0):
        errors = 0
        if 'value' in _dict:
            self._value = float(_dict['value']) * _import_scale_factor
            errors = errors + 1

        if 'phi' in _dict:
            v = _dict.get('phi')
            if v is None:
                v = 0.0
            self._phi = float(v)
            errors = errors + 1

        if 'theta' in _dict:
            v = _dict.get('theta')
            if v is None:
                v = 0.0
            self._theta = float(v)
            errors = errors + 1

        if 'reading_index_phi' in _dict:
            v = _dict.get('reading_index_phi')
            if v is None:
                v = 0.0
            self._reading_index_phi = int(v)
            errors = errors + 1

        if 'reading_index_theta' in _dict:
            v = _dict.get('reading_index_theta')
            if v is None:
                v = 0.0
            self._reading_index_theta = int(v)
            errors = errors + 1

        if 'is_valid' in _dict:
            v = _dict.get('is_valid')
            if v is None:
                v = True
            self._is_valid = bool(v)
            errors = errors + 1

        if 'id' in _dict:
            v = _dict.get('id')
            if v is None:
                v = 0
            self._id = int(v)
            errors = errors + 1

        if 'temperature' in _dict:
            v = _dict.get('temperature')
            if v is None:
                v = 0.0
            self._temperature = float(v)
            errors = errors + 1

        if errors < len(self.__dict__()):
            raise MRPReadingEntryException("from_dict import failed")
    def __dict__(self) -> dict:
        return {
            'value': self._value,
            'phi': self._phi,
            'theta': self._theta,
            'reading_index_phi': self._reading_index_phi,
            'reading_index_theta': self._reading_index_theta,
            'is_valid': self._is_valid,
            'id': self._id,
            'temperature': self._temperature
        }
    def to_dict(self) -> dict:
        return self.__dict__()