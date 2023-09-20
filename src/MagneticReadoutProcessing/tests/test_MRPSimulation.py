from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import os
import random
import unittest
import numpy as np

from MRP import MRPPolarVisualization, MRPSimulation
class TestMPRSimulation(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:
        self.batch_generation_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated_testdata")
        if not os.path.exists(self.batch_generation_folder_path):
            os.makedirs(self.batch_generation_folder_path)

    @unittest.skip
    def test_simulation_random_full_sphere(self):
        reading = MRPSimulation.MRPSimulation.generate_random_full_sphere_reading(False)
        visu = MRPVisualization.MRPVisualization(reading)
        #visu.plot3d(None)

    @unittest.skip
    def test_simulation_random_full_sphere_random(self):
        reading = MRPSimulation.MRPSimulation.generate_random_full_sphere_reading(True)
        visu = MRPVisualization.MRPVisualization(reading)
        #visu.plot3d(None)

    @unittest.skip
    def test_simulation_cubic_magnet(self):
        no_samples = 10
        magnet_size = 12 # mm
        add_random_factor = True
        for sample in range(no_samples):
            reading = MRPSimulation.MRPSimulation.generate_reading(magnet_size, add_random_factor)
            visu = MRPVisualization.MRPVisualization(reading)
            visu.plot3d(None)

            name = os.path.join(self.batch_generation_folder_path, 'test_simulation_cubic_magnet_' + str(magnet_size) + "mm_" + str(sample))
            visu.plot3d(name + ".mag.pkl.png")
            reading.dump_to_file( name + ".mag.pkl")

    @unittest.skip
    def test_simulation_cubic_magnet_with_random_polarisazion(self):
        no_samples = 10
        magnet_size = 12 # mm
        add_random_factor = True
        add_random_polarisation = True
        for sample in range(no_samples):
            reading = MRPSimulation.MRPSimulation.generate_reading(magnet_size, add_random_factor, add_random_polarisation)
            visu = MRPVisualization.MRPVisualization(reading)
            visu.plot3d(None)

            name = os.path.join(self.batch_generation_folder_path, 'test_simulation_cubic_magnet_' + str(magnet_size) + "mm_" + str(sample) + "_randompolarisation")
            visu.plot3d(name + ".mag.pkl.png")
            reading.dump_to_file( name + ".mag.pkl")

if __name__ == '__main__':
    unittest.main()
