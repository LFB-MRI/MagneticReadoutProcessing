import pytest
import unittest

from MagneticReadoutProcessing import MRPConfig
from MagneticReadoutProcessing import MRPReading
import configparser
import os
class TestMPRReading(unittest.TestCase):
    def test_reading_init(self):
        reading = MRPReading.MRPReading(None)
        self.assertIsNotNone(reading)



if __name__ == '__main__':
    unittest.main()
