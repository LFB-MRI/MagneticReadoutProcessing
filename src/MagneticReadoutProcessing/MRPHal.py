import serial

import MRPReading, MRPMeasurementConfig


class MRPHalException(Exception):
    def __init__(self, message="MRPHalException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPPHal:
    """Baseclass for hardware sensor interaction"""

    @staticmethod
    def list_serial_ports():
        pass


    def read_sensor_capabilities(self):


        commands_to_request = [
            'version', 'id', 'senorcount'
        ]
    def __init__(self):
        pass