import os
import random
import unittest
import numpy as np
from MagneticReadoutProcessing import MRPAnalysis
from MagneticReadoutProcessing import MRPConfig
from MagneticReadoutProcessing import MRPReading
from MagneticReadoutProcessing import MRPVisualization

class TestMPRAnalysis(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:
        # USE DEFAULT CONFIG
        self.config = MRPConfig.MRPConfig(None)
        self.config.load_defaults()

        self.reading_A = MRPReading.MRPReading(self.config)
        self.reading_B = MRPReading.MRPReading(self.config)
        self.assertIsNotNone(self.reading_A)
        self.assertIsNotNone(self.reading_B)

        self.reading_A.sensor_id = 0
        self.reading_B.sensor_id = 1

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
                self.reading_A.insert_reading(random.uniform(0, 1)*10.0, j, i, ii, jj, random.uniform(0, 1) * 10.0 + 25.0)
                self.reading_B.insert_reading(random.uniform(0, 1)*10.0, j, i, ii, jj, random.uniform(0, 1) * 10.0 + 25.0)
    # JUST USED FOR PREPARATION

    @unittest.skip
    def test_calibration_analysis_zero(self):
        # IF A CALIBRATION READING IS APPLIED ON THE SAME READING THE RESULT SHOULD BE ZERO
        # reading_A is the calibration reading
        # and will be applied directly onto reading_A
        # so the result should be zero for all entries
        MRPAnalysis.MRPAnalysis.apply_calibration_data_inplace(self.reading_A, self.reading_A)
        self.assertIsNotNone(self.reading_A)
        # CHECK FOR VALUES ZERO
        result = self.reading_A.to_numpy_polar()
        for r in result:
            self.assertEqual(r[2], 0.0)

    @unittest.skip
    def test_calibration_analysis_real(self):
        result_original = self.reading_B.to_numpy_polar()
        MRPAnalysis.MRPAnalysis.apply_calibration_data_inplace(self.reading_A, self.reading_B)
        self.assertIsNotNone(self.reading_B)
        # CHECK FOR VALUES ZERO
        result_A = self.reading_A.to_numpy_polar()
        result_B = self.reading_B.to_numpy_polar()
        # CHECK triangle inequality
        for idx, a in enumerate(result_A):
            b = result_B[idx]
            orig = result_original[idx]
            self.assertAlmostEqual(orig[2], b[2] + a[2])

    @unittest.skip
    def test_merge_analysis_EQUAL(self):

        self.assertIsNotNone(self.reading_A)
        # MERGE
        merged_reading = MRPAnalysis.MRPAnalysis.merge_two_half_sphere_measurements_to_full_sphere(self.reading_A, self.reading_A)
        self.assertIsNotNone(merged_reading)
        # CHECK RESULT
        visu = MRPVisualization.MRPVisualization(merged_reading)
        # PLOT INTO A WINDOW
        visu.plot3d(None)

    @unittest.skip
    def test_merge_analysis_TWO_READINGS(self):
        # IMPORT TWO EXISTING READINGS FROM FILE
        reading_top_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/114N2.mag.pkl")
        reading_bottom_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/114S2.mag.pkl")
        # IMPORT TOP READING
        reading_top = MRPReading.MRPReading(None)
        reading_top.load_from_file(reading_top_filepath)
        # IMPORT BOTTOM READING
        reading_bottom = MRPReading.MRPReading(None)
        reading_bottom.load_from_file(reading_bottom_filepath)

        self.assertIsNotNone(reading_top)
        self.assertIsNotNone(reading_bottom)

        merged_reading = MRPAnalysis.MRPAnalysis.merge_two_half_sphere_measurements_to_full_sphere(reading_top,
                                                                                                   reading_bottom)
        self.assertIsNotNone(merged_reading)

        # CHECK RESULT

        visu = MRPVisualization.MRPVisualization(merged_reading)

        # 2D PLOT INTO A WINDOW
        visu.plot3d(None)

        # 3D PLOT TO FILE
        #visu.plot3d(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plot3d_3d.png'))


if __name__ == '__main__':
    unittest.main()
