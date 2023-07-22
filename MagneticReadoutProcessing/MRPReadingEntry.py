

class MRPReadingEntry(object):
    """ Class holds all values for one read entry such as value and position"""
    value = None # [mT]
    temperature = None # [°C]
    phi = None
    theta = None

    reading_index_phi = None
    reading_index_theta = None
    is_valid = False
    id = None
    def __init__(self):
        self.value = None



    def __dict__(self):
        return {
            'value': self.value,
            'temperature': self.temperature,
            'phi': self.phi,
            'theta': self.theta,
            'reading_index_phi': self.reading_index_phi,
            'reading_index_theta': self.reading_index_theta,
            'is_valid': self.is_valid,
            'id': self.id
        }
