import os
from pathlib import Path
from typing import Annotated
import typer
from UDPPFunctionTranslator import UDPPFunctionTranslator


app = typer.Typer()



@app.command()
def listfunctions(ctx: typer.Context):
    print(UDPPFunctionTranslator.listfunctions())

@app.command()
def run(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(str(Path(str(os.path.dirname(__file__))).parent.joinpath("pipelines")))


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    app()
