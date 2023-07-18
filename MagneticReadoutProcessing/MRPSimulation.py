import math
import random
import numpy as np
from MagneticReadoutProcessing import MRPReading, MRPHelpers
import magpylib as magpy
from scipy.spatial.transform import Rotation as R
import vg
class MRPSimulation():
    """ This class generates simulated readings, so its possible to generate a reading using a simulated ideal 10x10x10 magnet """
    @staticmethod
    def generate_cubic_reading(_size_mm: int = 12, _randomize_magnetization:bool = False, _add_random_polarisation:bool = False, _sensor_distance_radius_mm: int = 40) -> MRPReading.MRPReading:
        """
        Generate a cubic magnet using components from magpylib to simulate a magnet and hallsensor.
        Then the virtual hallsensor is moved around the magnet and the values are stored in a reading.

        :param _size_mm: Optional;cubic magnet edge length in mm
        :type _size_mm: int
        :param _add_random_polarisation: Optional; add a random factor for the magnetization vector value
        :type _add_random_polarisation: bool
        :param _randomize_magnetization: Optional; appy a random factor to the hallsensor readouts
        :type _randomize_magnetization: bool
        :param _sensor_distance_radius_mm: distance between magnet and hallsensor
        :type _sensor_distance_radius_mm: int
        :return MRPReading: a generated MRPReading with set meta-data
        :rtype MRPReading: MRPReading

        """

        # CREATE MAGNET IN THE CENTER
        magnetization = (0, 0, 100)
        if _add_random_polarisation:
            magnetization = (0, 100 * random.uniform(0, 0.5), 100 * random.uniform(0.5, 1))


        magnet = magpy.magnet.Cuboid(magnetization=magnetization, dimension= (_size_mm, _size_mm, _size_mm), position=(0, 0, 0))
        magnet.rotate_from_rotvec((0,90,0), degrees=True)
        # CREATE ONE HALLSENSOR PROBE

        hallsensor_center = magpy.Sensor(position=(0, 0, 0), style_label='S1')
        hallsensor_r1 = magpy.Sensor(position=(0, 0, _sensor_distance_radius_mm), style_label='S1')
        hallsensor_r2 = magpy.Sensor(position=(0, 0, -_sensor_distance_radius_mm), style_label='S1')


        sensor_collection = magpy.Collection(hallsensor_center, hallsensor_r1,hallsensor_r2, style_label='sensor_collection')
        simulation_collection = magpy.Collection(magnet,sensor_collection,  style_label='simulation_collection')

        # CREATE READING
        reading = MRPReading.MRPReading(None, _sensor_id=0, _sensor_radius=_sensor_distance_radius_mm)
        reading.measurement_config['n_theta'] = 9#18
        reading.measurement_config['n_phi'] = 18#36
        reading.measurement_config['theta_radians'] = math.radians(180)
        reading.measurement_config['phi_radians'] = math.radians(360)
        reading.set_additional_data('is_generated_reading', 1)
        reading.set_additional_data('generation_source', 'magpylib')

        reading.set_additional_data('magnet_type', 'cuboid')
        reading.set_additional_data('magnet_dimension', '12x12x12')


        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:np.pi:reading.measurement_config['n_theta'] * 1j, 0.0:2.0 * np.pi:reading.measurement_config['n_phi'] * 1j]


        for index_phi, p in enumerate(phi[0, :]):
            for index_theta, t in enumerate(theta[:, 0]):
                horizontal_degree = math.degrees(p)
                vertical_degree = math.degrees(t)

                sensor_collection.reset_path()
                sensor_collection.rotate_from_euler(horizontal_degree, 'y', degrees=True)
                # CALC X Y Z
                horizontal_degree = math.degrees(t)
                vertical_degree = math.degrees(p)
                pos = MRPHelpers.asCartesian_degree((_sensor_distance_radius_mm, horizontal_degree, vertical_degree))




                #print(hallsensor.position)
                # GET BFIELD OF SENSOR
                readres = hallsensor_r1.getB(magnet)
                # CALCULATE B FIELD MAGNITUDE
                value = np.sqrt(readres.dot(readres))

                if readres[2] < 0:
                    value = -value

                if _randomize_magnetization:
                    value = value * random.uniform(0.9, 1)
                #print(value)
                reading.insert_reading(value, p, t, index_phi, index_theta, 25.0, True)

            # FOR DEBUGGING
        #magpy.show(simulation_collection)
        i =0

        return reading


    @staticmethod
    def generate_random_full_sphere_reading(_full_random: bool = False) -> MRPReading.MRPReading:
        """
        Generate a full sphere reading with random field values and predefined meta-data.


        :param _full_random: Optional; if true each inserted datapoint is random in polarity and strength
        :type _full_random: bool

        :return MRPReading: a generated MRPReading with set meta-data
        :rtype MRPReading: MRPReading

        """
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