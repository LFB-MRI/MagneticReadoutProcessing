# Introduction

## Background and Motivation

### Low-Field MRI

### Shimming procedure

## Aim of this Thesis


## Structure



# State of the art

## Opensource projects

## Conceptual design

* etnwicklung eines hardware uns software framework zur einfachen aquirierung von Meagnetfelddaten
* analysetools und funktionen



# Usecases




# Unified Sensor


* ziel ist es einen low cost hallsensor-interface  zu entwickeln welcher möglichst
* universell
* verschienee sensoren abbilden kann
* mit verschienden magneten typen und formen nutzbar
* reproduzierbar
* 1d, 2d, 3d
* integration

## Sensor selection



 %%Implemented_digital_halleffect_sensors.csv%%


* for higher ranges analog sensoren nutzen welche jedoch eine aufwändigere schaltung erfodern
* datenblatte links ergänzen
* alle i2c in der regel, welches eine einfache integration  ermöglicht
* eingebauter temperatursensor ermöglicht temperaturkompensation
* conrad teslameter mit seperaten temperatursensor


## Mechanical Structure

* 3d druck toleranztest
* magnet halterung mit kraftloser arretierung
* motoren und andere unter umstaänden magnetische teile in der nähe des sensors
* nylon schrauben, 3d druck, 3d gedruckte klemmverbindungen
* später rausrechnen durch kalibierung

## Electrical Interface

* usb, ethernet
* pps input output
* multiplexer for i2c sensors alredy implemented


## Firmware

* automatic sensor detation ablaufdiagramm erst nach i2c geräte scannen dann analog versuchen
* serial cli support for manual mode
* sync impulse => 1 mastersensor als taktqelle
* interene mittelung und speichern der werte im buffer ringubber welcher bei jedem sync impuls neu belegt wird
* 2. core übernimmt mittelung und auswetung
* was durch den user implementiert werden muss klasse


### User-Interface

%%Sensors_(+cli).png%%

%%Query_sensors_b_value_using_(+cli).png%%


* einfache bedienung durch nutzer auch ohne weitere software
* configuration
* debugging

## Sensor Syncronsisation

## Example Sensors

*anbei werden drei erschienee sensoren für unterschiedliche anwedungfälle
* tablle statisch dynamisch



### 1D: Single Sensor

%%1D_sensor_contrsuction_with_universal_magnet_mount.png%%

* einfachster aufbau rp pico + sensor


### 1D: Dual Sensor

* gleicher abstand zwei gleicher sensoren
* schnelle erkennung der plarisationsebene ggf offset vom mittelpunkt dieser




### Full-Sphere

%%Full-Sphere_sensor_implementation_using_two_Nema17_stepper_motors_in_a_polar_coordinate_system.png%%

* komplexester aufbau sensor + mechanik
* polar mechanisches system
* full sphere sensor

### Integration of an Professional Teslameter

* einfach anbindung professioneller teslameter
* Voltkraft





# Software readout framework


%%MRPlib_COMPLETE_FLOW.png%%


## Library requirements



### Concepts

* beispiele für projekte welche nur einzelne schnritte implementieren
* so kann man sich auf die implementierung 

### User interaction points


* grafik zeigen
* einzelne module erleutern

 
#### HAL

* aufbau hal im grunde wird nur ein die commandos an das sensor cli weitergegeben
* alle sensoren implementieren mehr oder weniger die gleichen befehle
* hal gibt nur weiter und ist "dumm"

#### Visualisation


### Export

* format import export
* matlab

#### Meta-Data





### Multi-Sensor setup

At the current state of implementation, it is only possible to detect and use sensors that are directly connected to the (+pc) with the library. This has the disadvantage that there must always be a physical connection. This can make it difficult to install multiple sensors in measurement setups where space or cable routing options are limited. To make sensors connected to a small `remote` (+pc) available on the network, the `Proxy`\ref{MRPlib_Proxy_Module.png} module has been developed. This can be a single board computer (e.g. a Raspberry Pi). The small footprint and low power consumption make it a good choice. It can also be used in a temperature chamber. The approach of implementing this via a (+rest) interface also offers the advantage that several measurements or experiments can be recorded at the same time with the sensors.

