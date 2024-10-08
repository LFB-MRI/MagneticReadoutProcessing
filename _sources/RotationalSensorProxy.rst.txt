RSP - Rotational Sensor Proxy
#######################################


This cli module is used to interface the currently most complex implemented sensor.
The roational sensor scans a manget using a polar mechanical sensor around the magnet.





Installation
************

.. note::

    In order to allow direct running of the examples below, the ``venv`` is used.
    So all cli commands are changed to: ``./venv/bin/python3.9 ./MRPRotationalSensorProxy/rsp.py`` instead of ``python3 ./MRPRotationalSensorProxy/rsp.py``.


.. code-block:: bash
    
    # Help
    $ ./venv/bin/python3.9 ./MRPRotationalSensorProxy/rsp.py --help
    Usage: rsp.py proxy [OPTIONS] COMMAND [ARGS]...
    Options:
    --help  Show this message and exit.
    Commands:
    rotational



Proxy for rotational sensor
***************************

To run a network proxy for a rotational sensor, start this software on the SMB inside of the roational sensor.


.. code-block:: bash
    

    # launch Help
    $ ./venv/bin/python3.9 ./MRPRotationalSensorProxy/rsp.py rotational --help
    Usage: rsp.py proxy launch [OPTIONS]

    Options:
    --port INTEGER         default: 5556
    --host TEXT            default: 0.0.0.0
    --debug / --no-debug   default: no-debug
    --klipperenpoint TEXT  default: http://127.0.0.1
    --sensordevice TEXT    default: /dev/ttyACM0
    --sensorbaud INTEGER   default: 0
    --help                 Show this message and exit.


To run the proxy interface and start the rest api, the launch command can be used with parameters from above.
Here in general two parameters are needed. One for the movement (klipper/moonraker) instance and one to interface the sensor.

.. code-block:: bash

    # url of the klipper instance, typical: klipperenpoint=http://127.0.0.1
    # sensordevice=/dev/ttyACMO or /dev/ttyUSB0 or use  ls /dev/serial/by-id/* go get right path
    # also socket:// urls are supporty by using it together with ser2net
    $ ./venv/bin/python3.9 ./MRPRotationalSensorProxy/rsp.py proxy rotational --klipperenpoint http://192.168.178.123 --sensordevice=socket://192.168.178.123:10001
    // FIRMWARE_NAME:Klipper FIRMWARE_VERSION:v0.11.0-303-g67499853
    PRECHECK: MECHANIC: True
    PRECHECK: SENSOR: 525771256544952
    Proxy started. http://0.0.0.0:5556/
    Terminate  [Y/n] [y]: 


Accessing the Rest-API
**********************

