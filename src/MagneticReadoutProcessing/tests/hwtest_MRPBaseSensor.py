from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np

import MRPHal
import MRPBaseSensor

class TestMPRHal(unittest.TestCase):
    hal_instance: MRPHal.MRPPHal = None
    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:

        # for testing this need to be set to a valid system port
        self.DEVICE_SERIAl_PORT = "/dev/tty.usbmodem3867315334391"
        # GET A UNIFIED SENSOR
        ports: [MRPHal.MRPHalSerialPortInformation] = MRPHal.MRPPHal.list_serial_ports()
        selected_port: MRPHal.MRPHalSerialPortInformation = None
        for port in ports:
            if 'Unified Sensor' in port.name:
                selected_port = port
                print(port)
        # CONNECT
        self.hal_instance: MRPHal.MRPPHal = MRPHal.MRPPHal(selected_port)
        self.hal_instance.connect()

    def tearDown(self) -> None:
        if self.hal_instance is not None:
            self.hal_instance.disconnect()
    def test_basesensor_readout_b(self):

        self.assertIsNotNone(self.hal_instance)
        basesensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(self.hal_instance)
        self.assertIsNotNone(basesensor)

        basesensor.query_readout()

        self.assertIsNotNone(basesensor.get_b())





if __name__ == '__main__':
    unittest.main()