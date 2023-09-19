from typing import Annotated, Optional

import typer

import MRPHal
import cli_helper
import cli_datastorage
import os

app = typer.Typer()

BASEPATH = os.path.dirname(__file__)+'/'


@app.command()
def list(ctx: typer.Context):
    cfg = cli_datastorage.CLIDatastorage()
    print("FOUND CONFIGURATIONS IN {}".format(cli_datastorage.CLIDatastorage.get_config_basepath()))
    for idx, e in enumerate(cfg.list_configs()):
        print("{}> {}".format(idx, e))


@app.command()
def setup(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = ""):
    cfg = cli_datastorage.CLIDatastorage(configname)


    print("CONFIGURE READING")

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX)
    resp = typer.prompt("READING-NAME:", curr)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX, resp)

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
    if len(curr) <= 0:
        curr = BASEPATH
    resp = typer.prompt("OUTPUT-FOLDER", curr)

    if len(curr) <= 0:
        print("user response empty: so setting the default path")
        resp = BASEPATH

    if not os.path.exists(resp):
        print("note folder does not exists: {}. please create first before running a measurement cycle".format(BASEPATH))
    if not os.path.exists(resp):
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER, resp)



    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT)
    if len(curr) <= 0:
        curr = 1
    resp = int(typer.prompt("NUMBER DATAPOINTS:", curr))
    if resp <= 0:
        print("invalid number for datapoints to collect: minimum is 1".format(1))
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT, "1")
    else:
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT, str(resp))



    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT)
    if len(curr) <= 0:
        curr = 1
    resp = int(typer.prompt("NUMBER AVERAGE READINGS PER DATAPOINT:", curr))
    if resp <= 0:
        print("invalid number for number readings per datapoint : minimum is 1".format(1))
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT, "1")
    else:
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT, str(resp))

    print("MEASUREMENT SETUP COMPLETE: {}".format(cfg.config_filepath()))



@app.command()
def setupsensor(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = "", path: Optional[str] = None):

    device_path: MRPHal.MRPHalSerialPortInformation = None
    # If the user gives no default path, prompt with a list of ports
    if path is None or len(path) <= 0:
        ports = MRPHal.MRPPHal.list_serial_ports()
        if len(ports) <= 0:
            print("no connected sensors found")
            raise typer.Abort("no connected sensors found")


        for idx, port in enumerate(ports):
            print("{} > {} - {}".format(idx, port.name, port.device_path))

        selected_sensor:int = -1
        while (not selected_sensor) or selected_sensor < 0:
            # DISPLAY USER MESSAGE
            if len(ports) == 1:
                resp = typer.prompt("Please select one of the found sensors [0]".format(len(ports) - 1))
            else:
                resp = typer.prompt("Please select one of the found sensors [0-{}]".format(len(ports)-1))
            # EVALUATE USER INPUT
            if resp and len(resp) > 0:
                try:
                    selected_sensor = int(resp)
                    if selected_sensor < len(ports) and selected_sensor >= 0:
                        break
                except Exception as e:
                    selected_sensor = -1

        #  ASSIGN
        device_path = ports[selected_sensor]
        print("selected sensor: {} - {}".format(device_path.name, device_path.device_path))

    else:
        device_path = MRPHal.MRPHalSerialPortInformation(_path=path)

    # check for valid device path if user specified
    if not device_path.is_valid():
        print("given device path {} is not valid".format(device_path.device_path))
        raise typer.Abort("given device path {} is not valid".format(device_path.device_path))


    # TEST CONNECTION
    sensor_connection = MRPHal.MRPPHal(device_path)
    sensor_connection.connect()
    print("sensor connected: ".format(sensor_connection.is_connected()))
    sensor_connection.disconnect()

    # UPDATE CONFIG
    cfg = cli_datastorage.CLIDatastorage(configname)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH, device_path.device_path)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_NAME, device_path.name)

    print("SENSOR SETUP COMPLETE: {}".format(cfg.config_filepath()))



@app.command()
def reset(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = ""):
    cfg = cli_datastorage.CLIDatastorage(configname)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH, "")
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_NAME, "")
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX, "")
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER, BASEPATH)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT, "1")
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT, "1")
    print("READING CONFIG RESET SUCCESS".format(cfg.config_filepath()))




@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()