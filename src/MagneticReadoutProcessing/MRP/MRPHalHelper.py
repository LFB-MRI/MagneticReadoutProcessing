from MRP import MRPHalSerialPortInformation, MRPHal, MRPHalLocal, MRPHalRest, MRPHalKlipper


class MRPHalHelperException(Exception):
    def __init__(self, message="MRPHalHelperException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPHalHelper:
    @staticmethod
    def createHalInstance(_port: MRPHalSerialPortInformation.MRPHalSerialPortInformation):

        if not _port.is_valid():
            raise MRPHalHelperException("invalid sensor config, please re-run connect command")

        sensor_connection: MRPHal.MRPHal = None
        if _port.getSensorsNeededHalImplementation() == MRPHalSerialPortInformation.MRPHalType.MRPHalLocal:
            sensor_connection = MRPHalLocal.MRPHalLocal(_port)
        elif _port.getSensorsNeededHalImplementation() == MRPHalSerialPortInformation.MRPHalType.MRPHalRest:
            sensor_connection = MRPHalRest.MRPHalRest(_port)
        elif _port.getSensorsNeededHalImplementation() == MRPHalSerialPortInformation.MRPHalType.MRPHalKlipper:
            sensor_connection = MRPHalKlipper.MRPHalKlipper(_port)

        return sensor_connection