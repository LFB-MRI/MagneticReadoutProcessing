# MINIMAL PROJECT



## Hardware Sensor

### NOTE

Example 360 degree fullsphere readings for the minimal example are located in the `readings/examples` folder, so its possible to skip the hardware sensor procedure.

### INSTALL CLI PACKAGES

```bash
# https://pypi.org/project/MagneticReadoutProcessing/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### CHECK IF CLI IS WORKING
```bash
# IN VENV
$ MRPCli --help
```

### EXAMPLE MAGNET MEASUREMENT USING STATIC SENSOR

```bash
# IN VENV
# EXTENDET HARDWARE DEMO IN:
# https://github.com/LFB-MRI/MagneticReadoutProcessing/tree/main/documentation/colloquium/demo
cd "$(dirname "$0")"
$ MRPCli --basepath $PWD/readings config setup static_sensor

# CONNECT SENSOR USING USB
$ MRPCli --basepath $PWD/readings config setupsensor static_sensor

# CHECK IF SENSOR IS WORKING
$ MRPCli --basepath $PWD/readings sensor query static_sensor

# RUN MEASUREMENT
$ MRPCli --basepath $PWD/readings measure run static_sensor
```

### EXAMPLE MAGNET MEASUREMENT USING ROTATIONAL FULLSPHERE SENSOR

```bash
# IN VENV
# EXTENDET HARDWARE DEMO IN:
# https://github.com/LFB-MRI/MagneticReadoutProcessing/tree/main/documentation/colloquium/demo
cd "$(dirname "$0")"
# USE NUMBER DATAPOINTS: 18 (so of at least 18 datapoints)
$ MRPCli --basepath $PWD/readings config setup rotationalsensor_measurement

# !!!
# CONNECT THE ROTATIONAL SENSOR USING THE PROXY MODULE
$ MRPProxy proxy launch tcp://rotationsensor.local:10001 klipper://rotationsensor.local:80 --disbaleprecheck 0
Proxy started. http://0.0.0.0:5556/
Terminate  [Y/n] [y]: 

# TEST IF PROXY IS WORKING RESULT IS A JSON OBJECT WITH "sensortype" : "rotationsensor"
$ curl -L 127.0.0.1:5556/ | json_pp

# FINALLYmCONFIGURE THE SENSOR CONNECTION IN THE CLI USING A MANUALLY SPECIFIED IP
$ MRPCli --basepath $PWD/readings config setupsensor --path http://127.0.0.1:5556 rotationalsensor_measurement
# !!!
# CHECK IF SENSOR IS WORKING
$ MRPCli --basepath $PWD/readings sensor query rotationalsensor_measurement

# RUN MEASUREMENT
$ MRPCli --basepath $PWD/readings measure run rotationalsensor_measurement
```


## Python project

This folder contains a pre-configured PyCharm and VSCode (launch.json) project. To open it use `File` -> `Open` in PyCharm IDE or `Open Folder` in VSCode.

###  VENV

To avoid messing up your local Python environment, the usage of Python-`venv` is used here.
For `Code` and `PyCharm` the environment should already setup, but in case there are any runtime errors, the environment can be setup manually:

```bash
# CREATE VENV IN MINIMAL_PROJECT FOLDER
python -m venv venv
# ACTIVATE
source venv/bin/activate
# INSTALL NEEDED PACKAGES
pip install -r requirements.txt
```



### MAIN.PY EXAMPLE
The `main.py` contains a simple import, do someting, export example using the `MRP` framework.
In addition the `readings` folder contains magnet readings of ten different magnets using the `Rotational Full-Sphere` sensor.



### MORE STUFF


```bash
# MORE READINGS OF DIFFERENT MAGNETS AND SENSORS:
# https://github.com/LFB-MRI/MagneticReadoutProcessing/tree/main/src/MagneticReadoutProcessing/readings

# MRP PACKAGE SOURCE CODE
# https://github.com/LFB-MRI/MagneticReadoutProcessing/tree/main/src/MagneticReadoutProcessing/MRP
```
