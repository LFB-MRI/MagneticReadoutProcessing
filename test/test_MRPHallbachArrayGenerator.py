import math

import numpy as np
import pytest
import unittest
import random
from MagneticReadoutProcessing import MRPConfig, MRPVisualization, MRPReading, MRPMeasurementConfig, MRPSimulation, MRPHallbachArrayGenerator
import configparser
import os
class TestMRPHallbachArrayGenerator(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    def setUp(self) -> None:

        self.import_export_test_folderpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(self.import_export_test_folderpath):
            os.makedirs(self.import_export_test_folderpath)


    def test_full_sphere_reading(self):
        reading = MRPSimulation.MRPSimulation.generate_cubic_reading()

        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(reading)


if __name__ == '__main__':
    unittest.main()
