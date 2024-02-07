from typing import Annotated, Optional
import typer

from MRPcli import cli_datastorage
import os
from pathlib import Path

from MRP import MRPMagnetTypes, MRPHal, MRPHalSerialPortInformation, MRPHalHelper

app = typer.Typer()

BASEPATH: str = '../readings'

@app.command()
def list(ctx: typer.Context):
    print("FOUND CONFIGURATIONS IN {}".format(cli_datastorage.CLIDatastorage.get_config_basepath()))
    for idx, e in enumerate(cli_datastorage.CLIDatastorage.list_configs()):
        print("{}> {}".format(idx, e))


@app.command()
def setup(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = ""):
    cfg = cli_datastorage.CLIDatastorage(configname)


    print("CONFIGURE READING")

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX)
    if len(curr) <= 0:
        curr = configname
    resp = typer.prompt("READING-NAME:", curr)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX, resp)

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
    if len(curr) <= 0:
        curr = cli_datastorage.CLIDatastorageConfig.get_basepath()
    resp = typer.prompt("OUTPUT-FOLDER", curr)

    if len(curr) <= 0:
        print("user response empty: so setting the default path")
        resp = cli_datastorage.CLIDatastorageConfig.get_basepath()
    # REL TO ABS PATHS

    # TRY TO CREATE FOLDER
    path_to_create = resp
    if not str(resp).startswith('/'):
        path_to_create = str(Path(cli_datastorage.CLIDatastorageConfig.get_basepath()).joinpath(Path(resp).resolve()))

    if not os.path.exists(path_to_create):
        if typer.prompt("Should now try to create the path {} ?  [y/n]".format(path_to_create), 'y') == 'y':
            Path(path_to_create).mkdir(parents=True, exist_ok=True)
        if not os.path.exists(path_to_create):
            print("note folder does not exists: {}. please create first before running a measurement cycle".format(path_to_create))
    else:
        print("final output path for reading {}".format(path_to_create))

    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER, resp)



    print("SUPPORTED MAGNET TYPES")
    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_MAGNET_TYPE)
    if len(curr) <= 0:
        curr = 0
    for idx, magnet in enumerate(MRPMagnetTypes.MagnetType):
        print("{} > {}".format(magnet.value, magnet.name))

    selected_magnet: int = 0
    while (not selected_magnet) or selected_magnet < 0:
        # DISPLAY USER MESSAGE
        resp: int = -1
        try:
            resp = int(typer.prompt("Please select one of the listed magnet types [0-{}]".format(len(MRPMagnetTypes.MagnetType) - 1), curr))
        except Exception as e:
            continue
        # EVALUATE USER INPUT
        if resp >= 0 and resp <= (len(MRPMagnetTypes.MagnetType) - 1):
            break
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_MAGNET_TYPE, str(resp))




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
def setupsensor(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = "", path: Optional[str] = None, exclude_network_sensors: bool = False):

    device_path: MRPHalSerialPortInformation.MRPHalSerialPortInformation = None


    # If the user gives no default path, prompt with a list of ports
    if path is None or len(path) <= 0:
        ports = MRPHalSerialPortInformation.MRPHalSerialPortInformation.list_serial_ports()

        if not exclude_network_sensors:
            network_ports = MRPHalSerialPortInformation.MRPHalSerialPortInformation.list_remote_serial_ports()
            ports = [*ports, *network_ports]

        if len(ports) <= 0:
            print("no connected sensors found")
            raise typer.Abort("no connected sensors found")


        for idx, port in enumerate(ports):
            print("{} > {} - {}".format(idx, port.name, port.device_path))

        selected_sensor: int = -1
        while selected_sensor < 0:
            # DISPLAY USER MESSAGE
            if len(ports) == 1:
                resp = typer.prompt("Please select one of the found sensors: 1 ".format(len(ports) - 1), default="0")
            else:
                resp = typer.prompt("Please select one of the found sensors: 0-{} ".format(len(ports)-1))
            # EVALUATE USER INPUT
            if resp and len(resp) > 0:
                try:
                    selected_sensor = int(resp)
                    if selected_sensor < len(ports) and selected_sensor >= 0:
                        break
                except Exception as e:
                    selected_sensor = -1

            elif len(ports) == 1:
                selected_sensor = 0
                break


        #  ASSIGN
        device_path = ports[selected_sensor]
        print("selected sensor: {} - {}".format(device_path.name, device_path.device_path))

    else:
        device_path = MRPHalSerialPortInformation.MRPHalSerialPortInformation(_path=path)

    # check for valid device path if user specified
    if not device_path.is_valid():
        print("given device path {} is not valid".format(device_path.device_path))
        raise typer.Abort("given device path {} is not valid".format(device_path.device_path))


    # TEST CONNECTION
    sensor_connection = MRPHalHelper.MRPHalHelper.createHalInstance(device_path)

    sensor_connection.connect()
    print("sensor connected: {} ID:{}".format(sensor_connection.is_connected(), sensor_connection.get_sensor_id()))
    sensor_connection.disconnect()

    # UPDATE CONFIG
    cfg = cli_datastorage.CLIDatastorage(configname)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH, device_path.device_path)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_NAME, device_path.name)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_BAUDRATE, str(sensor_connection.current_port.baudrate))
    print("SENSOR SETUP COMPLETE: {}".format(cfg.config_filepath()))


@app.command()
def reset(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = ""):
    cfg = cli_datastorage.CLIDatastorage(configname)
    cfg.reset()
    print("READING CONFIG RESET SUCCESS".format(cfg.config_filepath()))


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass


if __name__ == "__main__":
    app()