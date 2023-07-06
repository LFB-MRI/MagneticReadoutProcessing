#!/usr/bin/env python

from distutils.core import setup

setup(name='MagneticReadoutProcessing',
      version='1.0',
      description='Python Distribution Utilities',
      author='Marcel Ochsendorf',
      author_email='info@marcelochsendorf.com',
      url='https://github.com/LFB-MRI/MagnetCharacterization/',
      packages=['MagneticReadoutProcessing',
                'MagneticReadoutProcessing.MRPAnalysis',
                'MagneticReadoutProcessing.MRPConfig',
                'MagneticReadoutProcessing.MRPReading',
                'MagneticReadoutProcessing.MRPHelpers'
                ],
     )