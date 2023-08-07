import math

import numpy as np
import pytest
import unittest
import random
from MagneticReadoutProcessing import MRPConfig, MRPVisualization, MRPReading, MRPMeasurementConfig, MRPSimulation, MRPHallbachArrayGenerator
import configparser
import os
import vector
class TestMRPHallbachArrayGenerator(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    def setUp(self) -> None:

        self.import_export_test_folderpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(self.import_export_test_folderpath):
            os.makedirs(self.import_export_test_folderpath)


    @unittest.skip
    def test_helper_plot_vectors(self):
        vectors = [vector.obj(x=1, y=-2, z=-3), vector.obj(x=-4, y=4, z=2)]
        # NORMAL PLOT
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.plot_vectors(vectors)
        # SAVE TO FIG PLOT
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.plot_vectors(vectors, "test vector plot saved", self.import_export_test_folderpath + "/vector_save.png")

    @unittest.skip
    def test_generate_1k_hallbach_EIGHT_OPENSCAD(self):
        reading = MRPSimulation.MRPSimulation.generate_cubic_reading()
        readings= []
        for idx in range(8):
            readings.append(reading)

        res = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(readings)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_openscad_model(res, self.import_export_test_folderpath + "/test.scad")

    #@unittest.skip
    def test_generate_1k_hallbach_TWELVE_OPENSCAD(self):
        reading = MRPSimulation.MRPSimulation.generate_cubic_reading()
        readings = []
        for idx in range(12):
            readings.append(reading)

        res = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(
            readings)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_openscad_model(res, self.import_export_test_folderpath + "/test.scad", _2d_object_code=False)



    @unittest.skip
    def test_generate_1k_hallbach_EIGHT_IDEAL_PLOT(self):
        reading = MRPSimulation.MRPSimulation.generate_cubic_reading()
        readings = []
        for idx in range(8):
            readings.append(reading)

        res = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(readings)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_magnet_streamplot(res, self.import_export_test_folderpath + "/test.png")



if __name__ == '__main__':
    unittest.main()
