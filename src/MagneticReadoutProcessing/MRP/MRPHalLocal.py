""" class for interfacing (hardware, protocol) sensors running the UnifiedSensorFirmware """
import time
from enum import Enum

import requests
import serial
import serial.tools.list_ports
import re
import os
import io
from socket import *

from MRP import MRPHalSerialPortInformation, MRPHal
from MRP.MRPHalSerialPortInformation import MRPRemoteSensorType


class MRPHalLocalException(Exception):
    def __init__(self, message="MRPHalLocalException thrown"):
        self.message = message
        super().__init__(self.message)



class MRPHalLocal:
    """
    Baseclass for hardware sensor interaction using a serial interface.
    It contains functions to send rec commands from/to the sensor but no interpretation
    """

    TERMINATION_CHARACTER = '\n'

    READLINE_TIMEOUT_MULTIPLIER: int = 2
    READLINE_TIMEOUT: float = 0.1 * READLINE_TIMEOUT_MULTIPLIER
    READLINE_RETRY_ATTEMPT: int = 20

    current_port: MRPHalSerialPortInformation = None
    serial_port_instance: serial = None
    sio: io.TextIOWrapper = None


    def __init__(self, _selected_port: MRPHalSerialPortInformation, _type: MRPHalSerialPortInformation.MRPRemoteSensorType = MRPHalSerialPortInformation.MRPRemoteSensorType.BaseSensor):
        if _selected_port:
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
            raise MRPHalLocalException("set serial port information are invalid")
        self.current_port = _port

    def get_serial_port_information(self) ->MRPHalSerialPortInformation:
        return self.current_port

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
            raise MRPHalLocalException("set serial port information are invalid")

        # HANDLE SPECIAL SENSORS

        # IF A REMOTE SENSOR IS USED MROHalRest should be used
        if self.current_port.getSensorsNeededImplementation() == MRPRemoteSensorType.ApiSensor:
            raise MRPHalLocalException("remote sensor please use instance of MRPHalRest")

        dpath: str = self.current_port.device_path
        if self.current_port.is_remote_port():
            if dpath.startswith("tcp://"):
                dpath = dpath.replace('tcp://', 'socket://')
            elif dpath.startswith("udp://"):
                dpath = dpath.replace('udp://', 'socket://')

        # CREATE AND OEPN serial INSTANCE
        if self.serial_port_instance is None or self.current_port.is_remote_port():
            try:
                # call opens directly
                # if baudrate is 0 => tcp is used

                if self.current_port.is_remote_port():
                    self.serial_port_instance = serial.serial_for_url(dpath, timeout=1)
                else:
                    self.serial_port_instance = serial.Serial(port=self.current_port.device_path, baudrate=self.current_port.baudrate)
                # FURTHER CONFIGURATION
                self.serial_port_instance.rtscts = True
                self.serial_port_instance.dsrdtr = True
                self.serial_port_instance.timeout = self.READLINE_TIMEOUT

                # CREATE A BUFFERED READ/WRITE INSTANCE TO HANDlE send/rec over the port
                self.sio = io.TextIOWrapper(io.BufferedRWPair(self.serial_port_instance, self.serial_port_instance))
            except Exception as e: # remap exception ugly i know:)
                raise MRPHalLocalException(str(e))
        else:
            self.serial_port_instance.baudrate = self.current_port.baudrate
            self.serial_port_instance.port = self.current_port.device_path
            # OPEN
            try:
                self.serial_port_instance.open()
            except Exception as e: # remap exception ugly i know:)
                raise MRPHalLocalException(str(e))

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
        disconnects a opened serial port
        """
        if self.is_connected():
            self.serial_port_instance.close()

    def read_value(self):
        if not self.is_connected():
            raise MRPHalLocalException("sensor isn't connected. use connect() first")

    def send_command(self, _cmd: str) -> [str]:
        """
        sends a command to the sensor

        :param _cmd: command like help id read...
        :type _cmd: str

        :returns: returns sensor response as line separated by '\n'
        :rtype: [str]
        """
        if _cmd is None or len(_cmd) <= 0:
            raise MRPHalLocalException("_cmd is empty")

        if not self.is_connected():
            raise MRPHalLocalException("sensor isn't connected. use connect() first")

        # end eof character
        if self.TERMINATION_CHARACTER not in _cmd:
            _cmd = _cmd + self.TERMINATION_CHARACTER

        # send cmd
        self.sio.write(_cmd)
        # send data directly to avoid timeout issues on readline
        self.sio.flush()

        # wait for response
        result: str = ""
        for i in range(max(self.READLINE_RETRY_ATTEMPT, 1)):
            result = self.sio.readline()
            if len(result) > 1: # read more than '\n'
                break

        # REPLACE WINDOW NEWLINE CHARS
        result = result.strip('\r')

        # remove last termination character
        result = ''.join(result.rsplit('\n', 1))


        if 'parse error' in result:
                return []

        if self.TERMINATION_CHARACTER in result:
            return result.split(self.TERMINATION_CHARACTER).remove('')



        return [result]
    def query_command_str(self, _cmd: str) -> str:
        """
        queries a sensor command and returns the response as string

        :param _cmd: command like help id read...
        :type _cmd: str

        :returns: returns the response as concat string
        :rtype: str
        """
        res: [str] = self.send_command(_cmd)

        if len(res) <= 0:
            return ""

        if 'parse error' in res[0]:
            raise MRPHalLocalException("sensor returned invalid command or command not implemented for {}".format(_cmd))

        return "".join(str(e) for e in res)
    def query_command_int(self, _cmd: str) -> int:
        """
        queries a sensor command and returns the response as int

        :param _cmd: command like help id read...
        :type _cmd: str

        :returns: returns the as int parsed result
        :rtype: int
        """
        res = self.query_command_str(_cmd)
        if len(res) > 0:
            if '0x' in res:
                return int(res, base=16)
            return int(res)
        print(res)
        raise MRPHalLocalException("cant parse result {} for query {} into int".format(res, _cmd))

    def query_command_float(self, _cmd: str) -> float:
        """
        queries a sensor command and returns the response as float

        :param _cmd: command like help id read...
        :type _cmd: str

        :returns: returns the as float parsed result
        :rtype: float
        """
        for i in range(10):
            res = self.query_command_str(_cmd)
            if len(res) > 0:
                return float(res)
            print(res)
        raise MRPHalLocalException("cant parse result {} for query {} into float".format(res, _cmd))

    def get_sensor_id(self) -> str:
        """
        returns the sensors id

        :returns: id as string default unknown
        :rtype: str
        """
        res = self.query_command_str('id')
        if len(res) > 0:
            return res
        return "unknown"

    def get_sensor_count(self) -> int:
        """
        returns the connected sensors relevant for chained sensors

       :returns: sensor count
       :rtype: str
       """
        try:
            return self.query_command_int('sensorcnt')
        except MRPHalLocalException as e:
            return 0

    def get_sensor_names(self) -> [str]:
        """
        returns the sensor names defined in the sensor firmware as string list

        :returns: capabilities e.g. static, axis_x,..
        :rtype: [str]
        """
        try:
            res: str = self.query_command_str('sid')
            res = res.replace(" ", "")

            if ',' in res:
                return res.split(',')
            return res
        except MRPHalLocalException as e:
            return []

    def get_sensor_capabilities(self) -> [str]:
        """
        returns the sensor capabilities defined in the sensor firmware as string list

        :returns: capabilities e.g. static, axis_x,..
        :rtype: [str]
        """
        try:
            res: str = self.query_command_str('info')
            res = res.replace(" ", "")

            if ',' in res:
                return res.split(',')
            return res
        except MRPHalLocalException as e:
            return []

    def get_sensor_commandlist(self) -> [str]:
        try:
            res: str = self.query_command_str('commands')
            res = res.replace(" ", "")

            if len(res) <= 0:
                return []


            if ',' in res:
                return res.split(',')
            return [res]
        except MRPHalLocalException as e:
            print(str(e))
            return []


        return ret









