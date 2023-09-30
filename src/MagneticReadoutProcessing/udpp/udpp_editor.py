"""Typer base cli interface to allow the user to interact with the udppf system"""

import os
from pathlib import Path
from typing import Annotated
import typer
from UDPPFunctionTranslator import UDPPFunctionTranslator
from flask import Flask, request, jsonify,make_response
import time
import multiprocessing

app_typer = typer.Typer()

app_flask = Flask(__name__)

flask_server: multiprocessing.Process = None

PIPELINES_FOLDER = str(Path(str(os.path.dirname(__file__))).parent.joinpath("pipelines"))
TMP_FOLDER = str(Path(PIPELINES_FOLDER).joinpath("generated/"))


@app_flask.route("/")
def index():
    return "<p>Hello, World!</p>"



def flask_server_task(Conf):
   app_flask.run(host='0.0.0.0', port=1337,)



@app_typer.command()
def launch(ctx: typer.Context, port: int = 5000, host: str = "0.0.0.0"):
    #flask_server.start()
    flask_config = {"port": port, "host": host}
    flask_server = multiprocessing.Process(target=flask_server_task, args=(flask_config,))


    while(True):
        time.sleep(1)




@app_typer.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass
    #Path(PIPELINES_FOLDER).mkdir(parents=True, exist_ok=True)
    #Path(TMP_FOLDER).mkdir(parents=True, exist_ok=True)






if __name__ == "__main__":
    app_typer()
