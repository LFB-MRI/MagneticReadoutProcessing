
class MRPPHalRestRequestResponseState(object):
    success: bool = False
    sensortypes: [int] = []
    version: str = "0.0.0"
    id: str = ""
    sensorcount: int = 0
    initialized: bool = False
    capabilities: [str] = []
    commands: [str] = []

    def __init__(self):
        pass

    def __json__(self):
        return self.__dict__