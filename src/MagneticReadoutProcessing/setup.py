#!/usr/bin/env python

from distutils.core import setup
import pathlib
import pkg_resources


req_path = 'requirements.txt' # os.path.join(os.path.dirname(__file__), 'requirements.txt')
with pathlib.Path(req_path).open() as requirements_txt:
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

setup(name='MagneticReadoutProcessing',
      version='1.8.0',
      license='Apache 2',
      description='This library was created for the Low-Field MRI project and allows processing of data measured by magnetic field sensors. The focus is on visualization, followed by the provision of simple interfaces to work with this data. In general its possible to use this lib on all kinds of sensor data.',
      author='Marcel Ochsendorf',
      author_email='info@marcelochsendorf.com',
      url='https://github.com/LFB-MRI/MagnetCharacterization/',
      packages= ['MRP', 'MRPcli', 'MRPudpp', 'MRPproxy'],
      install_requires=install_requires,
      include_package_data=True,
      package_data={"": ["**/*.mag.json", "**/*.yaml", "**/*.html", "**/*.js", "**/*.css", "**/*.md", "**/*.json", "**/*.ts", "**/*.xml"]},
      entry_points={
          'console_scripts': [
            'MRPCli = MRPcli.cli:run', # FOR python -m MRPcli.cli --help
            'MRPUdpp = MRPudpp.uddp:run',
            'MRPproxy = MRPproxy.mrpproxy:run'
          ]
      }
     )
