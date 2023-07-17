import unittest

import magpylib as magpy
import numpy as np

from MagneticReadoutProcessing import MRPSimulation, MRPVisualization, MRPReadoutSource

"""
TODO
create nicht random  reading using simulation
reading laden
#readout source erstellen

als test:
radout source und testmagnet + sensor an versch positionen positionieren
b feld vergelicehn

"""

class TestMPRSimulation(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:
        pass

    def test_readoutsource(self):
        magnet_size = 12 # mm
        generated_reading = MRPSimulation.MRPSimulation.generate_cubic_reading(magnet_size)
        gen_magnet = MRPReadoutSource.MRPReadoutSource(generated_reading)


        # TODO PLOT FLIED FOR TESTING

        # SETUP REFERENCE MAGNET
        ref_magnet = magpy.magnet.Cuboid(magnetization=(0,0,100), dimension=(magnet_size, magnet_size, magnet_size),position=(0, 0, 0))

        # CREATE SENSORS
        gen_sensor = magpy.Sensor(position=(0, 0, 0), style_label='S1')
        ref_sensor = magpy.Sensor(position=(0, 0, 0), style_label='S1')

        # CREATE COLLECTIONS
        gen_collection = magpy.Collection(gen_magnet, gen_sensor,style_label='gen_collection')
        ref_collection = magpy.Collection(ref_magnet, ref_sensor,style_label='ref_collection')

        # TESTPOSITIONS
        testpositions = [(20 ,20 ,0),(20 ,40 ,0),(50 ,0 ,0), (15 ,15 ,15)]

        for idx, point in enumerate(testpositions):
            gen_sensor.position = point
            ref_magnet.position = point

            gen_value = gen_sensor.getB(gen_magnet)
            ref_value = ref_sensor.getB(ref_magnet)

            gen_mag_value = np.sqrt(gen_value.dot(gen_value))
            ref_mag_value = np.sqrt(ref_value.dot(ref_value))

            self.assertAlmostEquals(gen_mag_value, ref_mag_value)


