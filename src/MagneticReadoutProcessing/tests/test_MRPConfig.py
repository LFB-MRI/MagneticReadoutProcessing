from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import unittest
import configparser
import os

from MRP import MRPConfig

# TODO REWRITE TEST FOR CONFIG
class TestMPRConfig(unittest.TestCase):

    @unittest.skip
    def test_config_init(self):
        config = MRPConfig.MRPConfig(None)
        self.assertIsNotNone(config)

        assert (hasattr(config, 'MEASUREMENT_HORIZONTAL_RESOLUTION'))
        assert (hasattr(config, 'MEASUREMENT_VERTICAL_RESOLUTION'))
        assert (hasattr(config, 'MEASUREMENT_HORIZONTAL_AXIS_DEGREE'))
        assert (hasattr(config, 'MEASUREMENT_VERTICAL_AXIS_DEGREE'))

    @unittest.skip
    def test_config_load_default(self):
        config = MRPConfig.MRPConfig(None)
        config.load_defaults()
        self.assertIsNotNone(config)

    @unittest.skip
    def test_config_export(self):
        config = MRPConfig.MRPConfig(None)
        config.load_defaults()

        ret = config.get_as_dict()

        measurement = ret['MEASUREMENT']
        self.assertIsNotNone(measurement)

        self.assertTrue(measurement['HORIZONTAL_RESOLUTION'] == config.MEASUREMENT_HORIZONTAL_RESOLUTION)
        self.assertTrue(measurement['VERTICAL_RESOLUTION'] == config.MEASUREMENT_VERTICAL_RESOLUTION)
        self.assertTrue(measurement['HORIZONTAL_AXIS_DEGREE'] == config.MEASUREMENT_HORIZONTAL_AXIS_DEGREE)
        self.assertTrue(measurement['VERTICAL_AXIS_DEGREE'] == config.MEASUREMENT_VERTICAL_AXIS_DEGREE)

    @unittest.skip
    def test_config_configparser(self):
        CONFIG_FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       "assets/test_config_configparser.ini")
        print("config filepath: ", CONFIG_FILEPATH)
        IniConfig = configparser.ConfigParser()
        IniConfig.read(CONFIG_FILEPATH)

        # LOAD THE INIFILE USING THE MRPConfig class
        # THE values should be equal to the read values from IniConfig Instance
        config = MRPConfig.MRPConfig.load_from_ini(CONFIG_FILEPATH)
        ret = config.get_as_dict()
        measurement = ret['MEASUREMENT']
        self.assertTrue(measurement['HORIZONTAL_RESOLUTION'] == IniConfig['MEASUREMENT'].getint('HORIZONTAL_RESOLUTION', 18))
        self.assertTrue(measurement['VERTICAL_RESOLUTION'] == IniConfig['MEASUREMENT'].getint('VERTICAL_RESOLUTION', 18))
        self.assertTrue(measurement['HORIZONTAL_AXIS_DEGREE'] == IniConfig['MEASUREMENT'].getint('HORIZONTAL_AXIS_DEGREE', 18))
        self.assertTrue(measurement['VERTICAL_AXIS_DEGREE'] == IniConfig['MEASUREMENT'].getint('VERTICAL_AXIS_DEGREE', 18))

if __name__ == '__main__':
    unittest.main()
