import os
from pathlib import Path
from typing import Annotated
import typer
from UDPPFunctionTranslator import UDPPFunctionTranslator


app = typer.Typer()

PIPELINES_FOLDER = str(Path(str(os.path.dirname(__file__))).parent.joinpath("pipelines"))

@app.command()
def listfunctions(ctx: typer.Context):
    print(UDPPFunctionTranslator.listfunctions())

@app.command()
def listenabledpipelines(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(PIPELINES_FOLDER)
    for k in pipelines:
        print(k)


@app.command()
def run(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(PIPELINES_FOLDER)

    # ITERATE OVER EACH PIPELINE
    for pipeline in pipelines:
        # EXTRACT SETTINGS
        settings: dict = pipeline['settings']
        # EXTRACT STEPS
        # each step
        steps = UDPPFunctionTranslator.extract_pipelines_steps(pipeline)

        # CHECK FOR DUPLICATE PIPELINE STEPS
        # multiple main: true ?
        # CHECK FOR RING CALLS
        # CHECK INPUT OUTPUT PARAMETER TYPES


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    app()
