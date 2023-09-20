""" base class to query (b-value and temp) values from a hardware sensor running the UnifiedSensorFirmware """
from MRP import MRPHal


class MMRPBaseSensorException(Exception):
    def __init__(self, message="MMRPBaseSensorException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPBaseSensor(Exception):
    """ Baseclass for the simplest sensor with static and axis_b capabilities """

    sensor_connection: MRPHal.MRPPHal = None
    readout_result: dict = {}
    capabilities: list[str] = []
    sensor_axis: list = []
    sensor_count: int = 0
    def __init__(self, _sensor_connection: MRPHal.MRPPHal):
        if not _sensor_connection.is_connected():
            raise MMRPBaseSensorException("sensor is not connected please use _sensor_connection.connect() first")

        # CHECK CONNECTED SENSORS
        self.sensor_count = _sensor_connection.get_sensor_count()
        if self.sensor_count <= 0:
            raise MMRPBaseSensorException("connected sensor board has no connected sensors")

        # CHECK REQUIRED CAPS
        self.capabilities = _sensor_connection.get_sensor_capabilities()
        if 'static' not in self.capabilities:
            raise MMRPBaseSensorException("sensor capabilities list does not includes static so MRPBaseSensor is not the right interface for this sensor")

        # EXTRACT sensor AXIS
        for cap in self.capabilities:
            if 'axis_' in cap:
                self.sensor_axis.append(cap.split('_')[1])

        if len(self.sensor_axis) <= 0:
            raise MMRPBaseSensorException("sensor capabilities has no axis to readout such as axis_b axis_x")


        # POPULATE RESULT DICT
        for sc in range(self.sensor_count):
            self.readout_result[sc] = {}
            for axis in self.sensor_axis:
                self.readout_result[sc][axis] = 0.0


        self.sensor_connection = _sensor_connection

    def query_readout(self):
        """
        queries a complete readout of all connected sensors and their axis
        """
        for sensor_id in range(0,self.sensor_count):
            for axis in self.sensor_axis:
                self.readout_result[sensor_id][axis] = self.sensor_connection.query_command_float("readsensor {} {}".format(axis, sensor_id))


    def get_reading(self, _axis:str = 'b', _sensor_id: int = 0) -> float:
        if _sensor_id > self.sensor_count:
            raise MMRPBaseSensorException("given _sensor_id is out of range (max:{})".format(self.sensor_count))

        if _axis not in self.sensor_axis:
            raise MMRPBaseSensorException("sensor does not implement this axis {}".format(_axis))

        return self.readout_result[_sensor_id][_axis]

    def get_temp(self, _sensor_id: int = 0) -> float:
        """
        returns the sensors temperature
        trigger a readout first using the query_readout function

        :param _sensor_id: get b axis from specified sensor_id in range from 0 to self.sensor_count
        :type _sensor_id: int

        :returns: returns the temperature if not able to read temperature the result will be -254.0
        :rtype: float
        """

        if 'temp' in self.sensor_axis:
            return self.get_reading('temp', _sensor_id)
        return -254.0

    def get_b(self, _sensor_id: int = 0) -> float:
        """
        returns the b field value for a given sensor id
        trigger a readout first using the query_readout function
        if the sensor has z measurement capabilities, this axis will be used to read out the measurement prefix sign

        :param _sensor_id: get b axis from specified sensor_id in range from 0 to self.sensor_count
        :type _sensor_id: int

        :returns: returns the latest b field value
        :rtype: float
        """
        b = self.get_reading('b', _sensor_id)
        # if the sensor has z measurement capabilities
        # use z to correct the reading sign +/-
        if 'z' in self.sensor_axis:
            z = self.get_reading('z', _sensor_id)
            if z < 0.0:
                b = b * (-1.0)
        return b

    def get_vector(self, _sensor_id: int = 0) -> (float, float, float):
        """
        returns the x,y,z vector from 3D magnetometer sensors value for a given sensor id
        trigger a readout first using the query_readout function

        :param _sensor_id: get b axis from specified sensor_id in range from 0 to self.sensor_count
        :type _sensor_id: int

        :returns: returns the latest (x, y, z) field value
        :rtype: (float, float, float)
        """

        return (self.get_reading('x', _sensor_id), self.get_reading('y', _sensor_id), self.get_reading('z', _sensor_id))
