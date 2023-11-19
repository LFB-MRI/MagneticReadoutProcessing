
class MRPPHalRestRequestResponseState(object):
    success: bool
    sensortype: str
    version: str
    id: str
    sensorcount: int
    initialized: bool

    def __init__(self):
        pass

    def __json__(self):
        return self.__dict__