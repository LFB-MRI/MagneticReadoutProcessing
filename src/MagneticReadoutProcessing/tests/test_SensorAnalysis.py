from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np


import MRPAnalysis, MRPReading, MRPPolarVisualization, MRPSimulation, MRPReadingEntry

class TestMPRAnalysis(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:
        self.reading_zero = MRPReading.MRPReading()


        for i in range(100):
            measurement = MRPReadingEntry.MRPReadingEntry()
            measurement.value = 0.0
            self.reading_zero.insert_reading_instance(measurement, False)


        self.reading_set_a = MRPReading.MRPReading()
        values = [10, 5, 12, 2, 20, 4.5]
        for value in values:
            measurement = MRPReadingEntry.MRPReadingEntry()
            measurement.value = value
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




if __name__ == '__main__':
    unittest.main()