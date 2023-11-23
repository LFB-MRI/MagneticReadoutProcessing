"""Typer base MRPcli interface to allow the user to setup an RotationalSensor"""

__version__ = '0.0.1'


import bleach
import signal
import typer
from typing import List
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
    devices: [MRPHal.MRPHal] = []
    ports: [MRPHalSerialPortInformation.MRPHalSerialPortInformation] = []
    commandrouter: dict = {}
    combined_capabilities: [str] = [] # contains all caps from all connected devices
    combined_commands: [] = []


    lock: Lock = Lock()
    initialized: bool = False


    def __init__(self):
        self.initialized: bool = False



    def get_hal_instance_by_command(self, _cmd: str) -> MRPHal.MRPHal:


        if _cmd in self.commandrouter:
            try:
                index: int = self.commandrouter[_cmd]
                if index <= len(self.devices):
                    return self.devices[index]
                else:
                    raise MRPProxyException("get_hal_instance_by_command LUT out of range")
            except Exception as e:
                raise MRPProxyException(str(e))
        return None


    def get_combined_commands(self) -> [str]:
        return self.combined_commands

    def get_combined_capabilities(self) -> [str]:
        return self.combined_capabilities
    def init(self, _devices: [str], _disbaleprecheck: bool = False):

        if _devices is None or len(_devices) <= 0:
            raise Exception("_devices is None but needs to be supplied with at least one entry")

        self.combined_capabilities = []
        self.commandrouter = {}
        self.devices = []
        self.ports = []


        for idx, device in enumerate(_devices):

            port: MRP.MRPHalSerialPortInformation = MRP.MRPHalSerialPortInformation.MRPHalSerialPortInformation(device)

            try:
                hal: MRPHal.MRPHal = MRPHalHelper.MRPHalHelper.createHalInstance(port)
                hal.set_serial_port_information(port)
                hal.connect()
                print("PRECHECK: SENSOR_HAL: {}".format(hal.get_sensor_id()))
                #self.sensor.disconnect()

                # EVERY CHECK PASSED ADD DEVICE TO LIST
                self.devices.append(hal)
                self.ports.append(port)

                # GET CAPABILITIES
                self.combined_capabilities.extend(hal.get_sensor_capabilities())

                # NOW CHECK WICH COMMANDS CAN BE EXECUTED BY THIS DEVICE
                cmdlist: [str] = hal.get_sensor_commandlist()
                self.combined_commands.extend(cmdlist)

                dev_index = len(self.devices)-1
                if len(cmdlist) > 0:
                    for cmd in hal.get_sensor_commandlist():
                        self.commandrouter[cmd] = dev_index #hal.get_sensor_id()

                else:
                    # TODO REMOVE
                    caps: [str] = hal.get_sensor_capabilities()
                    if 'axis_b' in caps:
                        # if there is an axis_ cap then there should be a readout command for that
                        self.commandrouter['readsensor'] = dev_index
                        self.commandrouter['sensorcnt'] = dev_index
                    if 'axis_temp' in caps:
                        self.commandrouter['temp'] = dev_index
                    if 'static' in caps:
                        self.commandrouter['info'] = dev_index

                    # the get_sensor_commandlist command is only implemented in later version of the sensor firmware, so try to assume
                    # so used capabilities instead

            except Exception as e:
                if not _disbaleprecheck:
                    raise Exception("cant connect to sensor using {}: {}".format(port.device_path, str(e)))

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

            # REMOVE CMD PARAMETERS
            cmd_wo_parameters: str = cmd
            if ' ' in cmd:
                cmd_wo_parameters = cmd.split(' ')[0]

            # GET DEVICE HAL
            hal: MRPHal.MRPHal = hardware_instances.get_hal_instance_by_command(cmd_wo_parameters)
            if hal is not None:
                # EXECUTE COMMAND
                result_dict['output'] = hal.send_command(cmd)


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
            devices: str = app_flask.config["syscfg"]["devices"]
            disbaleprecheck: int = app_flask.config["syscfg"]["disbaleprecheck"]

            # TRY TO CONNECT TO THE HARDWARE
            hardware_instances.init(devices, disbaleprecheck)
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
    ret.commands = ['status', 'initialize', 'disconnect']

    ret.version = __version__
    # also add startconfig
    resdict: dict = ret.__dict__
    resdict.update(app_flask.config.get('syscfg', {}))

    resdict['hardware'] = {}
    # if system is not initialized redirect to init route first
    if app_flask.config.get('initialized', False):

        with hardware_instances.lock:
            resdict['initialized'] = True
            # GET CAPS AND AVAILABLE CMDS FOR THE LOCALLY CONNECTED DEVICES
            ret.capabilities.extend(hardware_instances.get_combined_capabilities())
            ret.commands.extend(hardware_instances.get_combined_commands())

        resdict['commands'] = ret.commands
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
def launch(typer_ctx: typer.Context, devices: List[str], port: int = 5556, host: str = "0.0.0.0", debug: bool = False, disbaleprecheck: int = 0):
    global terminate_flask
    #global hardware_instances



    sys_cfg = {
        'devices': devices,
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
