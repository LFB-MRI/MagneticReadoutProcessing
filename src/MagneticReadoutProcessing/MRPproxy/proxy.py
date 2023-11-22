"""Typer base MRPcli interface to allow the user to setup an RotationalSensor"""

__version__ = '0.0.1'


import bleach
import signal
import typer
from flask import Flask, request, jsonify, make_response, redirect, render_template, g
from flask_cors import CORS, cross_origin
import time
import multiprocessing
from waitress import serve
from threading import Lock
import MRP
import machineid

from MRP import MRPPHalRestRequestResponseState, MRPHalSerialPortInformation, MRPHal, MRPHalHelper



class MRPProxyException(Exception):
    def __init__(self, message="MRPProxyException thrown"):
        self.message = message
        super().__init__(self.message)

class ProxyGlobals:
    sensor_hal: MRPHal.MRPHal
    manipulator_hal: MRPHal.MRPHal

    lock: Lock = Lock()
    initialized: bool = False


    def __init__(self):
        self.sensor_hal: MRPHal.MRPHal = None
        self.manipulator_hal: MRPHal.MRPHal = None
        self.initialized: bool = False



    def init(self, _sensor_information: MRPHalSerialPortInformation.MRPHalSerialPortInformation, _manipulator_information: MRPHalSerialPortInformation.MRPHalSerialPortInformation = None, _disbaleprecheck: bool = False):

        if _sensor_information is None:
            raise Exception("_sensorinformation is None but needs to be supplied")

        if _sensor_information.getSensorsNeededImplementation() == MRPHalSerialPortInformation.MRPRemoteSensorType.ApiSensor:
            raise MRPProxyException("remote sensor please use instance of MRPHalRest")

        try:
            self.sensor_hal = MRPHalHelper.MRPHalHelper.createHalInstance(_sensor_information)
            self.sensor_hal.set_serial_port_information(_sensor_information)
            self.sensor_hal.connect()
            print("PRECHECK: SENSOR_HAL: {}".format(self.sensor_hal.get_sensor_id()))
            #self.sensor.disconnect()
        except Exception as e:
            if not _disbaleprecheck:
                raise Exception("cant connect to sensor using {}: {}".format(_sensor_information.device_path, str(e)))

        if _manipulator_information is not None:
            try:
                self.manipulator_hal = MRPHalHelper.MRPHalHelper.createHalInstance(_manipulator_information)
                self.manipulator_hal.set_serial_port_information(_manipulator_information)
                self.manipulator_hal.connect()
                print("PRECHECK: MANIPULATOR_HAL: {}".format(self.manipulator_hal.get_sensor_id()))
                # self.sensor.disconnect()
            except Exception as e:
                if not _disbaleprecheck:
                    raise Exception(
                        "cant connect to manipulator using {}: {}".format(_manipulator_information.device_path, str(e)))


        self.initialized = True


app_typer = typer.Typer()
app_flask = Flask(__name__)
cors = CORS(app_flask)
app_flask.config['CORS_HEADERS'] = 'Content-Type'

terminate_flask: bool = False
hardware_instances: ProxyGlobals = ProxyGlobals()



def signal_andler(signum, frame):
    global terminate_flask
    terminate_flask = True
    time.sleep(4)
    exit(1)
signal.signal(signal.SIGINT, signal_andler)


@app_flask.errorhandler(404)
def page_not_found(e):
    return redirect("/proxy/status")



@app_flask.route("/proxy/command")
@cross_origin()
def command():
    global hardware_instances

    cmd = bleach.clean(request.args.get('cmd', ''))
    devicetype = bleach.clean(request.args.get('devicetype', '0'))
    # if hardware is not initialized redirect to init route first
    # after init the request is coming back here
    if not app_flask.config.get('initialized', False):
        initilize_task()


    # PROCESS COMMANDS
    redirect_commands = ['status', 'initialize', 'disconnect']
    if cmd in redirect_commands:
        rd: str = '{}'.format(request.base_url).replace('/command','/{}'.format(cmd))
        return redirect(rd)


    else:
        result_dict = {}
        with hardware_instances.lock:


            ts: int = -1
            tm: int = -1

            if hardware_instances.sensor_hal:
                ts = int(hardware_instances.sensor_hal.get_serial_port_information().getSensorsNeededImplementation().value)

            if hardware_instances.manipulator_hal:
                tm = int(hardware_instances.manipulator_hal.get_serial_port_information().getSensorsNeededImplementation().value)

            if int(devicetype) == ts:
                result_dict['output'] = hardware_instances.sensor_hal.send_command(cmd)

            elif int(devicetype) == tm:
                result_dict['output'] = hardware_instances.sensor_hal.send_command(cmd)

            else:
                result_dict['output'] = []
                result_dict['error'] = True


            # SOME COMMANDS RESPORTS THE ERROR IN THE OUTPUT
            if 'error' in result_dict['output']:
                result_dict['error'] = True

        return jsonify(result_dict)



