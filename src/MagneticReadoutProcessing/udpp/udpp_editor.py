"""Typer base cli interface to allow the user to interact with the udppf system"""

import os
import signal
from pathlib import Path
from typing import Annotated
import typer
from UDPPFunctionTranslator import UDPPFunctionTranslator
from flask import Flask, request, jsonify, make_response, redirect
import time
import multiprocessing
from waitress import serve
import udpp_config

terminate_flask: bool = False



app_typer = typer.Typer()
app_flask = Flask(__name__, static_url_path='/static', static_folder=udpp_config.STATIC_FOLDER, template_folder=udpp_config.TEMPLATE_FOLDER)

def signal_andler(signum, frame):
    global terminate_flask
    terminate_flask = True
    time.sleep(4)
    exit(1)
signal.signal(signal.SIGINT, signal_andler)


@app_flask.route("/api/listpipelines")
def listpipelines():
    pipelines = UDPPFunctionTranslator.load_pipelines(udpp_config.PIPELINES_FOLDER)
    res: [str] = []

    for k, v in pipelines.items():
        res.append({
        'files': k,
        'names': v['settings']['name']
        })

    return jsonify(res)


@app_flask.route("/api/getpipeline/<filename>")
def getpipeline(filename):
    assert filename == request.view_args['filename']

    pipelines = UDPPFunctionTranslator.load_pipelines(udpp_config.PIPELINES_FOLDER)

@app_flask.route("/")
def index():
    return redirect("/static/dist/index.html")



def flask_server_task(_config: dict):
    host:str = _config.get("host", "0.0.0.0")
    port: int = _config.get("port", 5555)
    debug: bool = _config.get("debug", False)


    if debug:
        app_flask.run(host=host, port=port, debug=debug)
    else:
        serve(app_flask, host=host, port=port)




@app_typer.command()
def launch(ctx: typer.Context, port: int = 5555, host: str = "0.0.0.0", debug: bool = False):
    global terminate_flask

    flask_config = {"port": port, "host": host, "debug": debug}
    flask_server: multiprocessing.Process = multiprocessing.Process(target=flask_server_task, args=(flask_config,))
    flask_server.start()

    time.sleep(3)
    while( not terminate_flask):
        print("Editor started. Please open http://{}:{}/".format(host, port))
        if typer.prompt("Terminate  [Y/n]", 'y') == 'y':
            break


    # STOP
    flask_server.terminate()
    flask_server.join()



@app_typer.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass
    #Path(PIPELINES_FOLDER).mkdir(parents=True, exist_ok=True)
    #Path(TMP_FOLDER).mkdir(parents=True, exist_ok=True)






if __name__ == "__main__":
    app_typer()
