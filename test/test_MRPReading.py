import math

import numpy as np
import pytest
import unittest
import random
from MagneticReadoutProcessing import MRPConfig
from MagneticReadoutProcessing import MRPReading
import configparser
import os
class TestMPRReading(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    def setUp(self) -> None:
        # USE DEFAULT CONFIG
        self.config = MRPConfig.MRPConfig(None)
        self.config.load_defaults()


        self.import_export_test_folderpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(self.import_export_test_folderpath):
            os.makedirs(self.import_export_test_folderpath)

        self.import_export_test_filepath = os.path.join(self.import_export_test_folderpath, "tmp.pkl")


    def test_reading_init(self) -> MRPReading:
        reading = MRPReading.MRPReading(self.config)
        self.assertIsNotNone(reading)

        reading.set_additional_data('test', 1)
        reading.sensor_id = 0

        n_phi = self.config.MEASUREMENT_HORIZONTAL_RESOLUTION
        n_theta = self.config.MEASUREMENT_VERTICAL_RESOLUTION
        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:0.5 * np.pi:n_theta * 1j, 0.0:2.0 * np.pi:n_phi * 1j]

        ii = 0
        jj = 0
        for j in phi[0, :]:
            ii = ii + 1
            for i in theta[:, 0]:
                jj = jj + 1
                reading.insert_reading(random.uniform(0, 1), j, i, ii, jj, random.uniform(0, 1)*10.0+25.0)

        return reading

    def test_export_reading(self) -> None:
        reading = self.test_reading_init()
        self.assertIsNotNone(reading)
        # EXPORT READING TO A FILE
        reading.dump_to_file(self.import_export_test_filepath)

    def test_import_reading(self):
        # CREATE EMPTY READING
        reading_imported = MRPReading.MRPReading(None)
        # LOAD READING FROM FILE
        reading_imported.load_from_file(self.import_export_test_filepath)
        # CHECK IF ENTRIES ARE POPULATED
        self.assertIsNotNone(reading_imported.additional_data)
        self.assertIsNotNone(reading_imported.data)

    def test_cartesian_reading(self):
        reading = MRPReading.MRPReading(self.config)
        self.assertIsNotNone(reading)


        n_phi = 1
        n_theta = 1
        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER

        reading.insert_reading(random.uniform(0, 1), 0.0, 0.0, 0, 0, random.uniform(0, 1) * 10.0 + 25.0)
        # CONVERT TO CARTESIAN COORDINATES
        cartesian_result = reading.to_numpy_cartesian()
        self.assertIsNotNone(cartesian_result)
        self.assertNotEqual(len(cartesian_result), 0)


if __name__ == '__main__':
    unittest.main()
