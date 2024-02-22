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
from MRPproxy import machineid

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
    ids: [str] = []
    combined_sensornames: [str] = []


    lock: Lock = Lock()
    initialized: bool = False


    def __init__(self):
        self.initialized: bool = False

    def get_combined_id(self) -> str:
        return "-".join(self.ids)


    def get_hal_instance_by_command(self, _cmd: str, _id: str) -> MRPHal.MRPHal:


        if _cmd in self.commandrouter:
            try:

                dlist: [dict] = self.commandrouter[_cmd]

                if len(dlist) <= 0:
                    return None

                index: int = -1
                if len(dlist) == 1:
                    index: int = dlist[0]['index']
                else:

                    for e in dlist:
                        if e['id'] == _id:
                            index = e['index']
                            break


                if index <= len(self.devices):
                    return self.devices[index]
                else:
                    raise MRPProxyException("get_hal_instance_by_command LUT out of range")
            except Exception as e:
                raise MRPProxyException(str(e))
        return None


    def get_combined_commands(self) -> [str]:
        return self.combined_commands

    def get_combined_sensor_names(self) -> [str]:
        return self.combined_sensornames
    def get_combined_capabilities(self) -> [str]:
        return self.combined_capabilities


    def add_command_to_router(self, _cmd: str, _index: int, _id: str):
        #self.commandrouter['readsensor'] = dev_index

        if _cmd not in self.commandrouter:
            self.commandrouter[_cmd] = []

        if len(self.commandrouter[_cmd]) <= 0:
            self.commandrouter[_cmd] = [{'index': _index, 'id': _id}]
        else:
            self.commandrouter[_cmd].append({'index': _index, 'id': _id})


    def init(self, _devices: [str], _disbaleprecheck: bool = False):

        if _devices is None or len(_devices) <= 0:
            raise Exception("_devices is None but needs to be supplied with at least one entry")

        self.combined_capabilities = []
        self.commandrouter = {}
        self.devices = []
        self.ports = []
        self.ids = []


        for idx, device in enumerate(_devices):

            port: MRP.MRPHalSerialPortInformation = MRP.MRPHalSerialPortInformation.MRPHalSerialPortInformation(device)

            try:
                hal: MRPHal.MRPHal = MRPHalHelper.MRPHalHelper.createHalInstance(port)
                hal.set_serial_port_information(port)
                hal.connect()
                id: str = hal.get_sensor_id()
                print("PRECHECK: SENSOR_HAL: {}".format(id))
                self.ids.append(id)
                #self.sensor.disconnect()

                # EVERY CHECK PASSED ADD DEVICE TO LIST
                self.devices.append(hal)
                self.ports.append(port)

                # GET CAPABILITIES
                self.combined_capabilities.extend(hal.get_sensor_capabilities())

                self.combined_sensornames.extend(hal.get_sensor_names())
                # NOW CHECK WICH COMMANDS CAN BE EXECUTED BY THIS DEVICE
                cmdlist: [str] = hal.get_sensor_commandlist()
                self.combined_commands.extend(cmdlist)

                dev_index = len(self.devices)-1
                if len(cmdlist) > 0:
                    for cmd in hal.get_sensor_commandlist():
                        self.add_command_to_router(cmd, dev_index, id)

                else:
                    # TODO REMOVE
                    caps: [str] = hal.get_sensor_capabilities()
                    if 'axis_b' in caps:
                        # if there is an axis_ cap then there should be a readout command for that
                        self.add_command_to_router('readsensor', dev_index, id)
                        self.add_command_to_router('sensorcnt', dev_index, id)
                        self.combined_commands.extend(['readsensor', 'sensorcnt'])

                    if 'axis_temp' in caps:
                        self.add_command_to_router('temp', dev_index, id)
                        self.combined_commands.extend(['temp'])
                    if 'static' in caps:
                        self.add_command_to_router('info', dev_index, id)
                        self.combined_commands.extend(['info'])

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
    redirect_commands = ['status', 'initialize', 'disconnect', 'combinedsensorcnt']
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
            hal: MRPHal.MRPHal = hardware_instances.get_hal_instance_by_command(cmd_wo_parameters, devicetype)
            if hal is not None:
                # EXECUTE COMMAND
                result_dict['output'] = hal.send_command(cmd)


            else:
                result_dict['output'] = []
                result_dict['error'] = True


            # SOME COMMANDS RESPORTS THE ERROR IN THE OUTPUT
            if 'error' in result_dict['output'] and result_dict['output'] is not None:
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
        for hw in hardware_instances.devices:
            hw.disconnect()


    return jsonify({"error": False})

@app_flask.route("/proxy/combinedsensorcnt")
@cross_origin()
def combinedsensorcnt():
    global hardware_lock

    # if hardware is not initialized redirect to init route first
    # after init the request is coming back here
    if not app_flask.config.get('initialized', False):
        return redirect('/proxy/initialize?origin={}'.format(request.base_url))

    result_dict: dict = {
        'output': False,
        'output': ['0']
    }


    # try to disconnect the hardware
    count: int = 0
    with hardware_instances.lock:
        for hw in hardware_instances.devices:
            count = count + hw.get_sensor_count()

    result_dict['output'] = [str(count)]

    return jsonify(result_dict)


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
    ret.sensornames = []
    ret.commands = ['status', 'initialize', 'disconnect', 'combinedsensorcnt', 'sid']

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
            ret.sensornames.extend(hardware_instances.get_combined_sensor_names())

            resdict['id'] = "{}".format(hardware_instances.get_combined_id())
        resdict['commands'] = ret.commands
        resdict['capabilities'] = ret.capabilities
        resdict['sensornames'] = ret.sensornames


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
