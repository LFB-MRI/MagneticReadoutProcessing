from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np

from MRP import MRPHal, MRPBaseSensor, MRPDataVisualization, MRPReading, MRPReadingEntry


class TestMPRHal(unittest.TestCase):
    hal_instance: MRPHal.MRPPHal = None
    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:

        # TMP FOLDER FOR GRAPH EXPORTS
        self.import_export_test_folderpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(self.import_export_test_folderpath):
            os.makedirs(self.import_export_test_folderpath)


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


    #@unittest.skip
    def test_basesensor_create_calibration_reading(self):
        reading_calibrations: [MRPReading.MRPReading] = []


        samples = 1000
        basesensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(self.hal_instance)

        reading:MRPReading.MRPReading = None
        for senid in range(basesensor.sensor_count):
            reading: MRPReading.MRPReading = MRPReading.MRPReading()
            reading.measurement_config.id = senid

            for i in range(samples):
                print("capture: {}".format(i))
                basesensor.query_readout()

                measurement_a = MRPReadingEntry.MRPReadingEntry()
                measurement_a.value = basesensor.get_b(senid)
                measurement_a.temperature = basesensor.get_temp(senid)
                reading.insert_reading_instance(measurement_a, False)

        reading_calibrations.append(reading)

        export_filepath = os.path.join(self.import_export_test_folderpath, "test_basesensor_create_calibration_reading_error_{}.png".format(samples))
        MRPDataVisualization.MRPDataVisualization.plot_error(reading, "test_basesensor_create_calibration_reading_error", export_filepath)

        export_filepath = os.path.join(self.import_export_test_folderpath, "test_basesensor_create_calibration_reading_scatter_{}.png".format(samples))
        MRPDataVisualization.MRPDataVisualization.plot_scatter(reading, "test_basesensor_create_calibration_reading_scatter", export_filepath)




if __name__ == '__main__':
    unittest.main()