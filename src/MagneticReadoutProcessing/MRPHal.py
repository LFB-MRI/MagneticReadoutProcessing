import serial
import serial.tools.list_ports

import MRPReading, MRPMeasurementConfig


class MRPHalException(Exception):
    def __init__(self, message="MRPHalException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPPHal:
    """Baseclass for hardware sensor interaction"""

    @staticmethod
    def list_serial_ports():
        ports = serial.tools.list_ports.comports(include_links=False)



    def connect(self):
        pass
        # open serial port
        # check version
        # check id

    def read_value(self):
        pass
        # AXIS
    def read_sensor_capabilities(self):


        commands_to_request = [
            'version', 'id', 'senorcount'
        ]
    def __init__(self):
        pass