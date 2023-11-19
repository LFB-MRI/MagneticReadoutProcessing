"""Typer base MRPcli interface to allow the user to setup an RotationalSensor"""

__version__ = '0.0.1'




import bleach
import signal
import typer
from flask import Flask, request, jsonify, make_response, redirect, render_template
from flask_cors import CORS, cross_origin
import time
import multiprocessing
from waitress import serve
import machineid
import json_fix

from MRP import MRPPHalRestRequestResponseState

terminate_flask: bool = False



app_typer = typer.Typer()
app_flask = Flask(__name__)
cors = CORS(app_flask)
app_flask.config['CORS_HEADERS'] = 'Content-Type'
def signal_andler(signum, frame):
    global terminate_flask
    terminate_flask = True
    time.sleep(4)
    exit(1)
signal.signal(signal.SIGINT, signal_andler)



@app_flask.route("/status")
@cross_origin()
def status(pipeline:str, stagename:str, parameter:str, value: str = ""):
    ret: MRPPHalRestRequestResponseState = MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState()
    ret.sensortype = "rotationsensor"
    ret.id = machineid.id()
    ret.version = __version__

    return jsonify(ret)


def flask_server_task(_config: dict):
    host:str = _config.get("host", "0.0.0.0")
    port: int = _config.get("port", 5556)
    debug: bool = _config.get("debug", False)


    if debug:
        app_flask.run(host=host, port=port, debug=debug)
    else:
        serve(app_flask, host=host, port=port)




@app_typer.command()
def launch(ctx: typer.Context, port: int = 5556, host: str = "0.0.0.0", debug: bool = False):
    global terminate_flask

    flask_config = {"port": port, "host": host, "debug": debug}
    flask_server: multiprocessing.Process = multiprocessing.Process(target=flask_server_task, args=(flask_config,))
    flask_server.start()

    time.sleep(3)
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
