from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import math
import numpy as np
import pytest
import unittest
import random
import configparser
import os

from MRP import MRPConfig, MRPPolarVisualization, MRPReading, MRPMeasurementConfig
class TestMRPReading(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    def setUp(self) -> None:

        self.import_export_test_folderpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(self.import_export_test_folderpath):
            os.makedirs(self.import_export_test_folderpath)

        self.import_export_test_filepath = os.path.join(self.import_export_test_folderpath, "tmp.pkl")

    def test_full_sphere_reading(self) -> MRPReading:
        reading = MRPReading.MRPReading()
        reading.measurement_config.configure_fullsphere()
        self.assertIsNotNone(reading)

        reading.set_additional_data('test', 1)
        reading.sensor_id = 0

        n_phi = reading.measurement_config.n_phi
        n_theta = reading.measurement_config.n_theta
        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:np.pi:n_theta * 1j, 0.0:2.0 * np.pi:n_phi * 1j]

        ii = 0
        jj = 0
        for j in phi[0, :]:
            ii = ii + 1
            for i in theta[:, 0]:
                jj = jj + 1

                if i <= math.pi/2.0:
                    reading.insert_reading(1, j, i, ii, jj, random.uniform(0, 1) * 10.0 + 25.0)
                else:
                    reading.insert_reading(-1, j, i, ii, jj, random.uniform(0, 1) * 10.0 + 25.0)

        #visu = MRPVisualization.MRPVisualization(reading)
        # 2D PLOT INTO A WINDOW
        #visu.plot3d(None)
        #visu.plot2d_side(None)

        # 3D PLOT TO FILE
        # visu.plot3d(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plot3d_3d.png'))


if __name__ == '__main__':
    unittest.main()
