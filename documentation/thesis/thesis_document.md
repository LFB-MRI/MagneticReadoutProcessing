# Introduction

# Fundamentals

## Permanent magnet MRI

### Typical B0 Magnet structures

## Shimming procedure



# State of the art

## Opensource projects





# Unified Sensor

ziel ist es einen low cost hallsensor  zu entwickeln welcher möglichst
* universell
* verschienee sensoren abbilden kann
* mit verschienden magneten typen und formen nutzbar
* reproduzierbar
* 1d, 2d, 3d
* integration

## Sensor selection

* list of typical low cost hall sensors
* => alle i2c in der regel

## Mechanical Structure

* 3d druck toleranztest
* magnet halterung
*

## Electrical Interface

* usb, ethernet
* pps input output
* multiplexer for 

## Firmware

* automatic sensor detation
* serial cli support for manual mode
* sync impulse => 1 mastersensor als taktqelle
* interene mittelung und speichern der werte im buffer

### CLI Interface

* einfache bedienung durch nutzer auch ohne weitere software
* configuration

## Example Sensors


### 1D 

* einfachster aufbau rp pico + sensor

### 3D

* komplexester aufbau sensor + mechanik
* full sphere sensor





# Software readout framework


## Library requirements


### Concepts

### User interaction points

* grafik zeigen
* einzelne module erleutern

 
#### HAL

* aufbau hal im grunde wird nur ein die commandos an das sensor cli weitergegeben
* alle sensoren implementieren mehr oder weniger die gleichen befehle
* hal gibt nur weiter und ist "dumm"

#### Visualisation

#### Calibration


### Data management

* format import export
* matlab

#### Meta-Data





### Multi-Sensor setup

* combination of different connected sensors into one measurement mesh

* besipiel setup mit zwei raspberrypi´s



#### Network-Proxy

* erkennung aller lokal angeschlossener sensoren
* zsätzlich weiterleitung von anderen proxy systemen

#### Sensor Syncronisation

* alle clients über ptp verbunden
* zentraler reset zwischen zwei pps pulsen um den readout counter auf 0 zu setzten


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



### End to end testing




# Evaluation


## Prequesites for evaluation

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


