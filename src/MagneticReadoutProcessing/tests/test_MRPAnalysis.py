from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np


from MRP import MRPAnalysis, MRPReading, MRPPolarVisualization, MRPSimulation, MRPReadingEntry

class TestMPRAnalysis(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:
        # USE DEFAULT CONFIG


        self.reading_A = MRPReading.MRPReading()
        self.reading_A.measurement_config.configure_halfsphere()
        self.assertIsNotNone(self.reading_A)

        self.reading_B = MRPReading.MRPReading()
        self.reading_B.measurement_config.configure_halfsphere()
        self.assertIsNotNone(self.reading_B)

        self.reading_A.sensor_id = 0
        self.reading_B.sensor_id = 1

        n_phi = self.reading_A.measurement_config.n_phi
        n_theta = self.reading_A.measurement_config.n_theta
        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:0.5 * np.pi:n_theta * 1j, 0.0:2.0 * np.pi:n_phi * 1j]

        ii = 0
        jj = 0
        for j in phi[0, :]:
            ii = ii + 1
            for i in theta[:, 0]:
                jj = jj + 1
                self.reading_A.insert_reading(random.uniform(0, 1)*10.0, j, i, ii, jj)
                self.reading_B.insert_reading(random.uniform(0, 1)*10.0, j, i, ii, jj)
    # JUST USED FOR PREPARATION


    def test_apply_global_offset_inplace(self):
        reading = MRPReading.MRPReading()
        # take a few measurements
        for i in range(1000):
            measurement = MRPReadingEntry.MRPReadingEntry()
            # readout sensor or use dummy data and assign result
            measurement.value = 1.0
            reading.insert_reading_instance(measurement, False)

        reading_mean_value = MRPAnalysis.MRPAnalysis.calculate_mean(reading)
        reading_mean_value = -reading_mean_value
        MRPAnalysis.MRPAnalysis.apply_global_offset_inplace(reading, reading_mean_value)

        # TEST
        for entry in reading.data:
            self.assertEquals(entry.value, 0.0) # 1.0 - 1.0 should be zero :)



    @unittest.skip
    def test_calibration_fft(self):
        reading_ideal = MRPSimulation.MRPSimulation.generate_reading()
        res = MRPAnalysis.MRPAnalysis.calculate_fft(reading_ideal, True, True)

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


    def test_calculate_center_of_gravity(self):
        # TODO
        # CALULATE CENTER OF GRAVITY
        # STORE MAGNET TYPE IN READING -> DROP DOWN
        # CREATE FROM CoG a magpylib instance with magnet type
        # generate hallbach arrray with count a ring

        reading_ideal = MRPSimulation.MRPSimulation.generate_reading()

        result_vector = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(reading_ideal)

        # SETTING THE MAGNET TYPE IS NEEDED FOR LATER OPENSCAD GENERATION


        # result_vector


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


    def test_merge_analysis_EQUAL(self):

        self.assertIsNotNone(self.reading_A)
        # MERGE
        merged_reading = MRPAnalysis.MRPAnalysis.merge_two_half_sphere_measurements_to_full_sphere(self.reading_A, self.reading_A)
        self.assertIsNotNone(merged_reading)
        # CHECK RESULT
        visu = MRPPolarVisualization.MRPPolarVisualization(merged_reading)
        # PLOT INTO A WINDOW
        visu.plot3d(None)


    def test_merge_analysis_TWO_READINGS(self):
        self.assertIsNotNone(self.reading_A)
        self.assertIsNotNone(self.reading_B)

        merged_reading = MRPAnalysis.MRPAnalysis.merge_two_half_sphere_measurements_to_full_sphere(self.reading_A,
                                                                                               self.reading_B)
        self.assertIsNotNone(merged_reading)
        # CHECK RESULT
        visu = MRPPolarVisualization.MRPPolarVisualization(merged_reading)
        # 2D PLOT INTO A WINDOW
        visu.plot3d(None)
        # 3D PLOT TO FILE
        #visu.plot3d(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plot3d_3d.png'))


if __name__ == '__main__':
    unittest.main()
