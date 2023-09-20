from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np


from MRP import MRPAnalysis, MRPReading, MRPReadingEntry, MRPDataVisualization

class TestMRPDataVisualization(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self):
        # TMP FOLDER FOR GRAPH EXPORTS
        self.import_export_test_folderpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(self.import_export_test_folderpath):
            os.makedirs(self.import_export_test_folderpath)



        self.reading_zero = MRPReading.MRPReading()
        self.reading_zero.measurement_config.id = 0

        self.reading_one = MRPReading.MRPReading()
        self.reading_one.measurement_config.id = 1

        for i in range(100):
            measurement_a = MRPReadingEntry.MRPReadingEntry()
            measurement_a.value = 0.0
            measurement_a.temperature = (random.random() - 0.5) * 50.0
            self.reading_zero.insert_reading_instance(measurement_a, False)

            measurement_b = MRPReadingEntry.MRPReadingEntry()
            measurement_b.value = (random.random() -0.5) * 0.05
            measurement_b.temperature = (random.random() - 0.5) * 25.0
            self.reading_one.insert_reading_instance(measurement_b, False)


        self.reading_set_a = MRPReading.MRPReading()
        self.reading_set_a.measurement_config.id = 2

        values = [10, 5, 12, 2, 20, 4.5]
        for value in values:
            measurement = MRPReadingEntry.MRPReadingEntry()
            measurement.value = value
            measurement.temperature = value * 2.0
            self.reading_set_a.insert_reading_instance(measurement, False)
    def test_std_deviation(self):
        deviation_zero = MRPAnalysis.MRPAnalysis.calculate_std_deviation(self.reading_zero)
        self.assertEquals(deviation_zero, 0.0)

        deviation_set_a = MRPAnalysis.MRPAnalysis.calculate_std_deviation(self.reading_set_a)
        self.assertAlmostEquals(deviation_set_a, 6.0028, 2)

    def test_mean(self):
        mean_zero = MRPAnalysis.MRPAnalysis.calculate_mean(self.reading_zero)
        self.assertEquals(mean_zero, 0.0)

        mean_set_a = MRPAnalysis.MRPAnalysis.calculate_mean(self.reading_set_a)
        self.assertAlmostEquals(mean_set_a, 8.9166, 2)

    def test_variance(self):
        variance_zero = MRPAnalysis.MRPAnalysis.calculate_variance(self.reading_zero)
        self.assertEquals(variance_zero, 0.0)

        variance_set_a = MRPAnalysis.MRPAnalysis.calculate_variance(self.reading_set_a)
        self.assertAlmostEquals(variance_set_a, 36.034, 2)

    def test_error_visualisation(self):
        export_filepath = os.path.join(self.import_export_test_folderpath, "test_error_visualisation.png")
        rset: [MRPReading.MRPReading] = [self.reading_zero, self.reading_one, self.reading_set_a]
        MRPDataVisualization.MRPDataVisualization.plot_error(rset, "test_error_visualisation", export_filepath)

    def test_scatter_visualisation(self):
        export_filepath = os.path.join(self.import_export_test_folderpath, "test_scatter_visualisation.png")
        rset: [MRPReading.MRPReading] = [self.reading_zero, self.reading_one, self.reading_set_a]
        MRPDataVisualization.MRPDataVisualization.plot_scatter(rset, "test_scatter_visualisation", export_filepath)


    def test_temperature_visualisation(self):
        export_filepath = os.path.join(self.import_export_test_folderpath, "test_temperature_visualisation.png")
        rset: [MRPReading.MRPReading] = [self.reading_zero, self.reading_one, self.reading_set_a]
        MRPDataVisualization.MRPDataVisualization.plot_temperature(rset, "test_temperature_visualisation", export_filepath)




if __name__ == '__main__':
    unittest.main()