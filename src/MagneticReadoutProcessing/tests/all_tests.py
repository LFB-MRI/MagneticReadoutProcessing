#!/usr/bin/env python3
import unittest
from unittest import TestSuite
import os
import configparser



def load_tests(loader, tests, pattern):
    ''' Discover and load all unit tests in all files named ``*_test.py`` in ``./src/`` '''
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__)+'/test_config.ini')


    # add normal tests
    suite = TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('.', pattern='test_*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)

    # add hardware related tests
    if int(config['TESTCONFIG']['enable_hardware_required_tests']) > 0:
        for all_test_suite in unittest.defaultTestLoader.discover('.', pattern='hwtest_*.py'):
            for test_suite in all_test_suite:
                suite.addTests(test_suite)





    return suite

if __name__ == '__main__':
    unittest.main()