%%MRPlib_Proxy_Module.png%%

Another application example is when sensors are physically separated or there are long distances between them.
By connecting several sensors via the proxy module, it is possible to link several instances and all sensors available in the network are available to the control (+pc).

%%mrp_proxy_multi.png%%

The figure \ref{mrp_proxy_multi.png} shows the modified `multi-proxy - multi-sensor` topology. Here, both proxy instances do not communicate directly with the control (+pc), but `remote (+pc) #2` is connected to `remote (+pc) #1`. This is then visible as a sensor opposite the Control (+pc), even if there are several proxy instances behind it.


#### Network-Proxy

The figure \ref{MRPlib_Proxy_Module.png} shows the separation of the various (+hal) instances, which communicate with the physically connected sensors on the `remote`-(+pc) and the `control`-(+pc) side, which communicates with the remote side via the network. 
For the user, nothing changes in the procedure for setting up a measurement. The proxy application must always be started\ref{lst:mrpcli_proxy_start} on the `remote` (+pc) side.


```bash {#lst:mrpcli_proxy_start caption="MRPproxy usage to enable local sensor usage over network"}
# START PROXY INSTNACE WITH TWO LOCALLY CONNECTED SENSORS
$ python3 mrpproxy.py proxy launch /dev/ttySENSOR_A /dev/ttySENSOR_B # add another proxy instance http://proxyinstance_2.local for multi-sensor, multi-proxy chain
Proxy started. http://remotepc.local:5556/
PRECHECK: SENSOR_HAL: 1337 # SENSOR A FOUND
PRECHECK: SENSOR_HAL: 4242 # SENSOR B FOUND
Terminate  Proxy instance [y/N] [n]: 
```

After the proxy instance has been successfully started, it is optionally possible to check the status via the (+rest) interface:\ref{lst:mrpcli_config_rest}

```bash {#lst:mrpcli_config_rest caption="MRPproxy REST enpoiint query examples"}
    # GET PROXY STATUS
    $ wget http://proxyinstance.local:5556/proxy/status
    {
    "capabilities":[
      "static",
      "axis_b",
      "axis_x",
      "axis_y",
      "axis_z",
      "axis_temp",
      "axis_stimestamp"
   ],
   "commands":[
      "status",
      "initialize",
      "disconnect",
      "combinedsensorcnt",
      "sensorcnt",
      "readsensor",
      "temp"
   ]

   # RUN A SENSOR COMMAND AND GET THE TOTAL SENSOR COUNT
   $ wget http://proxyinstance.local:5556/proxy/command?cmd=combinedsensorcnt
   {
   "output":[
      "2"
   ]
}
}
```

The query result shows that the sensors are connected correctly and that their capabilites have also been recognised correctly. To be able to configure a measurement on the other, only the (+ip) address or host name of the remote (+pc) is required\ref{lst:mrpcli_config_using_rpc}. 


```bash {#lst:mrpcli_config_using_rpc caption="MRPcli usage example to connect with a network sensor"}
# CONFIGURE MEASUREMENT JOB USING A PROXY INSTANCE
$ MRPcli config setupsensor testcfg --path http://proxyinstance.local:5556
> remote sensor connected: True using proxy connection:
> http://proxyinstance.local:5556 with 1 local sensor connected
```


#### Sensor Syncronisation




Another important aspect when using several sensors via the proxy system is the synchronisation of the measurement intervals between the sensors. 
Individual sensor setups do not require any additional synchronisation information, as this is communicated via the (+usb) interface.
If several sensors are connected locally, they can be connected to each other via their sync input using short cables. One sensor acts as the central clock (see chapter \ref{sensor-syncronsisation}).
this no longer works for long distances and the syncronisation must be made via the network connection. 

If time-critical synchronisation is required, (+ptp) and (+pps) output functionality can be used on many single-board computers, such as the RaspberryPi Compute Module.


* was ptp, bild pps output
* alle clients über ptp verbunden
* dso bild von jeff gerling über rpi4 ptp


#### Command-Router

* nummerieierung zuerst lokale sensoren dann weitere proxy sensoren
* commando templating



