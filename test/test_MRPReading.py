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

        RESULT_FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp/tmp.pkl")
        if not os.path.exists(RESULT_FILEPATH):
            os.makedirs(RESULT_FILEPATH)
        reading.dump_to_file(RESULT_FILEPATH)

    def test_import_readin(self):
        pass

if __name__ == '__main__':
    unittest.main()
