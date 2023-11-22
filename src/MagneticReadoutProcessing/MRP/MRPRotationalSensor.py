""" base class to query (b-value and temp) values from a hardware sensor running the UnifiedSensorFirmware """
from MRP import MRPHal, MRPBaseSensor


class MMRPBaseSensorException(Exception):
    def __init__(self, message="MMRPBaseSensorException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPRotationalSensor:
    """ Baseclass for the full sphere sensor with dynamic and axis_b capabilities """

    sensor_connection: MRPHal.MRPHal = None
    manipolator_connection: MRPHal.MRPHal = None

    sensor: MRPBaseSensor.MRPBaseSensor = None

    def __init__(self, _sensor_connection: MRPHal.MRPHal, _manipolator_connection: MRPHal.MRPHal):
        if not _sensor_connection.is_connected():
            raise MMRPBaseSensorException("sensor is not connected please use _sensor_connection.connect() first")

        if not _manipolator_connection.is_connected():
            raise MMRPBaseSensorException("sensor is not connected please use _manipolator_connection.connect() first")



        self.sensor_connection = _sensor_connection
        self.manipolator_connection = _manipolator_connection

        self.sensor = MRPBaseSensor.MRPBaseSensor(self.sensor_connection)


    def configure_reading(self, _averaging_points: int = 10):
        pass





