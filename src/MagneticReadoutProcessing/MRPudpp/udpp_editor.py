"""Typer base MRPcli interface to allow the user to interact with the udppf system"""
import multiprocessing
import signal
import time

import bleach
import typer
from flask import Flask, request, jsonify, redirect, render_template
from flask_cors import CORS, cross_origin
from waitress import serve

from MRPudpp import UDPPFunctionTranslator
from MRPudpp import udpp_config

terminate_flask: bool = False



app_typer = typer.Typer()
app_flask = Flask(__name__, static_url_path='/static', static_folder=udpp_config.UDPPConfig.get_static_folder(), template_folder=udpp_config.UDPPConfig.get_template_folder())
cors = CORS(app_flask)
app_flask.config['CORS_HEADERS'] = 'Content-Type'
def signal_andler(signum, frame):
    global terminate_flask
    terminate_flask = True
    time.sleep(4)
    exit(1)
signal.signal(signal.SIGINT, signal_andler)



@app_flask.route("/api/updateinspectorparameter/<pipeline>/<stagename>/<parameter>/<value>")
@cross_origin()
def updateinspectorparameter(pipeline:str, stagename:str, parameter:str, value: str = ""):
    assert pipeline == request.view_args['pipeline']
    pipeline = bleach.clean(pipeline)

    assert stagename == request.view_args['stagename']
    stagename = bleach.clean(stagename)

    assert parameter == request.view_args['parameter']
    parameter = bleach.clean(parameter)

    assert value == request.view_args['value']
    value = bleach.clean(value)


    # CHECK PIPELINE EXIST
    pipelines = UDPPFunctionTranslator.UDPPFunctionTranslator.load_pipelines(udpp_config.UDPPConfig.get_pipeline_folder())
    if pipeline not in pipelines:
        return jsonify({'error': 'pipeline does not exist'}), 500

    pipeline_data:dict = pipelines[pipeline]

    # CHECK STAGE EXIST
    stage = UDPPFunctionTranslator.UDPPFunctionTranslator.extract_pipelines_steps(_pipeline=pipeline_data)
    if stagename not in stage:
        return jsonify({'error': 'stage does not exist'}), 500

    # TODO CHECK STAGE EXISTS
    # TODO CHECK FUNCTION EXSTS
    # TODO PARSE TO FUNCTION TYPE
    # ASSIGN
    # WRITE TO FILE BACK

    return jsonify({'ok': True})


@app_flask.route("/api/updateblock/<pipeline>/<stagename>/<action>/<functionname>")
@cross_origin()
def updateblock(pipeline:str, stagename:str, action:str, functionname:str):
    assert pipeline == request.view_args['pipeline']
    pipeline = bleach.clean(pipeline)

    assert stagename == request.view_args['stagename']
    stagename = bleach.clean(stagename)

    assert action == request.view_args['action']
    action = bleach.clean(action)

    assert functionname == request.view_args['functionname']
    functionname = bleach.clean(functionname)


@app_flask.route("/api/listpipelines")
@cross_origin()
def listpipelines():
    pipelines = UDPPFunctionTranslator.UDPPFunctionTranslator.load_pipelines(udpp_config.UDPPConfig.get_pipeline_folder())
    res: [str] = []

    for k, v in pipelines.items():
        res.append({
        'file': k,
        'name': v['settings']['name']
        })

    return jsonify({'pipelines':res})



@app_flask.route("/api/getnodetypes")
@cross_origin()
def getnodetypes():
    fkts: dict = UDPPFunctionTranslator.UDPPFunctionTranslator.listfunctions()
    return jsonify({'nodes':list(fkts.keys())})


@app_flask.route("/api/getnodeinformation/<functionname>")
@cross_origin()
def getnodeinformation(functionname: str):
    assert functionname == request.view_args['functionname']
    functionname = bleach.clean(functionname)

    functions: dict = UDPPFunctionTranslator.UDPPFunctionTranslator.listfunctions()

    if functionname not in functions:
        return jsonify({}), 404

    # return same as in stage description
    return jsonify({
        'function': functionname,
        'name': functionname,
        'position': { # Can be ignored
            'x': -1,
            'y': -1
        },
        'parameters': UDPPFunctionTranslator.UDPPFunctionTranslator.get_function_parameters(functionname),
        'inspector_parameters': UDPPFunctionTranslator.UDPPFunctionTranslator.get_inspector_parameters(functionname),
        'returns': UDPPFunctionTranslator.UDPPFunctionTranslator.get_function_return_parameters(functionname)
    })



@app_flask.route("/api/getpipeline/<filename>")
@cross_origin()
def getpipeline(filename: str):

    assert filename == request.view_args['filename']
    filename = bleach.clean(filename)


    # OPTIONAL READ WINDOW SIZE TO CALCULATE NODE POSITIONS IN BROWSER WINDOW
    canvas_size_x: int = request.args.get("canvas_size_x", default=100, type=int)
    canvas_size_y: int = request.args.get("canvas_size_y", default=100, type=int)

    pipelines: dict = UDPPFunctionTranslator.UDPPFunctionTranslator.load_pipelines(udpp_config.UDPPConfig.get_pipeline_folder())
    # pipeline found
    if filename in pipelines:
       return jsonify(UDPPFunctionTranslator.UDPPFunctionTranslator.EDITOR_get_stages_as_array(pipelines[filename], _canvas_view_size_x=canvas_size_x, _canvas_view_size_y=canvas_size_y))

    # create new pipeline and return content
    pipeline: dict = UDPPFunctionTranslator.UDPPFunctionTranslator.create_empty_pipeline(filename, udpp_config.UDPPConfig.get_pipeline_folder())
    # here we will perform a redirect to the new pipeline name
    pipelinefilename: str = list(pipeline.keys())[0]
    # redirect to new base url with replaced filename
    return redirect("{}".format(request.base_url.replace(filename, pipelinefilename)))


@app_flask.route("/")
def index():

    apiendpoint: str = request.base_url.strip("http://").strip("https://") # webclient decides method
    if not apiendpoint.endswith("/"):
        apiendpoint += "/"

    return redirect("/static/dist/index.html?apiendpoint={}".format(apiendpoint + "api/"))




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






if __name__ == "__main__":
    app_typer()
