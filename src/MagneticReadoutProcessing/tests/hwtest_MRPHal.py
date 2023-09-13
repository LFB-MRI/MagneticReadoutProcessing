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
        self.DEVICE_SERIAl_PORT = "/dev/tty.usbmodem3867315334391"
        self.hal_instance = MRPHal.MRPPHal()
    def test_connection(self):
        ports = MRPHal.MRPPHal.list_serial_ports()

        i = 0

    def test_sensor_readout(self):
        pass








if __name__ == '__main__':
    unittest.main()