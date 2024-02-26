# DEMO

### SENSOR

* show sensor cli

## CLI

* idea: preconfigure measurement
* run all measurements unsupervised
* => multi sensor
* => network support

```bash
$ pip install MagneticReadoutProcessing

# CONFIGURE MEASUREMENT
$ MRPCli --basepath $(pwd) config setup demo
# > demo
# > measurements
# > 0
# > 10
# > 1   # => *1000 if hardware averaging is enabled

$ MRPCli --basepath $(pwd) config setupsensor demo
# > 0 #=> note thats a unified sensor is connected

# SHOW SENSOR INTERACTION
$ MRPCli --basepath $(pwd) sensor info demo
$ MRPCli --basepath $(pwd) sensor query demo
# RUN MEASUREMENT + PLOTS
$ MRPCli --basepath $(pwd) measure run --generate-plots demo 

```


## UDPP

### SETUP
```bash
$ bash build.sh
$ clear
$ docker run --rm -it -v $(pwd):/mrpdemo mrpdemo:latest /bin/bash
# INSTALL LATEST VERSION
$ pip install MagneticReadoutProcessing
# SHOW INSTALLED VERSION
$ pip3 freeze | grep MagneticReadoutProcessing
```

### RUN PIPELINE

* similar to Gitlab CI

```bash
$ MRPUdpp --basepath $(pwd) pipeline listfunctions

$ MRPUdpp --basepath $(pwd) pipeline run --pipeline pipeline_minimal

# > used sensor bias readings taken from sensor in evaluation used
$ MRPUdpp --basepath $(pwd) pipeline run --pipeline pipeline_bias

# > concept additional_custom_modules
# > from usecase evaluation
# >
$ MRPUdpp --basepath $(pwd) pipeline run --pipeline pipeline_filter
```

###