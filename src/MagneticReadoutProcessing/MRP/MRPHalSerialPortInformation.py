import os
import re
import time
from _socket import SO_REUSEADDR, SO_BROADCAST
from enum import Enum
from socket import socket, AF_INET, SOCK_DGRAM
from ssl import SOL_SOCKET

import requests
import serial


class MRPHalSerialPortInformationException(Exception):
    def __init__(self, message="MRPHalSerialPortInformationException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPRemoteSensorType(Enum):
    Unknown = 0
    BaseSensor = 1
    ApiSensor = 2
    KlipperManipulator = 3 # FOR KLIPPER BASED MANIPULATORS

class MRPHalType(Enum):
    Unknown = 0
    MRPPHal = 1
    MRPHalLocal = 2
    MRPHalRest = 3
    MRPHalKlipper = 4


class MRPHalSerialPortInformation:
    """
    A little helper-class to store name and serial port device path
    """
    name: str = "Unknown"
    device_path: str = ""
    baudrate: int = 0
    target_sensor_implementation: MRPRemoteSensorType = MRPRemoteSensorType.Unknown

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

        SERIAL_LUT = [
            '386731533439'  # FIRST EVER BUILD SENSOR :)
            '00000000d0ad2036'  # FIRST ROTATIONAL SENSOR
            '230972496757412434',
            '601861E6227C4A4B'
            # '0483:5740'     # USB VID:PID IS WORKING TOO
        ]

        if len(_serial_number) < 0:
            raise MRPHalSerialPortInformationException("MRPHalSensorType from_serial_number _serial_number is empty")

        if _serial_number in SERIAL_LUT:
            return True
        return False


    @staticmethod
    def list_sensors() -> []:
        l: [MRPHalSerialPortInformation] = MRPHalSerialPortInformation.list_serial_ports()
        r: [MRPHalSerialPortInformation] = MRPHalSerialPortInformation.list_remote_serial_ports
        return l + r
    @staticmethod
    def list_remote_serial_ports() -> []:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        sock.settimeout(5)

        server_address = ('255.255.255.255', 9434)
        message = 'pfg_ip_broadcast_cl'

        # RESULT LIST
        valid_ports: [MRPHalSerialPortInformation] = []
        entry_list: [str] = []
        for i in range(1):
            # Send data
            sent = sock.sendto(message.encode(), server_address)
            try:
                data, server = sock.recvfrom(4096)
                data_str = data.decode('UTF-8')

                if 'pfgipresponseserv' in data_str:
                    if '_' in data_str:
                        sp: [str] = data_str.split('_')
                        host: str = server[0]
                        port: int = int(sp[1])
                        senid: str = "{}:{}".format(host, port)
                        if len(sp) >= 2:
                            senid = sp[2]

                        btype = "socket"
                        # DETECT USED SENSOR FOR AN API SENSORS WE TRY TO PING THE API
                        # IF an HTTP SERVER IS ON THE GOT PORT ITS AN REST API SENSOR
                        url = "http://{}:{}/status".format(host, port)
                        print("detecting remote sensor type using API endpoint: {}".format(url))
                        r = requests.get(url=url)
                        if r.status_code >= 200 and r.status_code < 400:
                            # TRY TO GET SENSOR IMPLEMENTATION
                            if 'application/json' in r.headers['content-type']:

                                try:
                                    doc = r.json()
                                    if 'sensortype' in doc:
                                        btype = str(doc['sensortype'])
                                except Exception as e:
                                    print("unknown remote sensor type: {}", r.json())
                                    btype = "unknown"

                        entry: MRPHalSerialPortInformation = MRPHalSerialPortInformation(
                            "{}://{}:{}".format(btype, host, port))
                        entry.name = "Unified Sensor {} [{}]".format(senid, btype)
                        if senid not in entry_list:
                            valid_ports.append(entry)
                            entry_list.append(senid)
            except Exception as e:
                pass
            time.sleep(0.1)

        return valid_ports

    @staticmethod
    def list_serial_ports(_filter_devicepath: str = ".+", _blacklist_devicepath: [str] = ['/dev/cu.Bluetooth-Incoming-Port']) -> []:
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

        DEFAULT_BAUDRATE: int = 115200
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
                if MRPHalSerialPortInformation.check_serial_number(port.serial_number):
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unified Sensor {}".format(port.serial_number),
                                                    _baudrate=DEFAULT_BAUDRATE))
                else:
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unknown Sensor {}".format(port.serial_number),
                                                    _baudrate=DEFAULT_BAUDRATE))
            elif port.pid is not None and port.vid is not None:
                combined = "{}:{}".format(port.pid, port.vid)
                if MRPHalSerialPortInformation.check_serial_number(port.serial_number):
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unified Sensor {}".format(combined),
                                                    _baudrate=DEFAULT_BAUDRATE))
                else:
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, "Unknown Sensor {}".format(port.serial_number),
                                                    _baudrate=DEFAULT_BAUDRATE))
            else:
                if port.name is not None and len(port.name) > 0:
                    valid_ports.append(MRPHalSerialPortInformation(port.device, port.name, _baudrate=DEFAULT_BAUDRATE))
                else:
                    valid_ports.append(
                        MRPHalSerialPortInformation(port.device, port.device, _baudrate=DEFAULT_BAUDRATE))

        return valid_ports






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

    def getSensorsNeededImplementation(self, _get_target_implementation: bool = False) -> MRPRemoteSensorType:

        if _get_target_implementation:
            return self.target_sensor_implementation


        if 'socket://' in self.device_path or 'tcp://' in self.device_path or 'udp://' in self.device_path:
            return MRPRemoteSensorType.BaseSensor
        elif 'loop://' in self.device_path:
            return MRPRemoteSensorType.BaseSensor
        elif 'http://' in self.device_path or 'https://' in self.device_path:
            return MRPRemoteSensorType.ApiSensor

        elif 'klipper://' in self.device_path or 'klippers://' in self.device_path:
            return MRPRemoteSensorType.KlipperManipulator

        return MRPRemoteSensorType.Unknown


    def setTargetSensorImplementation(self, _sti: MRPRemoteSensorType):
        self.target_sensor_implementation = _sti
    def getSensorsNeededHalImplementation(self) -> MRPHalType:

        if not self.is_valid():
            return MRPHalType.Unknown

        # HANDLE SPECIAL SENSORS
        if self.getSensorsNeededImplementation() == MRPRemoteSensorType.ApiSensor:
            return MRPHalType.MRPHalRest
        elif self.getSensorsNeededImplementation() == MRPRemoteSensorType.KlipperManipulator:
            return MRPHalType.MRPHalKlipper
        else:
            return MRPHalType.MRPHalLocal




    def is_remote_port(self) -> bool:
        if 'socket://' in self.device_path or 'tcp://' in self.device_path or 'udp://' in self.device_path:
            return True
        elif 'loop://' in self.device_path:
            return True
        elif 'http://' in self.device_path or 'https://' in self.device_path:
            return True
        elif 'klipper://' in self.device_path or 'klippers://' in self.device_path:
            return True
        return False


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
        elif 'loop://' in self.device_path:
            return True
        elif 'klipper://' in self.device_path or 'klippers://' in self.device_path:
            return True
        elif 'http://' in self.device_path or 'https://' in self.device_path:
            return True


        elif os.path.islink(self.device_path) or os.path.exists(self.device_path): # os.path.exists is needed for fs access pathlib is not working for /dev on mac
            if os.path.islink(self.device_path):
                # resolve symvlink
                self.device_path =  os.path.realpath(self.device_path)
            if self.baudrate is None or self.baudrate not in serial.SerialBase.BAUDRATES:
                return False

            return True
        return False