#!/usr/bin/env python

from distutils.core import setup
import pathlib
import pkg_resources
import setuptools
import os

req_path = 'requirements.txt' # os.path.join(os.path.dirname(__file__), 'requirements.txt')
with pathlib.Path(req_path).open() as requirements_txt:
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

setup(name='MagneticReadoutProcessing',
      version='1.2.0',
      description='Process raw data from magnetometers',
      author='Marcel Ochsendorf',
      author_email='info@marcelochsendorf.com',
      url='https://github.com/LFB-MRI/MagnetCharacterization/',
      packages= ['MRP', 'MRPcli', 'MRPudpp', 'tests'],#setuptools.find_packages('src', exclude=['test'], include=['MRPcli']),
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
            'MRPCli = MRPcli.cli:run', # FOR python -m MRPcli.cli --help
            'MRPUdpp = MRPudpp.uddp:run'
          ]
      }
     )
