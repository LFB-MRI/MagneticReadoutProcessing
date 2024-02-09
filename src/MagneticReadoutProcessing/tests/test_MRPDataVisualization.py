import re

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
        self.asset_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/test_histogram")
        if not os.path.exists(self.result_folder_path):
            os.makedirs(self.result_folder_path)


    def test_histogram_realdata(self):

        files = [f for f in os.listdir(self.asset_folder_path) if re.match(r'(.)*.mag.json', f)]


        for e in files:
            reading = MRPReading.MRPReading()
            import_file: str = os.path.join(self.asset_folder_path, e)
            reading.load_from_file(import_file)

            export_filename: str = os.path.join(self.result_folder_path, reading.get_name().replace(" ", "_") + ".png")
            name: str = reading.get_name()
            MRPDataVisualization.MRPDataVisualization.plot_histogram(reading, name, export_filename)

    def test_histogram_generated_data(self):
        reading = MRPReading.MRPReading()
        #reading.measurement_config.configure_halfsphere()
        reading.set_name("test_histogram_generated_data")
        self.assertIsNotNone(reading)

        for i in range(0, 10000):
            e: MRPReadingEntry.MRPReadingEntry = MRPReadingEntry.MRPReadingEntry()
            e.id = i
            e.value = random.uniform(0, 1) * 10.0

            reading.insert_reading_instance(e, False)

        self.assertIsNotNone(reading)

        export_filename: str = os.path.join(self.result_folder_path, reading.get_name())
        MRPDataVisualization.MRPDataVisualization.plot_histogram(reading, "test_histogram_generated_data", export_filename)





if __name__ == '__main__':
    unittest.main()
