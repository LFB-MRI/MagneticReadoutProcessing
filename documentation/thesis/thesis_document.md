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

* einfache bedienung durch nutzer auch ohne weitere software
* configuration
* debugging


## Example Sensors

*anbei werden drei erschienee sensoren für unterschiedliche anwedungfälle
* tablle statisch dynamisch



### 1D: Single Sensor

* einfachster aufbau rp pico + sensor


### 2D: Dual Sensor

* gleicher abstand zwei gleicher sensoren
* schnelle erkennung der plarisationsebene ggf offset vom mittelpunkt dieser

### Full-Sphere

* komplexester aufbau sensor + mechanik
* polar mechanisches system
* full sphere sensor

### Integration of an Professional Teslameter

* einfach anbindung professioneller teslameter
* Voltkraft

### Single channel NMR magnetometer



# Software readout framework


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


