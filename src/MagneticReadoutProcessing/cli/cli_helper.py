import typer
import MRPHal
import cli_datastorage


def __fix_import__fix_import():
    from pathlib import Path
    print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())



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