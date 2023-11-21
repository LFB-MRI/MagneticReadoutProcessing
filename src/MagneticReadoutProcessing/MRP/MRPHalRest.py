""" class for interfacing (hardware, protocol) sensors running the UnifiedSensorFirmware """
import time
from enum import Enum

import re
import os
import io
from socket import *

import requests

import MRP
from MRP import MRPPHalRestRequestResponseState
from MRP.MRPHal import MRPHalSerialPortInformation


class MRPHalRestException(Exception):
    def __init__(self, message="MRPHalRestException thrown"):
        self.message = message
        super().__init__(self.message)






class MRPPHalRest(MRP.MRPHal):
    """
    Baseclass for hardware sensor interaction using a serial interface.
    It contains functions to send rec commands from/to the sensor but no interpretation
    """

    TERMINATION_CHARACTER = '\n'
    READLINE_TIMEOUT = 0.1
    READLINE_RETRY_ATTEMPT = 5

    current_port: MRPHalSerialPortInformation = None

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
            raise MRPHalRestException("set serial port information are invalid")
        self.current_port = _port

    def request_json(self, _command: str):
        if _command is None or not _command:
            raise MRPHalRestException("request_json _command parameter is empty")

        spres = self.current_port.device_path.split(":")
        if len(spres) <= 0:
            raise MRPHalRestException("request_json replacement failed: {}".format(spres))

        # replace apisensor://192.168.178.1:5055 or rotationsensor://192.168.178.1:5055  with http://192.168.178.1:5055
        spres[0] = "http"
        url = "".join(spres)
        url = "{}/{}".format(url, _command)

        print("request_json: {}".format(url))

        r = requests.get(url=url, allow_redirects=True)

        if r.status_code >= 200 and r.status_code < 200:
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
            ret: dict = self.request_json('status')
            r.sensortype = ret['sensortype']
            r.version = ret['version']
            r.id = ret['id']
            r.sensorcount = ret['sensorcount']
            return r

        except Exception as e:
            r.success = False

    def connect(self) -> bool:
        """
        connect to the selected api

        :returns: returns true if an api connection was tested
        :rtype: bool
        """

        if not self.request_status().initialized:
            self.initialize()

        return self.request_status().success

    def initialize(self):
        ret: dict = self.request_json('initialize')

    def is_connected(self) -> bool:
        """
        returns true if the serial port is open

        :returns: returns true if a serial connection is open
        :rtype: bool
        """
        return self.request_status().success

    def disconnect(self):
        """
        disconnects a opened sensor connection
        """
        return True

    def get_sensor_id(self) -> str:
        """
        returns the sensors id

        :returns: id as string default unknown
        :rtype: str
        """
        r: MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState =  self.request_status()

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
        r: MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState = self.request_status()
        if r.success:
            return r.sensorcount
        else:
            return 0


    def get_sensor_capabilities(self) -> [str]:
        """
        returns the sensor capabilities defined in the sensor firmware as string list

        :returns: capabilities e.g. static, axis_x,..
        :rtype: [str]
        """
        try:
            res: str = self.query_command_str('info')

            if ' ' in res:
                res = res.strip(' ')

            if ',' in res:
                return res.split(',')
            return res
        except MRPHalRestException as e:
            return []
