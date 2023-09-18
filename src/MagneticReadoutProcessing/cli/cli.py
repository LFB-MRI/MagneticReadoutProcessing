import typer
import cli_datastorage
import cli_sensor

import cli_helper

#load_dotenv()
app = typer.Typer(add_completion=True)
app.add_typer(cli_sensor.app, name="sensor")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):

    storage = cli_datastorage.CLIDatastorage()
    storage.init()


    ctx.obj = cli_datastorage.Common()




if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()