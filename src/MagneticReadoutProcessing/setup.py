#!/usr/bin/env python

from distutils.core import setup
import pathlib
import pkg_resources
import setuptools

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

setup(name='MagneticReadoutProcessing',
      version='1.0',
      description='Process raw data from magnetometers',
      author='Marcel Ochsendorf',
      author_email='info@marcelochsendorf.com',
      url='https://github.com/LFB-MRI/MagnetCharacterization/',
      packages=['MagneticReadoutProcessing'],
      install_requires=install_requires #parse_requirements('requirements.txt', session='hack')
     )