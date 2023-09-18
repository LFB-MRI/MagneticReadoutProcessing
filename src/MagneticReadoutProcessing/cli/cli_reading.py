from typing import Optional
from typing_extensions import Annotated
from dataclasses import dataclass
#from dotenv import load_dotenv
import typer
import cli_helper
import cli_datastorage
import MRPHal
import os

from cli_sensor import connect_sensor_using_config

app = typer.Typer()

BASEPATH = os.path.dirname(__file__)+'/readings/'


def check_reading_configuration() ->bool:
    return False

@app.command()
def configure(ctx: typer.Context):
    cfg = cli_datastorage.CLIDatastorage()


    print("CONFIGURE READING")

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX)
    resp = typer.prompt("READING-NAME:", curr)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX, resp)

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
    if len(curr) <= 0:
        curr = BASEPATH
    resp = typer.prompt("OUTPUT-FOLDER",curr)

    if len(resp) <= 0 or not os.path.exists(resp):
        print("filepath invalid using: {} or specify again by running configure again".format(BASEPATH))
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER, BASEPATH)


    #READING_PREFIX = 2
    #READING_OUTPUT_FOLDER = 3
    #READING_DATAPOINT_COUNT = 4
    #READING_AVERAGE_COUNT = 5

    sensor_connection: MRPHal.MRPPHal = connect_sensor_using_config()
@app.command()
def run(ctx: typer.Context):

    # CReAte foLDER

    BASEPATH
    pass
    # Read CONFIg And CAPtUrE






@app.command()
def disconnect(ctx: typer.Context):
    cfg = cli_datastorage.CLIDatastorage()

    if len(cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH)) > 0:
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH, "")



@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    ctx.obj = cli_datastorage.Common()






if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()