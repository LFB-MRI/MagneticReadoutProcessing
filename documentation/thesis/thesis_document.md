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


### (+cli)) Interface

%%Sensors_CL-Interface.png%%

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

The graphic \ref{mrp_proxy_multi.png} shows the modified `multi-proxy - multi-sensor` topology. Here, both proxy instances do not communicate directly with the control (+pc), but `remote (+pc) #2` is connected to `remote (+pc) #1`. This is then visible as a sensor opposite the Control (+pc), even if there are several proxy instances behind it.


#### Network-Proxy

The graphic \ref{MRPlib_Proxy_Module.png} shows the separation of the various (+hal) instances, which communicate with the physically connected sensors on the `remote`-(+pc) and the `control`-(+pc) side, which communicates with the remote side via the network. 
For the user, nothing changes in the procedure for setting up a measurement. The proxy application must always be started on the `remote` (+pc) side. 


```bash
    # START PROXY INSTNACE WITH TWO LOCALLY CONNECTED SENSORS
    $ python3 mrpproxy.py proxy launch /dev/ttySENSOR_A /dev/ttySENSOR_B # add another proxy instance http://proxyinstance_2.local for multi-sensor, multi-proxy chain
    Proxy started. http://0.0.0.0:5556/
    PRECHECK: SENSOR_HAL: 1337 # SENSOR A FOUND
    PRECHECK: SENSOR_HAL: 4242 # SENSOR B FOUND
    Terminate  [Y/n] [y]: 
```

After the proxy instance has been successfully started, it is optionally possible to check the status via the (+rest) interface:

```bash
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

The query result shows that the sensors are connected correctly and that their capabilites have also been recognised correctly. To be able to configure a measurement on the other, only the (+ip) address or host name of the remote (+pc) is required:


```bash
  # CONFIGURE MEASUREMENT JOB USING A PROXY INSTANCE
  $ python3 mrpproxy.py proxy launch /dev/ttySENSOR_A /dev/ttySENSOR_B
```


#### Sensor Syncronisation




Another important aspect when using several sensors via the proxy system is the synchronisation of the measurement intervals between the sensors. 
Individual sensor setups do not require any additional synchronisation information, as this is communicated via the (+usb) interface.
If several sensors are connected locally, they can be connected to each other via their sync input using short cables. One sensor acts as the central clock (see chapter \ref{sensor-syncronsisation}).
However, this no longer works for long distances and the syncronisation must be made via the network connection. 

If time-critical synchronisation is required, (+ptp) and (+pps) output functionality can be used on many single-board computers, such as the RaspberryPi Compute Module.


* was ptp, bild pps output
* alle clients über ptp verbunden
* dso bild von jeff gerling über rpi4 ptp


#### Command-Router

* nummerieierung zuerst lokale sensoren dann weitere proxy sensoren
* commando templating



### Examples







# Usability improvements


## Commandline interface

* automatische sensor dedettion
* planung verschiedener messungen mit untersch. hardware
* zentrale abarbeitung

## Programmable data processing pipeline

%%example_measurement_analysis_pipeline.png%%


* datenanalyse für nicht programmieruer
* automatisierter aufbau der call-tree
* mit typcheck
* alle funktionen mit bestimmer signtur werden automatisch aus globals geladen und stehen nutzer zur verfühung


 ```yaml
 # pipeline_example_measurement_processing.yaml
 settings:
  enabled: true
  export_intermediate_results: false
  name: pipeline_example_measurement_processing

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



## Package distribution

%%MagneticReadoutProcessing_library_hosted_on_PyPi.png%%

One important point that improves usability for users is the simple installation of the library.
As it was created in the Python programming language, there are several public package directories where users can provide their software modules. Here, `PyPi`[@PyPI]\ref{MagneticReadoutProcessing_library_hosted_on_PyPi.png}[@MagneticReadoutProcessingPyPI] is the most commonly used package directory and offers direct support for the package installation programm (+pip).

In doing so, (+pip) not only manages possible package dependencies, but also manages the installation of different versions of a package. In addition, the version compatibility is also checked during the installation of a new package, which can be resolved manually by the user in the event of conflicts.

```bash
  # https://pypi.org/project/MagneticReadoutProcessing/
  # install the latest version
  $ pip3 install MagneticReadoutProcessing
  # install the specific version 1.4.0
  $ pip3 install MagneticReadoutProcessing==1.4.0
```

To make the library compatible with the package directory, Python provides separate installation routines that build a package in an isolated environment and then provide an installation `wheel` archive. This can then be uploaded to the package directory.

Since the library requires additional dependencies (e.g. `numpy`, `matplotlib`), which cannot be assumed to be already installed on the target system, these must be installed prior to the actual installation. These can be specified in the library installation configuration `setup.py` for this purpose.

```python
  # $ cat ./setup.py

  # dynamic requirement loading using 'requirements.txt'
  req_path = 'requirements.txt'
  with pathlib.Path(req_path).open() as requirements_txt:
      install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

  setup(name='MagneticReadoutProcessing',
        version='1.4.3',
        url='https://github.com/LFB-MRI/MagnetCharacterization/',
        packages= ['MRP', 'MRPcli', 'MRPudpp', 'MRPproxy'],
        install_requires=install_requires,
        include_package_data=True,
        package_data={"": ["**/*.mag.json", "**/*.yaml", "**/*.html", "**/*.js", "**/*.css", "**/*.md", "**/*.json", "**/*.ts", "**/*.xml"]},
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

%%MagneticReadoutProcessing_documentation_hosted_on_ReadTheDocs.png%%


In order to provide comprehensive documentation for the user, the source code was documented using Python-`docstrings`[@PythonDocstringReference]. This includes, among other things:

* Function description
* Input parameters - `param` and `type`
* Return value - `returns`, `rtype`

```python
    # MRPDataVisualisation.py - example docstring
    def plot_temperature(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None, _unit: str = "degree C") -> str:
        """
        Plots a temperature plot of the reading data as bar-graph figure

        :param _readings: readings to plot
        :type _readings: list(MRPReading.MRPReading)

        :param _title: Title text of the figure, embedded into the head
        :type _title: str

        :param _filename: export graphic to an given absolute filepath with .png
        :type _filename: str

        :returns: returns the filepath of the generated .png image file
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


[@ReadTheDocs]

[@MagneticReadoutProcessingReadTheDocs]

\ref{MagneticReadoutProcessing_documentation_hosted_on_ReadTheDocs.png}


### Tests


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


