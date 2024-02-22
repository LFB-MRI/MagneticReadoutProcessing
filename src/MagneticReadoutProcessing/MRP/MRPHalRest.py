""" class for interfacing (hardware, protocol) sensors running the UnifiedSensorFirmware """
import time
from enum import Enum

import re
import os
import io
from socket import *
import requests

from MRP import MRPPHalRestRequestResponseState, MRPHal
from MRP import MRPHalSerialPortInformation



class MRPHalRestException(Exception):
    def __init__(self, message="MRPHalRestException thrown"):
        self.message = message
        super().__init__(self.message)



class MRPHalRest(MRPHal.MRPHal):
    """
    Baseclass for hardware sensor interaction using a serial interface.
    It contains functions to send rec commands from/to the sensor but no interpretation
    """

    PROXY_URL_PATH_PREFIX = "proxy/" # SEE MRPProxy flask paths 127.0.0.1/proxy/<cmd>

    current_port: MRPHalSerialPortInformation.MRPHalSerialPortInformation = None


    def __init__(self, _selected_port: MRPHalSerialPortInformation, _type: MRPHalSerialPortInformation.MRPRemoteSensorType = MRPHalSerialPortInformation.MRPRemoteSensorType.ApiSensor):
        self.set_serial_port_information(_selected_port)

    def __del__(self):
        self.disconnect()


    def set_serial_port_information(self, _port: MRPHalSerialPortInformation):
        """
       set the serial port information = which serial port to connect to if the connect() function is called

       :param _port: serial port information
       :type _port: MRPHalSerialPortInformation
       """
        if _port is None or not _port.is_valid():
            raise MRPHalRestException("set serial port information are invalid")

        if _port.getSensorsNeededImplementation() != MRPHalSerialPortInformation.MRPRemoteSensorType.ApiSensor:
            raise MRPHalRestException("set serial port is not valid for this hal implementation")

        if not _port.device_path.startswith('http://') and not _port.device_path.startswith('https://'):
            raise MRPHalRestException("set serial port information device path didnt start with http:// or https:/")

        if not _port.device_path.endswith('/'):
            _port.device_path = _port.device_path + '/'

        if not _port.device_path.endswith(self.PROXY_URL_PATH_PREFIX):
            _port.device_path = _port.device_path + self.PROXY_URL_PATH_PREFIX

        print("set_serial_port_information: modified device path {}".format(_port.device_path))
        self.current_port = _port

    def get_serial_port_information(self) ->MRPHalSerialPortInformation:
        return self.current_port
    def request_json(self, _command: str, _request_timeout=300):
        if _command is None or not _command:
            raise MRPHalRestException("request_json _command parameter is empty")

        if not self.current_port.is_valid() or not self.current_port.is_remote_port():
            raise MRPHalRestException("port is invalid or no remote port: {}".format(self.current_port.device_path))

        #spres = self.current_port.device_path.split(":")
        #if len(spres) <= 0:
        #    raise MRPHalRestException("request_json replacement failed: {}".format(spres))

        # replace apisensor://192.168.178.1:5055 or rotationsensor://192.168.178.1:5055  with http://192.168.178.1:5055
        #spres[0] = "http"
        #url = "".join(spres)
        dtype = self.current_port.getSensorsNeededImplementation().value
        url = "{}command?cmd={}&devicetype={}".format(self.current_port.device_path, _command, int(dtype))

        #

        r = requests.get(url=url, allow_redirects=True, timeout=_request_timeout)

        if r.status_code >= 200 and r.status_code < 300:
            # TRY TO GET SENSOR IMPLEMENTATION
            if 'application/json' in r.headers['content-type']:
                try:
                    doc = r.json()
                    return doc
                except Exception as e:
                    raise MRPHalRestException("request_json {}".format(str(e)))
            else:
                raise MRPHalRestException("application/json required: {}".format(r.headers))
        else:
            raise MRPHalRestException("request_json r.status_code >= 200 and r.status_code < 400")

    def request_status(self) -> MRPPHalRestRequestResponseState:
        r: MRPPHalRestRequestResponseState = MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState()
        try:
            # TODO IMPLEMENT CUSTOM JSON PARSER
            ret: dict = self.request_json('status')
            r.sensortype = ret['sensortype']
            r.version = ret['version']
            r.id = ret['id']
            #r.sensorcount = ret['sensorcount']
            r.capabilities = ret['capabilities']
            r.initialized = ret['initialized']
            r.commands = ret['commands']
            r.success = True
            return r

        except Exception as e:
            print(str(e))
            r.success = False
        return r

    def connect(self) -> bool:
        """
        connect to the selected api

        :returns: returns true if an api connection was tested
        :rtype: bool
        """
        c = self.request_status()

        if c is None:
            return False
        return c.success

    def is_connected(self) -> bool:
        """
        returns true if the serial port is open

        :returns: returns true if a serial connection is open
        :rtype: bool
        """
        rt: MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState = self.request_status()
        return (rt.success and rt.initialized)

    def disconnect(self):
        """
        disconnects a opened sensor connection
        """
        return True

    def read_value(self):
        if not self.is_connected():
            raise MRPHalRestException("sensor isn't connected. use connect() first")

    def send_command(self, _cmd: str) -> [str]:
        """
        sends a command to the sensor

        :param _cmd: command like help id read...
        :type _cmd: str

        :returns: returns sensor response as line separated by '\n'
        :rtype: [str]
        """
        if _cmd is None or len(_cmd) <= 0:
            raise MRPHalRestException("_cmd is empty")

        if not self.is_connected():
            raise MRPHalRestException("sensor isn't connected. use connect() first")



        out: dict = self.request_json(_cmd)

        if 'output' in out and len(out['output']):
            return out['output']

        return []
        # TODO get output lines from dicts
    def query_command_str(self,_cmd: str) -> str:
        """
        queries a sensor command and returns the response as string

        :param _cmd: command like help id read...
        :type _cmd: str

        :returns: returns the response as concat string
        :rtype: str
        """
        res = self.send_command(_cmd)
        if 'parse error' in res:
            raise MRPHalRestException("sensor returned invalid command or command not implemented for {}".format(_cmd))

        return "".join(str(e) for e in res)

    def query_command_float(self, _cmd: str) -> float:
        """
        queries a sensor command and returns the response as float

        :param _cmd: command like help id read...
        :type _cmd: str

        :returns: returns the as float parsed result
        :rtype: float
        """
        res = self.query_command_str(_cmd)
        if len(res) > 0:
            return float(res)
        raise MRPHalRestException("cant parse result {} for query {} into int".format(res, _cmd))
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
        raise MRPHalRestException("cant parse result {} for query {} into int".format(res, _cmd))

    def get_sensor_id(self) -> str:
        """
        returns the sensors id

        :returns: id as string default unknown
        :rtype: str
        """
        r: MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState = self.request_status()

        if r.success:
            return r.id
        else:
            return ""

    def get_sensor_count(self) -> int:
        """
        returns the connected sensors relevant for chained sensors

       :returns: sensor count
       :rtype: str
       """
        try:
            return self.query_command_int('combinedsensorcnt')
        except Exception as e:
            return 0

    def get_sensor_names(self) -> [str]:
        r: MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState = self.request_status()
        if r.success:
            return r.sensornames
        else:
            return []

    def get_sensor_capabilities(self) -> [str]:
        """
        returns the sensor capabilities defined in the sensor firmware as string list

        :returns: capabilities e.g. static, axis_x,..
        :rtype: [str]
        """
        r: MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState = self.request_status()
        if r.success:
            return r.capabilities
        else:
            return []

    def get_sensor_commandlist(self) -> [str]:
        r: MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState = self.request_status()
        if r.success:
            return r.commands
        else:
            return []