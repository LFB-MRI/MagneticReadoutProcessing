from typing import Optional
from typing_extensions import Annotated
from dataclasses import dataclass
#from dotenv import load_dotenv
import typer
import cli_helper
import cli_datastorage
import MRPHal

app = typer.Typer()


def connect_sensor_using_config() -> MRPHal.MRPPHal:
    cfg = cli_datastorage.CLIDatastorage()

    path = cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH)
    name = cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_NAME)
    if len(path) < 0:
        raise typer.Abort("please connect sensor first using connect")

    device_path = MRPHal.MRPHalSerialPortInformation(_path=path, _name=name)

    if not device_path.is_valid():
        raise typer.Abort("invalid sensor config, please re-run connect command")

    sensor_connection = MRPHal.MRPPHal(device_path)
    sensor_connection.connect()

    if not sensor_connection.is_connected():
        raise typer.Abort("sensor connection failed, please check dialout permissions")

    return sensor_connection

@app.command()
def info(ctx: typer.Context):

    sensor_connection: MRPHal.MRPPHal = connect_sensor_using_config()

    print("SENSOR INFORMATION")
    print("NAME:".format(sensor_connection.current_port.name))
    print("ID: {}".format(sensor_connection.get_sensor_id()))
    print("CONNECTED SENSORS: {}".format(sensor_connection.get_sensor_count()))
    print("CAPABILITIES: {}".format(sensor_connection.get_sensor_capabilities()))



    sensor_connection.disconnect()








@app.command()
def disconnect(ctx: typer.Context):
    cfg = cli_datastorage.CLIDatastorage()

    if len(cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH)) > 0:
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH, "")

@app.command()
def connect(ctx: typer.Context, path: Optional[str] = None):

    device_path: MRPHal.MRPHalSerialPortInformation = None
    # If not defualt path is given by the  user promt the user with a list of ports
    if path is None or len(path) <= 0:
        ports = MRPHal.MRPPHal.list_serial_ports()
        if len(ports) <= 0:
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
        device_path =ports[selected_sensor]
        print("selected sensor: {} - {}".format(device_path.name, device_path.device_path))

    else:
        device_path = MRPHal.MRPHalSerialPortInformation(_path=path)

    # check for valid device path if user specified
    if not device_path.is_valid():
        raise typer.Abort("given device path {} is not valid".format(device_path.device_path))


    # TEST CONNECTION
    sensor_connection = MRPHal.MRPPHal(device_path)
    sensor_connection.connect()
    print(f"sensor connected: {sensor_connection.is_connected()}")
    sensor_connection.disconnect()

    # UPDATE CONFIG
    cfg = cli_datastorage.CLIDatastorage()
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH, device_path.device_path)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_NAME, device_path.name)





@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    ctx.obj = cli_datastorage.Common()




if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()