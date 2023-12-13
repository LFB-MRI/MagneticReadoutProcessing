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

* list of typical low cost hall sensors
* => alle i2c in der regel
*

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

* automatic sensor detation
* serial cli support for manual mode
* sync impulse => 1 mastersensor als taktqelle
* interene mittelung und speichern der werte im buffer
* was durch den user implementiert werden muss klasse


### CLI Interface

%%Sensors_CL-Interface.png%%

%%Query_sensors_b_value_using_CLI.png%%


* einfache bedienung durch nutzer auch ohne weitere software
* configuration
* debugging

## Sensor Syncronsisation \label{CHAPTER_Sensor_Syncronsisation}

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

At the moment, it is only possible to detect and use sensors that are directly connected to the PC with the library. This has the disadvantage that there must always be a physical connection. This can make it difficult to install multiple sensors in measurement setups where space or cable routing options are limited. To make sensors connected to a small remote PC available on the network, the 'Proxy' module has been developed. This can be a single board computer (e.g. a Raspberry Pi). The small footprint and low power consumption make it a good choice. It can also be used in a temperature chamber. The approach of implementing this via a REST interface also offers the advantage that several measurements or experiments can be recorded at the same time with the sensors.

%%MRPlib_Proxy_Module.png%%

Another application example is when sensors are physically separated or there are long distances between them.
By connecting several sensors via the proxy module, it is possible to link several instances and all sensors available in the network are available to the control PC.

%%mrp_proxy_multi.png%%

The graphic \ref{mrp_proxy_multi.png} shows the modified multi-proxy - multi-sensor topology. Here, both proxy instances do not communicate directly with the control PC, but remote PC #2 is connected to remote PC #1. This is then visible as a sensor opposite the Control PC, even if there are several proxy instances behind it.


#### Network-Proxy

The graphic \ref{MRPlib_Proxy_Module.png} shows the separation of the various HAL instances, which communicate with the physically connected sensors on the remote PC and the control PC side, which communicates with the remote side via the network. 
For the user, nothing changes in the procedure for setting up a measurement. The proxy application must always be started on the remote PC side. 


```bash
    # START PROXY INSTNACE WITH TWO LOCALLY CONNECTED SENSORS
    $ python3 mrpproxy.py proxy launch /dev/ttySENSOR_A /dev/ttySENSOR_B # add another proxy instance http://proxyinstance_2.local for multi-sensor, multi-proxy chain
    Proxy started. http://0.0.0.0:5556/
    PRECHECK: SENSOR_HAL: 1337 # SENSOR A FOUND
    PRECHECK: SENSOR_HAL: 4242 # SENSOR B FOUND
    Terminate  [Y/n] [y]: 
```

After the proxy instance has been successfully started, it is optionally possible to check the status via the REST interface:

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

The query result shows that the sensors are connected correctly and that their capabilites have also been recognised correctly. To be able to configure a measurement on the other, only the IP address or host name of the remote PC is required:


```bash
    # CONFIGURE MEASUREMENT JOB USING A PROXY INSTANCE
    $ python3 mrpproxy.py proxy launch /dev/ttySENSOR_A /dev/ttySENSOR_B
    
```


#### Sensor Syncronisation




Another important aspect when using several sensors via the proxy system is the synchronisation of the measurement intervals between the sensors. 
Individual sensor setups do not require any additional synchronisation information, as this is communicated via the USB interface.
If several sensors are connected locally, they can be connected to each other via their sync input using short cables. One sensor acts as the central clock (see chapter \ref{CHAPTER_Sensor_Syncronsisation}).
However, this no longer works for long distances and a diversion must be made via the network connection. 

If time-critical synchronisation is required, PTP and PPS functionality can be used on many single-board computers (such as the RaspberryPi Compute Module).


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

* datenanalyse für nicht programmieruer
* automatisierter aufbau der call-tree
* mit typcheck
* alle funktionen mit bestimmer signtur werden automatisch aus globals geladen und stehen nutzer zur verfühung

### Web base pipeline configuration

* drag& drop system
* automatische convertierung zum yaml system

## Package management

* verteilung durch paketmanager
* docker cli beispiel 

### Documentation







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


