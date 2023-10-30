"""  collection of functions to generate magnet data in software """
import math
import random
import numpy as np
import magpylib as magpy

from MRP import MRPReading, MRPHelpers, MRPMagnetTypes



class MRPSimulationException(Exception):
    def __init__(self, message="MRPSimulationException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPSimulation():
    """ This class generates simulated readings, so its possible to generate a reading using a simulated ideal 10x10x10 magnet """

    @staticmethod
    def generate_reading(_type: MRPMagnetTypes.MagnetType = MRPMagnetTypes.MagnetType.N45_CUBIC_12x12x12, _randomize_magnetization: bool = False,
                         _add_random_polarisation: bool = False,
                         _sensor_distance_radius_mm: int = 40) -> MRPReading.MRPReading:
        """
        Generate a cubic magnet using components from magpylib to simulate a magnet and hallsensor.
        Then the virtual hallsensor is moved around the magnet and the values are stored in a reading.

        :param _type: Type of magnet
        :type _type: MRPMagnetTypes.MagnetType

        :param _add_random_polarisation: Optional; add a random factor for the magnetization vector value
        :type _add_random_polarisation: bool

        :param _randomize_magnetization: Optional; appy a random factor to the hallsensor readouts
        :type _randomize_magnetization: bool

        :param _sensor_distance_radius_mm: distance between magnet and hallsensor
        :type _sensor_distance_radius_mm: int

        :returns: a generated MRPReading with set meta-data
        :rtype: MRPReading.MRPReading

        """

        # CREATE MAGNET IN THE CENTER
        magnetization = (0, 0, 100)
        if _add_random_polarisation:
            magnetization = (0, 100 * random.uniform(0, 0.5), 100 * random.uniform(0.5, 1))

        dim = _type.get_dimension()

        magnet: magpy.magnet = None
        if _type.is_cubic():
            magnet = magpy.magnet.Cuboid(magnetization=magnetization, dimension=_type.get_dimension())
        elif _type.is_cylindrical():
            magnet = magpy.magnet.Cylinder(magnetization=magnetization, dimension=(dim[0], dim[1]))
        else:
            raise MRPSimulationException("magnet type not implemented yet :/")


        magnet.rotate_from_rotvec((0, 90, 0), degrees=True)
        # CREATE ONE HALLSENSOR PROBE

        hallsensor_center = magpy.Sensor(position=(0, 0, 0), style_label='S1')
        hallsensor_r1 = magpy.Sensor(position=(0, 0, _sensor_distance_radius_mm), style_label='S1')
        hallsensor_r2 = magpy.Sensor(position=(0, 0, -_sensor_distance_radius_mm), style_label='S1')

        sensor_collection = magpy.Collection(hallsensor_center, hallsensor_r1, hallsensor_r2,
                                             style_label='sensor_collection')
        simulation_collection = magpy.Collection(magnet, sensor_collection, style_label='simulation_collection')

        # CREATE READING
        reading = MRPReading.MRPReading()
        reading.measurement_config.configure_fullsphere()
        reading.measurement_config.magnet_type = _type

        reading.set_additional_data('is_generated_reading', 1)
        reading.set_additional_data('generation_source', 'magpylib')

        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:np.pi:reading.measurement_config.n_theta * 1j,
                     0.0:2.0 * np.pi:reading.measurement_config.n_phi * 1j]

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

                # print(hallsensor.position)
                # GET BFIELD OF SENSOR
                readres = hallsensor_r1.getB(magnet)
                # CALCULATE B FIELD MAGNITUDE
                value = np.sqrt(readres.dot(readres))

                if readres[2] < 0:
                    value = -value

                if _randomize_magnetization:
                    value = value * random.uniform(0.9, 1)
                # print(value)
                reading.insert_reading(value, p, t, index_phi, index_theta)



        return reading

    @staticmethod
    def __generate_reading_data__(_configured_reading: MRPReading.MRPReading,
                                  _full_random: bool = False) -> MRPReading.MRPReading:
        _configured_reading.set_additional_data('is_generated_reading', 1)
        _configured_reading.set_additional_data('generation_source', 'random')
        # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
        theta, phi = np.mgrid[0.0:np.pi:_configured_reading.measurement_config.n_theta * 1j,
                     0.0:2.0 * np.pi:_configured_reading.measurement_config.n_phi * 1j]

        center = _configured_reading.measurement_config.theta_radians / 2.0

        for index_phi, p in enumerate(phi[0, :]):
            for index_theta, t in enumerate(theta[:, 0]):
                # ADD IF UPPER SPHERE + values
                # - on lower

                if _full_random:
                    _configured_reading.insert_reading(-100 + random.uniform(0, 1) * 200.0, p, t, index_phi,
                                                       index_theta)
                else:
                    if t > center:
                        _configured_reading.insert_reading(-80 + random.uniform(0, 1) * 40.0, p, t, index_phi,
                                                           index_theta)
                    else:
                        _configured_reading.insert_reading(80 + random.uniform(0, 1) * 40.0, p, t, index_phi,
                                                           index_theta)

        return _configured_reading

    @staticmethod
    def generate_random_half_sphere_reading(_full_random: bool = False) -> MRPReading.MRPReading:
        """
                Generate a half sphere reading with random field values and predefined meta-data.

                :param _full_random: Optional; if true each inserted datapoint is random in polarity and strength
                :type _full_random: bool

                :returns: a generated MRPReading with set meta-data
                :rtype: MRPReading.MRPReading

                """
        reading = MRPReading.MRPReading(None)
        reading.sensor_id = 0
        reading.measurement_config.configure_halfsphere()
        reading.measurement_config.sensor_distance_radius = 10
        reading.measurement_config.magnet_type = MRPMagnetTypes.MagnetType.N45_SPHERE_10

        return MRPSimulation.__generate_reading_data__(reading, _full_random)
    @staticmethod
    def generate_random_full_sphere_reading(_full_random: bool = False) -> MRPReading.MRPReading:
        """
        Generate a full sphere reading with random field values and predefined meta-data.

        :param _full_random: Optional; if true each inserted datapoint is random in polarity and strength
        :type _full_random: bool

        :returns: a generated MRPReading with set meta-data
        :rtype: MRPReading.MRPReading

        """
        reading = MRPReading.MRPReading(None)
        reading.sensor_id = 0
        reading.measurement_config.configure_fullsphere()
        reading.measurement_config.sensor_distance_radius = 10
        reading.measurement_config.magnet_type = MRPMagnetTypes.MagnetType.N45_SPHERE_10

        return MRPSimulation.__generate_reading_data__(reading, _full_random)

