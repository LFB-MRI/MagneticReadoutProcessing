import configparser

class MRPConfig():
    """ Stores basic metadata regarding a reading/measurement, all attributes regarding MEASUREMENT are required in order to configure a MRPReading instance"""

    # [HARDWARE]
    HARDWARE_GCODE_SERIAL_INTERFACE = 'socket://magpi.local:10001'
    HARDWARE_READOUTUNIT_SERIAL_INTERFACE = 'socket://magpi.local:10003'
    HARDWARE_AXIS_LIMIT_HORIZONTAL_MIN = -4
    HARDWARE_AXIS_LIMIT_HORIZONTAL_MAX = 355
    HARDWARE_AXIS_LIMIT_VERTICAL_MIN = -4
    HARDWARE_AXIS_LIMIT_VERTICAL_MAX = 51
    HARDWARE_READOUTUNIT_USER_ALTERNATIVE_UART_PROTOCOL = 1 # 0=protobuf 1=serial
    # [MEASUREMENT]
    MEASUREMENT_HORIZONTAL_AXIS_DEGREE = 360  # REQUIRED
    MEASUREMENT_VERTICAL_AXIS_DEGREE = 90  # REQUIRED
    MEASUREMENT_HORIZONTAL_RESOLUTION = MEASUREMENT_HORIZONTAL_AXIS_DEGREE/2/10 #REQUIRED
    MEASUREMENT_VERTICAL_RESOLUTION = MEASUREMENT_VERTICAL_AXIS_DEGREE/10 #REQUIRED


    
    
    
    MEASUREMENT_READOUT_AVERAGING_POINT = 1
    MEASUREMENT_SENSOR_MAGNET_DISTANCE = 40
    MEASUREMENT_SENSOR_Z_AXIS_INVERTED = 0

    MEASUREMENT_SENSOR_USE_Z_VALUE_AS_B = 0
    # [DEBUG]
    DEBUG_USE_SIMULATED_HARDWARE = 1
    DEBUG_MOVE_TO_AXIS_LIMITS = 1
    DEBUG_PERFORM_READ_SENSOR_TEST = 1
    DEBUG_DISABLE_MOTOR_MOVEMENTS = 1

    @staticmethod
    def load_from_ini(_config_file_path: str = None):
        """
        loads a given .ini file and parses the entries.
        If valid entries are present, these values will be overwritten

        :param _config_file_path: absolute filepath to .ini file with config overwrite entries. See config.ini.EXAMPLE
        :type _config_file_path: str

        """
        IniConfig = configparser.ConfigParser()
        IniConfig.read(_config_file_path)

        return MRPConfig(IniConfig)



    def __init__(self, _config: configparser = None):
        """
        Inits the config holder class and:
        A) loads default values if _config is None
        B) uses a configparser instance to load valid entries in

        :param _config: Optional; load entries from config parser
        :type _config: configparser

        """

        if _config is not None:
            # [HARDWARE]
            if 'HARDWARE' in _config:
                self.HARDWARE_GCODE_SERIAL_INTERFACE = _config['HARDWARE'].get('GCODE_SERIAL_INTERFACE', self.HARDWARE_GCODE_SERIAL_INTERFACE)
                self.HARDWARE_READOUTUNIT_SERIAL_INTERFACE = _config['HARDWARE'].get('READOUTUNIT_SERIAL_INTERFACE', self.HARDWARE_READOUTUNIT_SERIAL_INTERFACE)
                self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MIN = _config['HARDWARE'].getint('AXIS_LIMIT_HORIZONTAL_MIN',self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MIN)
                self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MAX = _config['HARDWARE'].getint('AXIS_LIMIT_HORIZONTAL_MAX', self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MAX)
                self.HARDWARE_AXIS_LIMIT_VERTICAL_MIN = _config['HARDWARE'].getint('AXIS_LIMIT_VERTICAL_MIN', self.HARDWARE_AXIS_LIMIT_VERTICAL_MIN)
                self.HARDWARE_AXIS_LIMIT_VERTICAL_MAX = _config['HARDWARE'].getint('AXIS_LIMIT_VERTICAL_MAX', self.HARDWARE_AXIS_LIMIT_VERTICAL_MAX)
                self.HARDWARE_READOUTUNIT_USER_ALTERNATIVE_UART_PROTOCOL = _config['HARDWARE'].getboolean('READOUTUNIT_USER_ALTERNATIVE_UART_PROTOCOL', self.HARDWARE_READOUTUNIT_USER_ALTERNATIVE_UART_PROTOCOL)
            # [MEASUREMENT]
            if 'MEASUREMENT' in _config:
                self.MEASUREMENT_HORIZONTAL_RESOLUTION = _config['MEASUREMENT'].getint('HORIZONTAL_RESOLUTION', self.MEASUREMENT_HORIZONTAL_RESOLUTION)
                self.MEASUREMENT_VERTICAL_RESOLUTION = _config['MEASUREMENT'].getint('VERTICAL_RESOLUTION', self.MEASUREMENT_VERTICAL_RESOLUTION)
                self.MEASUREMENT_READOUT_AVERAGING_POINT = _config['MEASUREMENT'].getint('READOUT_AVERAGING_POINT', self.MEASUREMENT_READOUT_AVERAGING_POINT)
                self.MEASUREMENT_SENSOR_MAGNET_DISTANCE = _config['MEASUREMENT'].getint('SENSOR_MAGNET_DISTANCE', self.MEASUREMENT_SENSOR_MAGNET_DISTANCE)
                self.MEASUREMENT_SENSOR_Z_AXIS_INVERTED = _config['MEASUREMENT'].getboolean('SENSOR_Z_AXIS_INVERTED', self.MEASUREMENT_SENSOR_Z_AXIS_INVERTED)
                self.MEASUREMENT_HORIZONTAL_AXIS_DEGREE = _config['MEASUREMENT'].getint('HORIZONTAL_AXIS_DEGREE', self.MEASUREMENT_HORIZONTAL_AXIS_DEGREE)
                self.MEASUREMENT_VERTICAL_AXIS_DEGREE = _config['MEASUREMENT'].getint('VERTICAL_AXIS_DEGREE', self.MEASUREMENT_VERTICAL_AXIS_DEGREE)
                self.MEASUREMENT_SENSOR_USE_Z_VALUE_AS_B = _config['MEASUREMENT'].getboolean('SENSOR_USE_Z_VALUE_AS_B', self.MEASUREMENT_SENSOR_USE_Z_VALUE_AS_B)


            # [DEBUG]
            if 'DEBUG' in _config:
                self.DEBUG_USE_SIMULATED_HARDWARE = _config['DEBUG'].getboolean('USE_SIMULATED_HARDWARE', self.DEBUG_USE_SIMULATED_HARDWARE)
                self.DEBUG_MOVE_TO_AXIS_LIMITS = _config['DEBUG'].getboolean('MOVE_TO_AXIS_LIMITS', self.DEBUG_MOVE_TO_AXIS_LIMITS)
                self.DEBUG_PERFORM_READ_SENSOR_TEST = _config['DEBUG'].getboolean('PERFORM_READ_SENSOR_TEST', self.DEBUG_PERFORM_READ_SENSOR_TEST)
                self.DEBUG_DISABLE_MOTOR_MOVEMENTS = _config['DEBUG'].getboolean('DISABLE_MOTOR_MOVEMENTS', self.DEBUG_DISABLE_MOTOR_MOVEMENTS)

        else:
            self.load_defaults()

    def get_as_dict(self) -> dict:
        """
        returns the current config as dict.
        This dict is also stored in a exported MRPReading

        :returns: the current config
        :rtype: dict

        """
        return dict({
            'HARDWARE': dict({
                'GCODE_SERIAL_INTERFACE': self.HARDWARE_GCODE_SERIAL_INTERFACE,
                'READOUTUNIT_SERIAL_INTERFACE': self.HARDWARE_READOUTUNIT_SERIAL_INTERFACE,
                'AXIS_LIMIT_HORIZONTAL_MIN': self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MIN,
                'AXIS_LIMIT_HORIZONTAL_MAX': self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MAX,
                'AXIS_LIMIT_VERTICAL_MIN': self.HARDWARE_AXIS_LIMIT_VERTICAL_MIN,
                'AXIS_LIMIT_VERTICAL_MAX': self.HARDWARE_AXIS_LIMIT_VERTICAL_MAX,
                'READOUTUNIT_USER_ALTERNATIVE_UART_PROTOCOL': self.HARDWARE_READOUTUNIT_USER_ALTERNATIVE_UART_PROTOCOL
            }),
            'MEASUREMENT': dict({
                'HORIZONTAL_RESOLUTION': self.MEASUREMENT_HORIZONTAL_RESOLUTION,
                'VERTICAL_RESOLUTION': self.MEASUREMENT_VERTICAL_RESOLUTION,
                'READOUT_AVERAGING_POINT': self.MEASUREMENT_READOUT_AVERAGING_POINT,
                'SENSOR_MAGNET_DISTANCE': self.MEASUREMENT_SENSOR_MAGNET_DISTANCE,
                'SENSOR_Z_AXIS_INVERTED': self.MEASUREMENT_SENSOR_Z_AXIS_INVERTED,
                'HORIZONTAL_AXIS_DEGREE': self.MEASUREMENT_HORIZONTAL_AXIS_DEGREE,
                'VERTICAL_AXIS_DEGREE': self.MEASUREMENT_VERTICAL_AXIS_DEGREE,
                'SENSOR_USE_Z_VALUE_AS_B': self.MEASUREMENT_SENSOR_USE_Z_VALUE_AS_B
            }),
            'DEBUG': dict({
                'USE_SIMULATED_HARDWARE': self.DEBUG_USE_SIMULATED_HARDWARE,
                'MOVE_TO_AXIS_LIMITS': self.DEBUG_MOVE_TO_AXIS_LIMITS,
                'PERFORM_READ_SENSOR_TEST': self.DEBUG_PERFORM_READ_SENSOR_TEST,
                'DISABLE_MOTOR_MOVEMENTS': self.DEBUG_DISABLE_MOTOR_MOVEMENTS
            })
        })


    def load_defaults(self):
        """
        Set all values to default.

        """
        # [HARDWARE]
        self.HARDWARE_GCODE_SERIAL_INTERFACE = "socket://127.0.0.1:10001"
        self.HARDWARE_READOUTUNIT_SERIAL_INTERFACE = "socket://127.0.0.1:10003"
        self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MIN = -4
        self.HARDWARE_AXIS_LIMIT_HORIZONTAL_MAX = 1062
        self.HARDWARE_AXIS_LIMIT_VERTICAL_MIN = -4
        self.HARDWARE_AXIS_LIMIT_VERTICAL_MAX = 106
        self.READOUTUNIT_USER_ALTERNATIVE_UART_PROTOCOL = False
        # [MEASUREMENT]
        self.MEASUREMENT_HORIZONTAL_RESOLUTION = 36
        self.MEASUREMENT_VERTICAL_RESOLUTION = 18
        self.MEASUREMENT_READOUT_AVERAGING_POINT = 1
        self.MEASUREMENT_SENSOR_MAGNET_DISTANCE = 40
        self.MEASUREMENT_SENSOR_Z_AXIS_INVERTED = 1
        self.MEASUREMENT_HORIZONTAL_AXIS_DEGREE = 360
        self.MEASUREMENT_VERTICAL_AXIS_DEGREE = 180
        self.MEASUREMENT_SENSOR_USE_Z_VALUE_AS_B = True
        # [DEBUG]
        self.DEBUG_USE_SIMULATED_HARDWARE = False
        self.DEBUG_MOVE_TO_AXIS_LIMITS = False
        self.DEBUG_PERFORM_READ_SENSOR_TEST = False
        self.DISABLE_MOTOR_MOVEMENTS = False
