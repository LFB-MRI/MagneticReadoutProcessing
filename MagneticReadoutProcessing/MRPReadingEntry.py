
class MRPReadingEntryException(Exception):
    def __init__(self, message="MRPReadingEntryException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPReadingEntry:
    """ Class holds all values for one read entry such as value and position"""
    _value = None # [mT]
    _phi = None
    _theta = None
    _reading_index_phi = None
    _reading_index_theta = None
    _is_valid = False
    _id = None
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
    def reading_index_phi(self, value: float):
        self._reading_index_phi = value

    @property
    def reading_index_theta(self):
        return self._reading_index_theta

    @reading_index_theta.setter
    def reading_index_theta(self, value: float):
        self._reading_index_theta = value

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value: float):
        self._is_valid = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: float):
        self._id = value


    def __init__(self, p_id: int = None, p_value: float = None, p_phi: float = None, p_theta: float = None, p_rip: int = None, p_rit: int = None, p_is_valid: bool = False):
            self._id = p_id
            self._value = p_value
            self._phi = p_phi
            self._theta = p_theta
            self._reading_index_phi = p_rip
            self._reading_index_theta = p_rit
            self._is_valid = p_is_valid

    def from_dict(self, _dict: dict):
        errors = 0
        if 'value' in _dict:
            self._value = float(_dict['value'])
            errors = errors + 1

        if 'phi' in _dict:
            self._phi = float(_dict['phi'])
            errors = errors + 1

        if 'theta' in _dict:
            self._theta = float(_dict['theta'])
            errors = errors + 1
        if 'reading_index_phi' in _dict:
            self._reading_index_phi = int(_dict['reading_index_phi'])
            errors = errors + 1

        if 'reading_index_theta' in _dict:
            self._reading_index_theta = int(_dict['reading_index_theta'])
            errors = errors + 1

        if 'is_valid' in _dict:
            self._is_valid = bool(_dict['is_valid'])
            errors = errors + 1
        if 'id' in _dict:
            self._id = int(_dict['id'])
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
            'id': self._id
        }
    def to_dict(self) -> dict:
        return self.__dict__()