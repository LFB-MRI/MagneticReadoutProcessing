from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np


from MRP import MRPHal

class TestMPRHal(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:

        # for testing this need to be set to a valid system port
        self.DEVICE_SERIAl_PORT = "/dev/tty.usbmodem3867315334391"
    def test_list_serial_ports(self):
        ports = MRPHal.MRPPHal.list_serial_ports()
        self.assertNotEqual(len(ports), 0)


    def test_connect_failed(self):
        port = MRPHal.MRPHalSerialPortInformation(_path="/dev/zero")
        hal_instance = MRPHal.MRPPHal(port)
        with self.assertRaises(MRPHal.MRPHalException):
            hal_instance.connect()

    def test_connect_ok(self):
        port = MRPHal.MRPHalSerialPortInformation(_path="loop://")
        hal_instance = MRPHal.MRPPHal(port)
        with self.assertRaises(MRPHal.MRPHalException):
            hal_instance.connect()

    def test_send_command(self):
        # GET A UNIFIED SENSOR
        ports: [MRPHal.MRPHalSerialPortInformation] = MRPHal.MRPPHal.list_serial_ports()
        selected_port:MRPHal.MRPHalSerialPortInformation = None
        for port in ports:
            if 'Unified Sensor' in port.name:
                selected_port = port
                print(port)
        # CONNECT
        hal_instance: MRPHal.MRPPHal = MRPHal.MRPPHal(selected_port)
        hal_instance.connect()

        # SEND A COMMAND
        ret: str = hal_instance.send_command("version")

        # DISCONNECT
        hal_instance.disconnect()

        # CHECK RESULT
        self.assertIsNotNone(ret)
        self.assertTrue(len(ret) > 0)

        self.assertRegex(ret, "v[0-9]+.[0-9]+.[0-9]+")


    def test_sensor_capabilities(self):
        # GET A UNIFIED SENSOR
        ports: [MRPHal.MRPHalSerialPortInformation] = MRPHal.MRPPHal.list_serial_ports()
        selected_port:MRPHal.MRPHalSerialPortInformation = None
        for port in ports:
            if 'Unified Sensor' in port.name:
                selected_port = port
                print(port)
        # CONNECT
        hal_instance: MRPHal.MRPPHal = MRPHal.MRPPHal(selected_port)
        hal_instance.connect()

        # TRy to read basic commands
        cap = hal_instance.get_sensor_capabilities()
        id = hal_instance.get_sensor_id()
        sc = hal_instance.get_sensor_count()



if __name__ == '__main__':
    unittest.main()