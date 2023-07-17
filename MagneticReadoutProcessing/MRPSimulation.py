""" This class generates simulated readings, so its possible to generate a reading using a simulated ideal 10x10x10 magnet """
import math
import random
import numpy as np
from MagneticReadoutProcessing import MRPReading, MRPHelpers
import magpylib as magpy
import matplotlib.pyplot as plt
class MRPSimulation(object):
    @staticmethod
    def generate_cubic_reading(_size_mm: int = 12, _randomize_magnetization=False,
                               _sensor_distance_radius_mm: int = 40) -> MRPReading.MRPReading:


        # CREATE MAGNET IN THE CENTER
        magnet = magpy.magnet.Cuboid(magnetization=(0,0,100), dimension= (_size_mm, _size_mm, _size_mm), position=(0, 0, 0))

        # CREATE ONE HALLSENSOR PROBE
        hallsensor = magpy.Sensor(style_label='S1')
        simulation_collection = magpy.Collection(magnet, hallsensor, style_label='simulation_collection')


        # CREATE READING
        reading = MRPReading.MRPReading(None, _sensor_id=0, _sensor_radius=_sensor_distance_radius_mm)
        reading.measurement_config['n_theta'] = 18
        reading.measurement_config['n_phi'] = 36
        reading.measurement_config['theta_radians'] = math.radians(180)
        reading.measurement_config['phi_radians'] = math.radians(360)
        reading.set_additional_data('is_generated_reading', 1)
        reading.set_additional_data('generation_source', 'magpylib')

        reading.set_additional_data('magnet_type', 'cuboid')
        reading.set_additional_data('magnet_dimension', 'magpylib')


        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:np.pi:reading.measurement_config['n_theta'] * 1j, 0.0:2.0 * np.pi:reading.measurement_config['n_phi'] * 1j]


        for index_phi, p in enumerate(phi[0, :]):
            for index_theta, t in enumerate(theta[:, 0]):

                # CALC X Y Z

                hallsensor.position = MRPHelpers.asCartesian((_sensor_distance_radius_mm, t, p))

                #print(hallsensor.position)
                #plot = magpy.show(simulation_collection)

                magpy.show(simulation_collection)


                # TODO SET ORIENTATION OF SENSOR PROBE
                # TODO CORRECT IMAGE
                readres = hallsensor.getB(magnet)

                value = math.sqrt(math.pow(readres[0],2.0)+ math.pow(readres[1],2.0)+ math.pow(readres[2],2.0))
                print(value)
                reading.insert_reading(value, p, t, index_phi, index_theta, 25.0, True)


        return reading


    @staticmethod
    def generate_random_full_sphere_reading(_full_random: bool = False) -> MRPReading.MRPReading:
        reading = MRPReading.MRPReading(None)
        reading.sensor_id = 0

        reading.measurement_config['n_theta'] = 18
        reading.measurement_config['n_phi'] = 36
        reading.measurement_config['theta_radians'] = math.radians(180)
        reading.measurement_config['phi_radians'] = math.radians(360)
        reading.set_additional_data('is_generated_reading', 1)
        reading.set_additional_data('generation_source', 'random')
        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:np.pi:reading.measurement_config['n_theta'] * 1j, 0.0:2.0 * np.pi:reading.measurement_config['n_phi'] * 1j]


        center = reading.measurement_config['theta_radians']/2.0

        for index_phi, p in enumerate(phi[0, :]):
            for index_theta, t in  enumerate(theta[:, 0]):
                # ADD IF UPPER SPHERE + values
                # - on lower

                if _full_random:
                    reading.insert_reading(-100 + random.uniform(0, 1) * 200.0, p, t, index_phi, index_theta, 25.0)
                else:
                    if t > center:
                        reading.insert_reading(-80 + random.uniform(0, 1) * 40.0, p, t, index_phi, index_theta, 25.0)
                    else:
                        reading.insert_reading(80 + random.uniform(0, 1) * 40.0, p, t, index_phi, index_theta, 25.0)

        # ADD METADATA
        # ADD NAME, MAGNET INFORMATION

        # create magpi lib magnet
        # roate source around
        return reading