### Examples



# Usability improvements


## Command Line Interface

%%MRP_(+cli)_output_to_configure_a_new_measurement.png%%

In the first version of this library, the user had to write his own Python scripts even for short measurement and visualisation tasks. However, this was already time-consuming for reading out a sensor and configuring the measurement parameters and metadata and quickly required more than 100 lines of new Python code. Although such examples are provided in the documentation, it must be possible for programming beginners in particular to use them. To simplify these tasks, a (+cli)\ref{example_measurement_analysis_pipeline.png} was implemented around this library, which is then also supplied as a fixed component. This (+cli) implements the following functionalities:

* Detection of connected sensors
* Configuration of measurement series
* Recording of measured values from stored measurement series
* Simple commands for checking recorded measurement series and their data.

Thanks to this functionality of the (+cli), it is now possible to connect a sensor to the (+pc), configure a measurement series with it and run it at the end. The result is then an exported file with the measured values.
These can then be read in again with the library and processed further. The following\ref{lst:mrpcli_config_run} bash code shows this procedure in detail:

```bash {#lst:mrpcli_config_run caption="CLI example for configuring a measurement run"}
# CLI EXAMPLE FOR CONFIGURING A MEASUREMENT RUN
## CONFIGURE THE SENSOR TO USE
$ MRPcli config setupsensor testcfg
> 0 - Unified Sensor 386731533439 - /dev/cu.usbmodem3867315334391
> Please select one of the found sensors [0]:
> sensor connected: True 1243455
## CONFIGURE THE MEASUREMENT
$ MRPcli config setup testcfg
> CONFIGURE testcfg
> READING-NAME: [testreading]: testreading
> OUTPUT-FOLDER [/cli/reading]: /tmp/reading_folder_path
> NUMBER DATAPOINTS: [1]: 10
> NUMBER AVERAGE READINGS PER DATAPOINT: [1]: 100
# RUN THE CONFIGURED MEASUREMENT
$ MRPcli measure run
> STARTING MEASUREMENT RUN WITH FOLLOWING CONFIGS: ['testcfg']
> config-test: OK
> sensor-connection-test: OK
> START MEASUREMENT CYCLE
> sampling 10 datapoints with 100 average readings
> SID:0 DP:0 B:47.359mT TEMP:23.56
> ....
> dump_to_file testreading_ID:525771256544952_SID:0_MAG:N45_CUBIC_12x12x12.mag.json
```

## Programmable data processing pipeline

%%example_measurement_analysis_pipeline.png%%

\ref{example_measurement_analysis_pipeline.png}

* datenanalyse für nicht programmieruer
* automatisierter aufbau der call-tree
* mit typcheck
* alle funktionen mit bestimmer signtur werden automatisch aus globals geladen und stehen nutzer zur verfühung


```yaml {caption="Example User Defined Processing Pipeline"}
stage import_readings:
  function: import_readings
  parameters:
    IP_input_folder: ./readings/fullsphere/
    IP_file_regex: 360_(.)*.mag.json

stage import_bias_reading:
  function: import_readings
  parameters:
    IP_input_folder: ./readings/fullsphere/
    IP_file_regex: bias_reading.mag.json

stage apply_bias_offset:
  function: apply_sensor_bias_offset
  parameters:
    bias_readings: stage import_bias_reading
    readings_to_calibrate: stage import_readings

stage apply_temp_compensation:
  function: apply_temperature_compensation
  parameters:
    readings_to_calibrate: stage import_readings

stage plot_normal_bias_offset:
  function: plot_readings
  parameters:
    readings_to_plot: stage apply_temp_compensation
    IP_export_folder: ./readings/fullsphere/plots/
    IP_plot_headline_prefix:  Sample N45 12x12x12 magnets calibrated

stage export_readings:
  function: export_readings
  parameters:
    readings_to_plot: stage apply_temp_compensation
    IP_export_folder: ./readings/fullsphere/plots/
```




## Tests

Software tests in libraries offer numerous advantages for improving quality and efficiency. Firstly, they enable the identification of errors and vulnerabilities before software is published as a new version. This significantly improves the reliability of library applications. Tests also ensures consistent and reliable performance, which is particularly important when libraries are used by different users and for different usecases.

