from typing import Annotated

import typer
import cli_helper
import cli_datastorage
import os

app = typer.Typer()




@app.command()
def run(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = ""):

    if configname is not None and len(configname) > 0:
        pass
    else:
        pass
        # load all json _config files

    # check config valid
    pass




@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    ctx.obj = cli_datastorage.Common()






if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()