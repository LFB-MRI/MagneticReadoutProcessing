from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import unittest

import magpylib as magpy
import numpy as np
from matplotlib import pyplot as plt

from MRP import MRPSimulation, MRPReadoutSource

"""
TODO
create nicht random  reading using simulation
reading laden
#readout source erstellen

als test:
radout source und testmagnet + sensor an versch positionen positionieren
b feld vergelicehn

"""


def plot_field_lines_two_sources(_source1: magpy.magnet, _source2: magpy.magnet):
    fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(13, 5))
    ts = np.linspace(-40, 40, 40)
    grid = np.array([[(x, 0, z) for x in ts] for z in ts])

    B_ref = magpy.getB(_source1, grid)
    Bamp_ref = np.linalg.norm(B_ref, axis=2)
    Bamp_ref /= np.amax(Bamp_ref)

    B_gen = magpy.getB(_source2, grid)
    Bamp_gen = np.linalg.norm(B_gen, axis=2)
    Bamp_gen /= np.amax(Bamp_gen)

    sp_ref = ax1.streamplot(grid[:, :, 0], grid[:, :, 2], B_ref[:, :, 0], B_ref[:, :, 2], density=2, color=Bamp_ref,
                            linewidth=np.sqrt(Bamp_ref) * 3, cmap='coolwarm')
    sp_gen = ax2.streamplot(grid[:, :, 0], grid[:, :, 2], B_gen[:, :, 0], B_gen[:, :, 2], density=2, color=Bamp_ref,
                            linewidth=np.sqrt(Bamp_gen) * 3, cmap='coolwarm')
    ax1.set(title='MagPyLib_magnet', xlabel='x-position [mm]', ylabel='z-position [mm]', aspect=1)
    ax2.set(title='CUSTOMSOURCE_magnet', xlabel='x-position [mm]', ylabel='z-position [mm]', aspect=1)
    plt.colorbar(sp_ref.lines, ax=ax1, label='[mT]')
    plt.colorbar(sp_gen.lines, ax=ax2, label='[mT]')
    plt.tight_layout()
    plt.show()



class TestMPRSimulation(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    # CALLED BEFORE EACH SUB-TESTCASE
    def setUp(self) -> None:
        pass


    def test_readoutsource_misc(self):
        pass

    @unittest.skip
    def test_readoutsource_initial(self):
        magnet_size = 12 # mm

        generated_reading = MRPSimulation.MRPSimulation.generate_reading(magnet_size)
        gen_magnet = MRPReadoutSource.MRPReadoutSource(generated_reading)



        # TODO PLOT FLIED FOR TESTING

        # SETUP REFERENCE MAGNET
        ref_magnet = magpy.magnet.Cuboid(magnetization=(0, 0, 100), dimension=(magnet_size, magnet_size, magnet_size),position=(0, 0, 0))

        # CREATE SENSORS
        gen_sensor = magpy.Sensor(position=(0, 0, 0), style_label='S1')
        ref_sensor = magpy.Sensor(position=(0, 0, 0), style_label='S1')

        # CREATE COLLECTIONS
        gen_collection = magpy.Collection(gen_magnet, gen_sensor,style_label='gen_collection')
        ref_collection = magpy.Collection(ref_magnet, ref_sensor,style_label='ref_collection')

        # TESTPOSITIONS
        testpositions = [(0 ,0 ,0)] #,(20 ,40 ,0),(50 ,0 ,0), (15 ,15 ,15)]

        for idx, point in enumerate(testpositions):
            gen_sensor.position = point
            ref_magnet.position = point

            gen_value = gen_sensor.getB(gen_magnet)
            ref_value = ref_sensor.getB(ref_magnet)

            gen_mag_value = np.sqrt(gen_value.dot(gen_value))
            ref_mag_value = np.sqrt(ref_value.dot(ref_value))


            print("gen_value:{} ref_value:{}".format(gen_mag_value, ref_mag_value))


            # PLOT FIELD LINES
            plot_field_lines_two_sources(ref_magnet, ref_magnet)
            i = 0
            #plot field lines
            #side by side
            #self.assertAlmostEquals(gen_mag_value, ref_mag_value)