%%MRP_library_test_results_for_different_submodules_executed_in_PyCharm_(+ide).png%%

During the development of the library, test cases were also created for all important functionalities and use cases. The test framework `PyTest`[@PyTest] was used for this purpose, as it offers direct integration in most (+ide)s (see \ref{MRP_library_test_results_for_different_submodules_executed_in_PyCharm_(+ide).png}) and also because it provides detailed and easy-to-understand test reports as output in order to quickly identify and correct errors. It also allows to tag tests, which is useful for grouping tests or excluding certain tests in certain build environment scenarios.
Since all intended use cases were mapped using the test cases created, the code of the test cases could later be used in slightly simplified variants\ref{lst:pytest_example_code} as examples for the documentation. 


```python {#lst:pytest_example_code caption="Example pytest class for testing MRPReading module functions"}
# $ cat test_mrpreading.py
class TestMPRReading(unittest.TestCase):
  # PREPARE A INITIAL CONFIGURATION FILE FOR ALL FOLLOWING TEST CASES IN THIS FILE
  def setUp(self) -> None:
      self.test_folder: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
      self.test_file:str = os.path.join(self.import_export_test_folderpath, "tmp")

  def test_matrix(self):
      reading: MRPReading = MRPSimulation.generate_reading()
      matrix: np.ndarray = reading.to_numpy_matrix()
      n_phi: float = reading.measurement_config.n_phi
      n_theta: float = reading.measurement_config.n_theta
      # CHECK MATRIX SHAPE
      self.assertTrue(matrix.shape != (n_theta,))
      self.assertTrue(len(matrix.shape) <= n_phi))

  def test_export_reading(self) -> None:
      reading: MRPReading = self.test_reading_init()
      self.assertIsNotNone(reading)
      # EXPORT READING TO A FILE
      reading.dump_to_file(self.test_file)

  def test_import_reading(self):
      # CREATE EMPTY READING
      reading_imported:MRPReading = MRPReading.MRPReading(None)
      # LOAD READING FROM FILE
      reading_imported.load_from_file(self.test_file)
      # CHECK IF ENTRIES ARE POPULATED
      self.assertIsNotNone(reading_imported.additional_data)
      self.assertIsNotNone(reading_imported.data)
```


One problem, however, is the parts of the library that require direct access to external hardware. These are, for example, the `MRPHal` and `MRPHalRest` modules, which are required to read out sensors connected via the network.
Two different approaches were used here. In the case of local development, the test runs were carried out on a (+pc) that can reach the network hardware and thus the test run could be carried out with real data.

In the other scenario, the tests are to be carried out before a new release in the repository on the basis of `Github Actions`[@GithubActions]. Here there is the possibility to host local runner software, which then has access to the hardware, but then a (+pc) must be permanently available for this task. Instead, the hardware sensors were simulated by software and executed via virtualisation on the systems provided by `Github Actions`[@GithubActions].


## Package distribution

One important point that improves usability for users is the simple installation of the library.
As it was created in the Python programming language, there are several public package directories where users can provide their software modules. Here, `PyPi`[@PyPI]\ref{MagneticReadoutProcessing_library_hosted_on_PyPi.png}[@MagneticReadoutProcessingPyPI] is the most commonly used package directory and offers direct support for the package installation programm (+pip)\ref{lst:setup_lib_with_pip}.

%%MagneticReadoutProcessing_library_hosted_on_PyPi.png%%

In doing so, (+pip) not only manages possible package dependencies, but also manages the installation of different versions of a package. In addition, the version compatibility is also checked during the installation of a new package, which can be resolved manually by the user in the event of conflicts.

```bash {#lst:setup_lib_with_pip caption="Bash commands to install the MagneticReadoutProcessing library using pip"}
# https://pypi.org/project/MagneticReadoutProcessing/
# install the latest version
$ pip3 install MagneticReadoutProcessing
# install the specific version 1.4.0
$ pip3 install MagneticReadoutProcessing==1.4.0
```

