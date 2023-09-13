import serial
import serial.tools.list_ports
from enum import Enum
import re
import os
from pathlib import Path
import MRPReading, MRPMeasurementConfig


class MRPHalException(Exception):
    def __init__(self, message="MRPHalException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPHalSerialPortInformation():
    """
    A little helper-class to store name and serial port device path
    """
    name: str = "Unknown"
    device_path: str = ""
    baudrate = 115200

    def __init__(self, _path: str, _name: str = "Unified Sensor", _baudrate: int = 115200):
        """
        contructor to save some information about the serial port

        :param _path: filesystem serial port path such e.g. /dev/ttyUSB0
        :type _path: str

        :param _name: human readable name
        :type _name: str

        :param _baud: baudrate such as 9600 115200 (default 115200 for UnifiedSensorBaudrate)
        :type _baud: int
        """
        self.name = _name
        self.device_path = _path

        if _baudrate > 0:
            self.baudrate = _baudrate

    def is_valid(self) -> bool:
        """
        check if the _path exist in the filesystem

        :returns: returns true if the path is valid (path exists)
        :rtype: bool
        """
        if self.device_path is None or len(self.device_path) <= 0:
            return False

        if 'socket://' in self.device_path or 'tcp://' in self.device_path or 'udp://' in self.device_path:
            return True
        elif os.path.exists(self.device_path): # os.path.exists is needed for fs access pathlib is not working for /dev on mac
            return True
        return False



class MRPHalSensorState:
    pass


class MRPPHal:
    """
    Baseclass for hardware sensor interaction
    """

    @staticmethod
    def check_serial_number(_serial_number: str) -> bool:
        """
        This function is implements a simple lookup table to check for connected sensor using the vid:pid or usb serial number.
        Its just a precheck to indicate a possible connected sensor to the user.
        Add your own sensor ids into the SERIAL_LUT variable

        :param _serial_number: given usb serial number
        :type _serial_number: str

        :returns: true if serial number is a valid sensor
        :rtype: bool
        """

        SERIAL_LUT = {
            '386731533439'  # FIRST EVER BUILD SENSOR :)
            '0483:5740'     # USB VID:PID IS WORKING TOO
        }

        if len(_serial_number) < 0:
            raise MRPHalException("MRPHalSensorType from_serial_number _serial_number is empty")

        if _serial_number in SERIAL_LUT:
            return True
        return False

    @staticmethod
    def list_serial_ports(_filter_devicepath: str = ".+", _blacklist_devicepath: [str] = ['/dev/cu.Bluetooth-Incoming-Port', '/dev/cu.HKAuraBT']) -> [MRPHalSerialPortInformation]:
        """
        Returns all found serial ports on the system
        The function returns the max value of (x,y,z) or (d,h)

        :param _filter_devicepath: regex filter for filtering device paths e.g. /dev/tty*
        :type _filter_devicepath: str

        :param _blacklist_devicepath: blacklist specified device paths e.g. bluetooth port on Mac systems '/dev/cu.Bluetooth-Incoming-Port'
        :type _blacklist_devicepath: [str]

        :returns: returns a list of MRPHalSerialPortInformation instance with serial port name and device path
        :rtype: [MRPHalSerialPortInformation]
        """

        # DEFAULT ALLOW ANY PORT
        if _filter_devicepath is None:
            _filter = ".+"

        # GET SYSTEM PORT
        ports = serial.tools.list_ports.comports(include_links=True)
        # RESULT LIST
        valid_ports: [MRPHalSerialPortInformation] = []

        # ITERATE OVER PORTS AND FILTER
        for port in ports:
            # SKIP BLACKLISTED DEVICE PATHS
            if port.device in _blacklist_devicepath:
                continue

            # SKIP REGEX FILTERED
            try:
                x = re.search(_filter_devicepath, str(port.device))
                if not x:
                    continue
            except Exception as e:
                continue

            # IF SERIAL NUMBER REGISTERED SHOW IT AS SENSOR
            if port.serial_number is not None and len(port.serial_number) > 0:
                if MRPPHal.check_serial_number(port.serial_number):
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unified Sensor {}".format(port.serial_number)))
                else:
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unknown Sensor {}".format(port.serial_number)))
            elif port.pid is not None and port.vid is not None:
                combined = "{}:{}".format(port.pid, port.vid)
                if MRPPHal.check_serial_number(port.serial_number):
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unified Sensor {}".format(combined)))
                else:
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unknown Sensor {}".format(port.serial_number)))
            else:
                if port.name is not None and len(port.name) > 0:
                    valid_ports.append(MRPHalSerialPortInformation(port.device, port.name))
                else:
                    valid_ports.append(MRPHalSerialPortInformation(port.device, port.device))

        return valid_ports


    current_port: MRPHalSerialPortInformation = None
    serial_port_instance: serial = None

    def __init__(self, _selected_port: MRPHalSerialPortInformation):
        self.current_port = _selected_port



    def __del__(self):
        self.disconnect()

    def set_serial_port_information(self, _port: MRPHalSerialPortInformation):
        """
       set the serial port information = which serial port to connect to if the connect() function is called

       :param _port: serial port information
       :type _port: MRPHalSerialPortInformation
       """
        if self.current_port is None or not self.current_port.is_valid():
            raise MRPHalException("set serial port information are invalid")
        self.current_port = _port


    def connect(self) -> bool:
        """
        connect to the selected serial port

        :returns: returns true if a serial connection was made
        :rtype: bool
        """

        # DISCONNECT FIRST
        if self.is_connected():
            self.disconnect()

        # CHECK PORT FILE EXISTS
        if self.current_port is None or not self.current_port.is_valid():
            raise MRPHalException("set serial port information are invalid")

        # CREATE serial INSTANCE
        if self.serial_port_instance is None:
            self.serial_port_instance = serial.Serial(port=self.current_port.device_path, baudrate=self.current_port.baudrate)
        else:
            self.serial_port_instance.baudrate = self.DEFAULT_BAUDRATE
            self.serial_port_instance.port = self.current_port.device_path

        # TRY TO OPEN
        try:
            self.serial_port_instance.open()
        except Exception as e: # remap exception ugly i know:)
            raise MRPHalException(str(e))



        return self.serial_port_instance.isOpen()
    def is_connected(self) -> bool:
        """
        returns true if the serial port is open

        :returns: returns true if a serial connection is open
        :rtype: bool
        """
        if self.serial_port_instance is not None and self.serial_port_instance.is_open:
            return True
        return False


    def disconnect(self):
        """
        disconnects a may opened serial port
        """
        if self.is_connected():
            self.serial_port_instance.close()


    def read_value(self):
        if self.is_connected():
            raise MRPHalException("sensor isn't connected. use connect() first")


    def read_sensor_capabilities(self):

        commands_to_request = [
            'version', 'id', 'senorcount'
        ]


