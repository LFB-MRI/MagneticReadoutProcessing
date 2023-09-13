from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np


import MRPHal

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
        port = MRPHal.MRPHalSerialPortInformation(_path="/dev/42")
        hal_instance = MRPHal.MRPPHal(port)
        with self.assertRaises(MRPHal.MRPHalException):
            hal_instance.connect()

    def test_connect_failed(self):
        port = MRPHal.MRPHalSerialPortInformation(_path=self.DEVICE_SERIAl_PORT)
        hal_instance = MRPHal.MRPPHal(port)
        with self.assertRaises(MRPHal.MRPHalException):
            hal_instance.connect()

    def test_connect_ok(self):
        port = MRPHal.MRPHalSerialPortInformation(_path=self.DEVICE_SERIAl_PORT)
        hal_instance = MRPHal.MRPPHal(port)

        hal_instance.connect()


        hal_instance.disconnect()

    def test_sensor_connection(self):
        port = MRPHal.MRPHalSerialPortInformation(_path=self.DEVICE_SERIAl_PORT)
        hal_instance = MRPHal.MRPPHal(port)

        hal_instance.connect()




        hal_instance.disconnect()





    def test_sensor_readout(self):
        pass








if __name__ == '__main__':
    unittest.main()