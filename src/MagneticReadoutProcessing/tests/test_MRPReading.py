from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import math
import numpy as np
import pytest
import unittest
import random

from MRP import MRPReading, MRPSimulation




import os
class TestMPRReading(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    def setUp(self) -> None:


        self.import_export_test_folderpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(self.import_export_test_folderpath):
            os.makedirs(self.import_export_test_folderpath)

        self.import_export_test_filepath = os.path.join(self.import_export_test_folderpath, "tmp")

    def test_matrix_init(self):
        reading = MRPSimulation.MRPSimulation.generate_reading()
        matrix = reading.to_numpy_matrix()

        n_phi = reading.measurement_config.n_phi
        n_theta = reading.measurement_config.n_theta
        # CHECK MATRIX SHAPE
        self.assertTrue(matrix.shape != (n_theta, ) and len(matrix.shape) <= n_phi)





    def test_reading_init(self) -> MRPReading:
        reading = MRPReading.MRPReading()
        reading.measurement_config.configure_fullsphere()
        self.assertIsNotNone(reading)

        reading.set_additional_data('test', 1)
        reading.sensor_id = 0

        n_phi = reading.measurement_config.n_phi
        n_theta = reading.measurement_config.n_theta
        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:0.5 * np.pi:n_theta * 1j, 0.0:2.0 * np.pi:n_phi * 1j]

        ii = 0
        jj = 0
        for j in phi[0, :]:
            ii = ii + 1
            for i in theta[:, 0]:
                jj = jj + 1
                reading.insert_reading(random.uniform(0, 1), j, i, ii, jj)
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
        reading = MRPReading.MRPReading()
        self.assertIsNotNone(reading)


        reading.insert_reading(random.uniform(0, 1), 0.0, 0.0, 0, 0)
        # CONVERT TO CARTESIAN COORDINATES
        cartesian_result = reading.to_numpy_cartesian()
        self.assertIsNotNone(cartesian_result)
        self.assertNotEqual(len(cartesian_result), 0)

if __name__ == '__main__':
    unittest.main()
