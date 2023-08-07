import math

import numpy as np
import pytest
import unittest
import random
from MagneticReadoutProcessing import MRPConfig, MRPVisualization, MRPReading, MRPMeasurementConfig, MRPSimulation, MRPHallbachArrayGenerator, MRPMagnetTypes
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



    #@unittest.skip
    def test_generate_1k_hallbach_8_OPENSCAD_3D(self):
        reading = MRPSimulation.MRPSimulation.generate_reading()
        readings = []
        for idx in range(8):
            readings.append(reading)

        res = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(
            readings)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_openscad_model([res],
                                                                                    self.import_export_test_folderpath + "/test_generate_1k_hallbach_8_OPENSCAD_3D.scad",
                                                                                    _2d_object_code=False, _add_annotations=True)

    #@unittest.skip
    def test_generate_1k_hallbach_12_OPENSCAD_2D(self):
        reading = MRPSimulation.MRPSimulation.generate_reading()
        readings = []
        for idx in range(12):
            readings.append(reading)

        res = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(
            readings)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_openscad_model([res], self.import_export_test_folderpath + "/test_generate_1k_hallbach_12_OPENSCAD_2D.scad", _add_annotations=False)

    #@unittest.skip
    def test_generate_1k_hallbach_32_OPENSCAD_2D(self):
        reading = MRPSimulation.MRPSimulation.generate_reading()
        readings = []
        for idx in range(32):
            readings.append(reading)

        res = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction( readings)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_openscad_model([res], self.import_export_test_folderpath + "/test_generate_1k_hallbach_32_OPENSCAD_2D.scad", _add_annotations=False)

    #@unittest.skip
    def test_generat_1k_hallbach_8_24_OPENSCAD_2D(self):
        reading = MRPSimulation.MRPSimulation.generate_reading(MRPMagnetTypes.MagnetType.N45_CUBIC_15x15x15)
        reading_15 = []
        for idx in range(24):
            reading_15.append(reading)

        reading = MRPSimulation.MRPSimulation.generate_reading(MRPMagnetTypes.MagnetType.N45_CUBIC_9x9x9)
        reading_9 = []
        for idx in range(8):
            reading_9.append(reading)

        reading = MRPSimulation.MRPSimulation.generate_reading(MRPMagnetTypes.MagnetType.N45_CUBIC_12x12x12)
        reading_12 = []
        for idx in range(16):
            reading_12.append(reading)

        # GENERATE TWO SETS OF MAGNETS
        res_15 = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(reading_15)
        res_9 = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(reading_9)
        res_12 = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(
            reading_12)

        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_openscad_model([res_15, res_9, res_12], self.import_export_test_folderpath + "/test_generat_1k_hallbach_8_24_OPENSCAD_2D.scad", _add_annotations=False)

    #@unittest.skip
    def test_generate_1k_hallbach_EIGHT_IDEAL_PLOT(self):
        reading = MRPSimulation.MRPSimulation.generate_reading()
        readings = []
        for idx in range(8):
            readings.append(reading)

        res = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(readings)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_magnet_streamplot([res], self.import_export_test_folderpath + "/test.png")



if __name__ == '__main__':
    unittest.main()
