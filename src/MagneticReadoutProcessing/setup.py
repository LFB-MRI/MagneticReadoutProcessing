#!/usr/bin/env python

from distutils.core import setup

setup(name='MagneticReadoutProcessing',
      version='1.0',
      description='Process raw data from magnetometers',
      author='Marcel Ochsendorf',
      author_email='info@marcelochsendorf.com',
      url='https://github.com/LFB-MRI/MagnetCharacterization/',
      packages=['MagneticReadoutProcessing'],
      install_requires=['wheel', 'magpylib', 'numpy', 'matplotlib']
     )