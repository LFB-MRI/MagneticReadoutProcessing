from typing import Optional
from typing_extensions import Annotated
from dataclasses import dataclass
#from dotenv import load_dotenv
import typer
import cli_helper
import cli_datastorage
import MRPHal
import MRPBaseSensor
app = typer.Typer()


def connect_sensor_using_config(_configname: str) -> MRPHal.MRPPHal:
    cfg = cli_datastorage.CLIDatastorage(_configname)

    path = cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH)
    name = cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_NAME)
    if len(path) < 0:
        print("please connect sensor first using connect")
        raise typer.Abort("please connect sensor first using connect")

    device_path = MRPHal.MRPHalSerialPortInformation(_path=path, _name=name)

    if not device_path.is_valid():
        print("invalid sensor config, please re-run connect command")
        raise typer.Abort("invalid sensor config, please re-run connect command")

    sensor_connection = MRPHal.MRPPHal(device_path)
    sensor_connection.connect()

    if not sensor_connection.is_connected():
        print("sensor connection failed, please check dialout permissions")
        raise typer.Abort("sensor connection failed, please check dialout permissions")

    return sensor_connection

@app.command()
def info(ctx: typer.Context, configname: Annotated[str, typer.Argument()]):

    sensor_connection: MRPHal.MRPPHal = connect_sensor_using_config(_configname=configname)

    print("SENSOR INFORMATION")
    print("NAME:".format(sensor_connection.current_port.name))
    print("ID: {}".format(sensor_connection.get_sensor_id()))
    print("CONNECTED SENSORS: {}".format(sensor_connection.get_sensor_count()))
    print("CAPABILITIES: {}".format(sensor_connection.get_sensor_capabilities()))



    sensor_connection.disconnect()



@app.command()
def query(ctx: typer.Context, configname: Annotated[str, typer.Argument()]):

    sensor_connection: MRPHal.MRPPHal = connect_sensor_using_config(_configname=configname)

    if 'static' in sensor_connection.get_sensor_capabilities():
        sensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(sensor_connection)
        print("> B:{}".format(sensor.get_b()))
        print("> XYZ:{}".format(sensor.get_vector()))
        print("> TEMP:{}".format(sensor.get_temp()))
    else:
        print("sensor readout for this type isn't currently implemented")
        raise typer.Abort("sensor readout for this type isn't currently implemented")

    sensor_connection.disconnect()







@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass




if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()