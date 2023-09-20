from fix_import import __fix_import__fix_import
__fix_import__fix_import()

import math
import numpy as np
import pytest
import unittest
import random

from MRP import MRPMagnetTypes




import os
class TestMRPMagnetTypes(unittest.TestCase):

    # PREPARE A INITIAL CONFIGURATION FILE
    def setUp(self) -> None:
        pass

    def test_magnet_type_cubic_12(self):
        magnet = MRPMagnetTypes.MagnetType.N45_CUBIC_12x12x12

        self.assertEqual(magnet.get_height(), 12)
        self.assertEqual(magnet.get_dimension(), (12,12,12))
        self.assertFalse(magnet.is_invalid())
        self.assertFalse(magnet.is_cylindrical())
        self.assertTrue(magnet.is_cubic())

    def test_magnet_type_cylinder_5x10(self):
        # CONVERSION TEST
        cy = MRPMagnetTypes.MagnetType.N45_CYLINDER_5x10.to_int()
        magnet = MRPMagnetTypes.MagnetType.from_int(cy)
        dim = magnet.get_dimension()
        self.assertEqual(dim, (5, 10, 0))


        h = magnet.get_height()
        self.assertEqual(h, 10)

        self.assertFalse(magnet.is_invalid())
        self.assertTrue(magnet.is_cylindrical())
        self.assertFalse(magnet.is_cubic())


    def test_magnet_type_invalid(self):
        magnet = MRPMagnetTypes.MagnetType.from_int(-1)
        self.assertIsNone(magnet)

        magnet = MRPMagnetTypes.MagnetType.from_int(0)

        self.assertTrue(magnet.is_invalid())
        self.assertFalse(magnet.is_cylindrical())
        self.assertFalse(magnet.is_cubic())

        with self.assertRaises(MRPMagnetTypes.MRPMagnetTypeException):
            magnet.get_height()

        with self.assertRaises(MRPMagnetTypes.MRPMagnetTypeException):
            magnet.get_dimension()


if __name__ == '__main__':
    unittest.main()
