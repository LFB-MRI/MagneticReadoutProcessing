""" base class to query (b-value and temp) values from a hardware sensor running the UnifiedSensorFirmware """
import MRP
from MRP import MRPHalLocal, MRPHalRest


class MMRPBaseSensorException(Exception):
    def __init__(self, message="MMRPBaseSensorException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPRotationalSensor:
    """ Baseclass for the full sphere sensor with dynamic and axis_b capabilities """

    sensor_connection: MRPHalRest.MRPPHalRest = None


    def __init__(self, _sensor_connection: MRPHalRest.MRPHalRest):
        if not _sensor_connection.is_connected():
            raise MMRPBaseSensorException("sensor is not connected please use _sensor_connection.connect() first")

        self.sensor_connection = _sensor_connection

    def query_readout(self):
        """
        queries a complete readout of all connected sensors and their axis
        """
        # TODO MOVE TO POSITION AND QUERy all axis information
        #for sensor_id in range(0,self.sensor_count):
        #    for axis in self.sensor_axis:
        #        self.readout_result[sensor_id][axis] = self.sensor_connection.query_command_float("readsensor {} {}".format(axis, sensor_id))



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
