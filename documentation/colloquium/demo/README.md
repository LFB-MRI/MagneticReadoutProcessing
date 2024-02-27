# DEMO

### SETUP

```bash
$ bash build.sh
$ clear
```


### SENSOR

* show sensor cli

## CLI

* idea: preconfigure measurement
* run all measurements unsupervised
* => multi sensor
* => network support

```bash
$ pip install MagneticReadoutProcessing
$ pip install --upgrade MagneticReadoutProcessing
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

### CLI USING DOCKER
```bash
$ docker run --rm -it --device=/dev/ttyACM0 -v $(pwd):/demo mrpdemo:latest /bin/bash
$ cd demo
```

### CLI FOR ROTATIONAL SENSOR
```bash
# LAUNCH PROXY FIRST
$ MRPProxy proxy launch tcp://169.254.40.154:10001 klipper://169.254.40.154:80 --disbaleprecheck 0
# TEST PROXY
$ curl 127.0.0.1:5556/
# CONNECT SENSOR TO CLI
$ MRPCli --basepath $(pwd) config setupsensor --path http://127.0.0.1:5556 demo  
```



## UDPP

### SETUP
```bash
$ docker run --rm -it -v $(pwd):/demo mrpdemo:latest /bin/bash
$ cd demo
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
