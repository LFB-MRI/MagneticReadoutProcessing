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
from moonraker import MoonrakerPrinter
from MRP import MRPPHalRestRequestResponseState, MRPHal


class RSPProxyGlobals:
    sensor_port: MRPHal.MRPHalSerialPortInformation
    sensor: MRPHal.MRPPHal
    mechanic: MoonrakerPrinter
    lock: Lock = Lock()
    initialized: bool = False


    def __init__(self):
        self.sensor_port = MRPHal.MRPHalSerialPortInformation(_path="")
        self.sensor = MRP.MRPHal.MRPPHal = MRP.MRPHal.MRPPHal(self.sensor_port)
        self.mechanic = MoonrakerPrinter("", no_init=True)
        self.initialized = False

    def init(self, klipperendpoint:str, sensordevice:str, sensorbaud:int = 0, disbaleprecheck:bool = False):


        self.mechanic.set_address("{}".format(klipperendpoint))
        self.mechanic.init()

        self.sensor_port.device_path = sensordevice
        self.sensor.set_serial_port_information(self.sensor_port)

        # CHECK PARAMETERS
        rfw_succ, _ = self.mechanic.request_firmware() # REQUEST VERSION

        if rfw_succ:
            print("PRECHECK: MECHANIC: {}".format(True))
        elif not disbaleprecheck:
            raise Exception("cant connect to klipper/moonrakerusing: {}".format(klipperendpoint))
        # CHECK SENSOR CONNECTION

        try:
            if sensorbaud > 0:
                self.sensor_port.baudrate = sensorbaud

            self.sensor.connect()
            print("PRECHECK: SENSOR: {}".format(self.sensor.get_sensor_id()))
            #self.sensor.disconnect()
        except Exception as e:
            if not disbaleprecheck:
                raise Exception("cant connect to sensor using {}: {}".format(sensordevice, str(e)))

        self.initialized = True


app_typer = typer.Typer()
app_flask = Flask(__name__)
cors = CORS(app_flask)
app_flask.config['CORS_HEADERS'] = 'Content-Type'

terminate_flask: bool = False
hardware_instances: RSPProxyGlobals = RSPProxyGlobals()



def signal_andler(signum, frame):
    global terminate_flask
    terminate_flask = True
    time.sleep(4)
    exit(1)
signal.signal(signal.SIGINT, signal_andler)


@app_flask.errorhandler(404)
def page_not_found(e):
    return redirect("/rsp/status")


@app_flask.route("/rsp/initialize")
@cross_origin()
def initialize():
    global hardware_instances

    #user = request.args.get('user')
    origin = bleach.clean(request.args.get('origin', ''))
    # IF NOT INITILALIZED INIT HARDWARE_INSTANCED_ WITH PROVIDED HARDWARE PARAMETERS
    if not app_flask.config.get('initialized', False):
        with hardware_instances.lock:
            klipperendpoint: str = app_flask.config["syscfg"]["klipperendpoint"]
            sensordevice: str = app_flask.config["syscfg"]["sensordevice"]
            sensorbaud: int = app_flask.config["syscfg"]["sensorbaud"]
            disbaleprecheck: int = app_flask.config["syscfg"]["disbaleprecheck"]

            # TRY TO CONNECT TO THE HARDWARE
            hardware_instances.init(klipperendpoint, sensordevice, sensorbaud, disbaleprecheck)
            # MARK AS SYSTEM INITIALIZED
            app_flask.config['initialized'] = True

    if len(origin) > 0:
        return redirect(origin)

    return jsonify(app_flask.config)

@app_flask.route("/rsp/perform_mea")
@cross_origin()
def

@app_flask.route("/rsp/disconnect")
@cross_origin()
def disconnect():
    global hardware_lock

    # if hardware is not initialized redirect to init route first
    # after init the request is coming back here
    if not app_flask.config.get('initialized', False):
        return redirect('/rsp/initialize?origin={}'.format(request.base_url))

    # try to disconnect the hardware
    with hardware_instances.lock:
        hardware_instances.sensor.disconnect() # disconnect sensors
        hardware_instances.mechanic.disable_motors() # disbale motors

    return jsonify({"error": False})


@app_flask.route("/rsp/status")
@cross_origin()
def status():
    global hardware_instances

    # if hardware is not initialized redirect to init route first
    # after init the request is coming back here
    if not app_flask.config.get('initialized', False):
        return redirect('/rsp/initialize?origin={}'.format(request.base_url))

    ret: MRPPHalRestRequestResponseState = MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState()
    ret.sensortype = "rotationsensor"
    ret.id = machineid.id()
    ret.version = __version__
    # also add startconfig
    resdict: dict = ret.__dict__
    resdict.update(app_flask.config.get('syscfg', {}))

    resdict['hardware'] = {}
    # if system is not initialized redirect to init route first
    if app_flask.config.get('initialized', False):
        resdict['sys_initialized'] = True
        with hardware_instances.lock:
            resdict['hardware']["sensorid"] = hardware_instances.sensor.get_sensor_id()

            _, mechred = hardware_instances.mechanic.request_firmware()  # REQUEST VERSION
            resdict['hardware'].update(mechred)
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
def rotational(typer_ctx: typer.Context, port: int = 5556, host: str = "0.0.0.0", debug: bool = False, klipperendpoint: str = "http://127.0.0.1", sensordevice: str = "/dev/ttyACM0", sensorbaud: int = 0, disbaleprecheck: int = 0):
    global terminate_flask
    #global hardware_instances



    sys_cfg = {
        'klipperendpoint': klipperendpoint,
        'sensordevice': sensordevice,
        'sensorbaud': sensorbaud,
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
