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
        self.asset_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
        if not os.path.exists(self.result_folder_path):
            os.makedirs(self.result_folder_path)


    def test_histogram_realdata(self):
        reading = MRPReading.MRPReading()
        import_file: str = os.path.join(self.asset_folder_path, 'MMC5603NJ_1000_SAMPLES_1_AVG.mag.json')
        reading.load_from_file(import_file)

        export_filename: str = os.path.join(self.result_folder_path, 'MMC5603NJ_1000_SAMPLES_1_AVG_HISTOGRAMM.mag.json.png')
        MRPDataVisualization.MRPDataVisualization.plot_histogram(reading, "MMC5603NJ_1000_SAMPLES_1_AVG_HISTOGRAMM", export_filename)

        reading = MRPReading.MRPReading()
        import_file: str = os.path.join(self.asset_folder_path, 'MMC5603NJ_1000_SAMPLES_5_AVG.mag.json')
        reading.load_from_file(import_file)

        export_filename: str = os.path.join(self.result_folder_path,'MMC5603NJ_1000_SAMPLES_5_AVG_HISTOGRAMM.mag.json.png')
        MRPDataVisualization.MRPDataVisualization.plot_histogram(reading, "MMC5603NJ_1000_SAMPLES_5_AVG_HISTOGRAMM",export_filename)

    def test_histogram_generated_data(self):
        reading = MRPReading.MRPReading()
        reading.measurement_config.configure_halfsphere()
        self.assertIsNotNone(reading)

        for i in range(0, 10000):
            e: MRPReadingEntry.MRPReadingEntry = MRPReadingEntry.MRPReadingEntry()
            e.id = i
            e.value = random.uniform(0, 1) * 10.0

            reading.insert_reading_instance(e, False)

        self.assertIsNotNone(reading)

        export_filename: str = os.path.join(self.result_folder_path, 'test_histogram_generated_data.png')
        MRPDataVisualization.MRPDataVisualization.plot_histogram(reading, "test_histogram_generated_data", export_filename)





if __name__ == '__main__':
    unittest.main()
