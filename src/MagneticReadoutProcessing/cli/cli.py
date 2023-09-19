import typer
import cli_datastorage
import cli_sensor
import cli_config
import cli_helper
import cli_measure


#load_dotenv()
app = typer.Typer(add_completion=True)
app.add_typer(cli_sensor.app, name="sensor")
app.add_typer(cli_config.app, name="config")
app.add_typer(cli_measure.app, name="measure")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass





if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()