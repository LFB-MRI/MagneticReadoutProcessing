# MINIMAL PROJECT


```bash
# https://pypi.org/project/MagneticReadoutProcessing/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Hardware Sensor

### CHECK IF CLI IS WORKING
```bash
# IN VENV
$ MRPCli --help
```

### EXAMPLE MAGNET MEASUREMENT USING HARDWARE SENSOR

```bash
# IN VENV
# EXTENDET HARDWARE DEMO IN:
# https://github.com/LFB-MRI/MagneticReadoutProcessing/tree/main/documentation/colloquium/demo
cd "$(dirname "$0")"
$ MRPCli --basepath $PWD/readings config setup test

# CONNECT SENSOR USING USB
$ MRPCli --basepath $PWD/readings config setupsensor test

# CHECK IF SENSOR IS WORKING
$ MRPCli --basepath $PWD/readings sensor query test

# RUN MEASUREMENT
$ MRPCli --basepath $PWD/readings measure run test
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
