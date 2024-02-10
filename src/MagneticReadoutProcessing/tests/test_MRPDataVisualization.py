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
        self.asset_histogram_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/test_histogram")
        self.asset_linearity_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/test_linearity")
        if not os.path.exists(self.result_folder_path):
            os.makedirs(self.result_folder_path)



    def test_linearity_realdata(self):
        files = [f for f in os.listdir(self.asset_linearity_folder_path) if re.match(r'(.)*.mag.json', f)]

        sensors:set = set()

        for e in files:
            sp: [str] = e.split('_')
            sensors.add(sp[0])


        to_process: dict = {}
        for sensor in sensors:
            to_process[sensor] = {
                'files': [],
                'distance': [],
                'N': [],
                'RUN': [],
                'dist_min': 1000,
                'dist_max': 0
            }

        for s in sensors:
            for e in files:
                if e.startswith(s):
                    DISTANCE = ""
                    N = ""
                    RUN = ""
                    splr: [str] = e.split('_')
                    for sp in splr:
                        if "DISTANCE=" in sp:
                            DISTANCE = sp.split("=")[1]
                            d: int = (int(re.findall(r'\d+', DISTANCE)[0]))
                            to_process[s]['dist_min'] = min(to_process[s]['dist_min'], d)
                            to_process[s]['dist_max'] = max(to_process[s]['dist_max'], d)
                        elif "RUN=" in sp:
                            RUN = sp.split("=")[1]
                        elif "N=" in sp:
                            N = sp.split("=")[1]

                    to_process[s]['files'].append(e)
                    to_process[s]['distance'].append(DISTANCE)
                    to_process[s]['N'].append(N)
                    to_process[s]['RUN'].append(RUN)

        for k in to_process:
            e = to_process[k]

            total_dst: int = to_process[s]['dist_max'] - to_process[s]['dist_min']
            reading_name: str = "Linearity of " + k + " using " + str(len(e['files'])) + " samples over an distance of {}".format(total_dst) + "mm"
            export_filename: str = os.path.join(self.result_folder_path, reading_name.replace(" ", "_").replace("mm", "").replace("{}","") + ".png")

            # IMPORT READINGS
            readings: [MRPReading.MRPReading] = []
            for idx, r in enumerate(e['files']):
                reading: MRPReading.MRPReading = MRPReading.MRPReading()

                if 'tlv493d' in k.lower():
                    reading.set_unit_import_scale_factor(10000.0)




                import_file: str = os.path.join(self.asset_linearity_folder_path, r)
                reading.load_from_file(import_file)
                reading.set_name("DISTANCE={}".format(e['distance'][idx]))
                readings.append(reading)


            MRPDataVisualization.MRPDataVisualization.plot_linearity(readings, reading_name, export_filename)




    def test_histogram_realdata(self):

        files = [f for f in os.listdir(self.asset_histogram_folder_path) if re.match(r'(.)*.mag.json', f)]

        for e in files:
            reading = MRPReading.MRPReading()
            import_file: str = os.path.join(self.asset_histogram_folder_path, e)

            if 'tlv493d' in e.lower():
                reading.set_unit_import_scale_factor(10000.0)
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