def initilize_task():
    if not app_flask.config.get('initialized', False):
        with hardware_instances.lock:
            manipulatordevice: str = app_flask.config["syscfg"]["manipulatordevice"]
            sensordevice: str = app_flask.config["syscfg"]["sensordevice"]
            disbaleprecheck: int = app_flask.config["syscfg"]["disbaleprecheck"]

            sensport: MRP.MRPHalSerialPortInformation = MRP.MRPHalSerialPortInformation.MRPHalSerialPortInformation(sensordevice)
            mechport: MRP.MRPHalSerialPortInformation = MRP.MRPHalSerialPortInformation.MRPHalSerialPortInformation(manipulatordevice)
            # TRY TO CONNECT TO THE HARDWARE
            hardware_instances.init(sensport, mechport, disbaleprecheck)
            # MARK AS SYSTEM INITIALIZED
            app_flask.config['initialized'] = True


@app_flask.route("/proxy/initialize")
@cross_origin()
def initialize():
    global hardware_instances

    #user = request.args.get('user')
    origin = bleach.clean(request.args.get('origin', ''))
    # IF NOT INITILALIZED INIT HARDWARE_INSTANCED_ WITH PROVIDED HARDWARE PARAMETERS
    initilize_task()

    if len(origin) > 0:
        return redirect(origin)

    return jsonify(app_flask.config)

# is_connected
# get_sensor_count
# get_sensor_capabilities -> []

@app_flask.route("/proxy/disconnect")
@cross_origin()
def disconnect():
    global hardware_lock

    # if hardware is not initialized redirect to init route first
    # after init the request is coming back here
    if not app_flask.config.get('initialized', False):
        return redirect('/proxy/initialize?origin={}'.format(request.base_url))

    # try to disconnect the hardware
    with hardware_instances.lock:
        hardware_instances.manipulator_hal.disconnect() # disconnect sensors
        hardware_instances.manipulator_hal.disconnect() # disconnect manipulator

    return jsonify({"error": False})


@app_flask.route("/proxy/status")
@cross_origin()
def status():
    global hardware_instances

    # if hardware is not initialized redirect to init route first
    # after init the request is coming back here
    if not app_flask.config.get('initialized', False):
        return redirect('/proxy/initialize?origin={}'.format(request.base_url))

    ret: MRPPHalRestRequestResponseState = MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState()
    ret.sensortype = "rotationsensor"
    ret.id = machineid.id()
    ret.capabilities = []
    ret.version = __version__
    # also add startconfig
    resdict: dict = ret.__dict__
    resdict.update(app_flask.config.get('syscfg', {}))

    resdict['hardware'] = {}
    # if system is not initialized redirect to init route first
    if app_flask.config.get('initialized', False):
        resdict['sys_initialized'] = True
        with hardware_instances.lock:
            resdict['initialized'] = True
            if hardware_instances.sensor_hal:
                resdict['hardware']["sensor_hal"] = hardware_instances.sensor_hal.get_sensor_id()
                ret.capabilities.extend(hardware_instances.sensor_hal.get_sensor_capabilities())
            if hardware_instances.manipulator_hal:
                resdict['hardware']["manipulator_hal"] = hardware_instances.manipulator_hal.get_sensor_id()
                ret.capabilities.extend(hardware_instances.manipulator_hal.get_sensor_capabilities())

        resdict['capabilities'] = ret.capabilities

    else:
        resdict['initialized'] = False

    return jsonify(resdict)


def flask_server_task(_config: dict):
    global hardware_instances
    host: str = _config.get("host", "0.0.0.0")
    port: int = _config.get("port", 5556)
    debug: bool = _config.get("dbg", False)

    app_flask.config.update(_config)
    #with flas
    #    flask.g.test = 0

    #app_flask.app_context().push()
    if debug:
        app_flask.run(host=host, port=port, debug=debug)
    else:
        serve(app_flask, host=host, port=port)




@app_typer.command()
def launch(typer_ctx: typer.Context, port: int = 5556, host: str = "0.0.0.0", debug: bool = False, manipulatordevice: str = "http://127.0.0.1", sensordevice: str = "/dev/ttyACM0", disbaleprecheck: int = 0):
    global terminate_flask
    #global hardware_instances



    sys_cfg = {
        'manipulatordevice': manipulatordevice,
        'sensordevice': sensordevice,
        'disbaleprecheck': disbaleprecheck,
        'initialized': False
    }




    # FINALLY START FLASK

    flask_config = {"port": port, "host": host, "dbg": debug, "syscfg": sys_cfg}
    flask_server: multiprocessing.Process = multiprocessing.Process(target=flask_server_task, args=(flask_config,))
    flask_server.start()

    # STORE user parameter in flask context to access them in each route
    #flask_ctx = app_flask.app_context()




    while( not terminate_flask):
        print("Proxy started. http://{}:{}/".format(host, port))
        if typer.prompt("Terminate  [Y/n]", 'y') == 'y':
            break


    # STOP
    flask_server.terminate()
    flask_server.join()



@app_typer.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    app_typer()