To make the library compatible with the package directory, Python provides separate installation routines that build a package in an isolated environment and then provide an installation `wheel` archive. This can then be uploaded to the package directory.

Since the library requires additional dependencies (e.g. `numpy`, `matplotlib`), which cannot be assumed to be already installed on the target system, these must be installed prior to the actual installation. These can be specified in the library installation configuration `setup.py`\ref{lst:setup_py_req} for this purpose.

```python {#lst:setup_py_req caption="setup.py with dynamic requirement parsing used given requirements.txt"}
# dynamic requirement loading using 'requirements.txt'
req_path = './requirements.txt'
with pathlib.Path(req_path).open() as requirements_txt:
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

setup(name='MagneticReadoutProcessing',
      version='1.4.3',
      url='https://github.com/LFB-MRI/MagnetCharacterization/',
      packages= ['MRP', 'MRPcli', 'MRPudpp', 'MRPproxy'],
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
            'MRPCli = MRPcli.cli:run',
            'MRPUdpp = MRPudpp.uddp:run',
            'MRPproxy = MRPproxy.mrpproxy:run'
          ]
      }
    )
```

To make the (+cli) scripts written in Python easier for the user to execute without having to use the `python3` prefix. This has been configured in the installation configuration using the `entry_points` option, and the following commands are available to the user:

* `MRPcli --help` instead of `python3 cli.py --help`
* `MRPudpp --help` instead of `python3 udpp.py --help`
* `MRPproxy --help` instead of `python3 proxy.py --help`

In addition, these commands are available globally in the system without the terminal shell being located in the library folder.



### Documentation


In order to provide comprehensive documentation for the enduser, the source code was documented using Python-`docstrings`[@PythonDocstringReference] and the Python3.5 type annotations:

* Function description
* Input parameters - using `param` and `type`
* Return value - using `returns`, `rtype`

The use of type annotations also simplifies further development, as modern (+ide)s can more reliably display possible methods to the user as an assistance.\ref{pydocstring}

```python {#lst:pydocstring caption="Python docstring example"}
    # MRPDataVisualisation.py - example docstring
    def plot_temperature(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None, _unit: str = "degree C") -> str:
        """
        Plots a temperature plot of the reading data as figure
        :param _readings: readings to plot
        :type _readings: list(MRPReading.MRPReading)
        :param _title: Title text of the figure, embedded into the head
        :type _title: str
        :param _filename: export graphic to an given absolute filepath with .png
        :type _filename: str
        :returns: returns the abs filepath of the generated file
        :rtype: str
        """
        if _readings is None or len(_readings) <= 0:
            raise MRPDataVisualizationException("no readings in _reading given")
        num_readings = len(_readings)
        # ...
```


Since 'docstrings' only document the source code, but do not provide simple how-to-use instructions, the documentation framework `Sphinx`[@SphinxDocumentation] was used for this purpose. This framework makes it possible to generate (+html) or (+pdf) documentation from various source code documentation formats, such as the used `docstrings`.
These are converted into a Markdown format in an intermediate step and this also allows to add further user documentation such as examples or installation instructions.

In order to make the documentation created by `Sphinx` accessible to the user, there are, as with the package management by `PyPi` services, which provide Python library documentation online.

%%MagneticReadoutProcessing_documentation_hosted_on_ReadTheDocs.png%%

Once the finished documentation has been generated from static (+html) files, it is stored in the project repository. Another publication option is to host the documentation via online services such as `ReadTheDocs`[@ReadTheDocs], where users can make documentation for typical software projects available to others.

The documentation has also been uploaded for `ReadTheDocs`[@MagneticReadoutProcessingReadTheDocs] and linked in the repository and on the overview page\ref{MagneticReadoutProcessing_documentation_hosted_on_ReadTheDocs.png} on `PyPi`.

The process of creating and publishing the documentation has been automated using `GitHub Actions`[@GithubActions], so that it is always automatically kept up to date with new features.





# Evaluation


## Prequesites for evaluation

%%testmagnets_in_holder.png%%

## Evaluation confiugration

### Sensor readout

### Processing pipeline

## Test scenarios

## Results









# Conclusion and dicussion
## Conclusion

## Problems

## Outlook

* magfield camera


