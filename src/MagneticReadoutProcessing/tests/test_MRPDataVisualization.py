from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np


from MRP import MRPDataVisualization, MRPSimulation, MRPReading, MRPReadingEntry


class TestMPRDataVisualization(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:
        self.result_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated_plots")
        if not os.path.exists(self.result_folder_path):
            os.makedirs(self.result_folder_path)


    def test_histogram_generated_data(self):
        reading_A = MRPReading.MRPReading()
        reading_A.measurement_config.configure_halfsphere()
        self.assertIsNotNone(reading_A)

        for i in range(0, 10000):
            e: MRPReadingEntry.MRPReadingEntry = MRPReadingEntry.MRPReadingEntry()
            e.id = i
            e.value = random.uniform(0, 1) * 10.0

            reading_A.insert_reading_instance(e, False)

        self.assertIsNotNone(reading_A)

        export_filename: str = os.path.join(self.result_folder_path, 'test_histogram_generated_data.png')
        MRPDataVisualization.MRPDataVisualization.plot_histogram(reading_A, "test_histogram_generated_data", export_filename)





if __name__ == '__main__':
    unittest.main()
