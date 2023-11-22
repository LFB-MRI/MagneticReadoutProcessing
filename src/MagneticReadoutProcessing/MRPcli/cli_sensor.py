from typing_extensions import Annotated
import typer
from MRPcli import cli_helper

from MRP import MRPHalLocal, MRPBaseSensor, MRPHal

app = typer.Typer()


@app.command()
def info(ctx: typer.Context, configname: Annotated[str, typer.Argument()]):

    sensor_connection: MRPHal.MRPHal = cli_helper.create_hal_instance_using_config(_configname=configname)

    print("SENSOR INFORMATION")
    print("NAME:".format(sensor_connection.current_port.name))
    print("ID: {}".format(sensor_connection.get_sensor_id()))
    print("CONNECTED SENSORS: {}".format(sensor_connection.get_sensor_count()))
    print("CAPABILITIES: {}".format(sensor_connection.get_sensor_capabilities()))

    sensor_connection.disconnect()


@app.command()
def query(ctx: typer.Context, configname: Annotated[str, typer.Argument()]):
    sensor_connection: MRPHal.MRPHal = cli_helper.create_hal_instance_using_config(_configname=configname)
    sensor_connection.connect()
    caps = sensor_connection.get_sensor_capabilities()
    if 'static' in caps:
        sensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(sensor_connection)
        # perform sensor readout
        sensor.query_readout()
        # iterate over result
        rtx = sensor_connection.get_sensor_count()
        for idx in range(rtx):
            print("QUERY RESULT FOR SENSOR_ID:{} SENSOR_NUMBER:{}".format(sensor_connection.get_sensor_id(), idx))
            print("> B:{}".format(sensor.get_b(_sensor_id=idx)))


            print("> TEMP:{}".format(sensor.get_temp(_sensor_id=idx)))
            
            if 'axis_x' in caps:
                print("> X:{}".format(sensor.get_reading(_axis='x', _sensor_id=idx)))
            if 'axis_y' in caps:
                print("> Y:{}".format(sensor.get_reading(_axis='y', _sensor_id=idx)))
            if 'axis_z' in caps:
                print("> Z:{}".format(sensor.get_reading(_axis='z', _sensor_id=idx)))

    sensor_connection.disconnect()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass


if __name__ == "__main__":
    app()
