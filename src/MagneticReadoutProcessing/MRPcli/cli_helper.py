import typer
from MRPcli import cli_datastorage
from MRP import MRPHal, MRPHalSerialPortInformation, MRPHalHelper



def __fix_import__fix_import():
    from pathlib import Path
    print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())




def create_hal_instance_using_config(_configname: str) -> MRPHal.MRPHal:
    cfg: cli_datastorage.CLIDatastorage = cli_datastorage.CLIDatastorage(_configname)

    path: str = cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH)
    name: str = cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_NAME)

    baudrate: int = 0
    try:
        baudrate = int(cfg.get_value(cli_datastorage.CLIDatastorageEntries.SENSOR_SERIAL_BAUDRATE))
    except Exception as e:
        print(str(e))

    if len(path) < 0:
        print("please connect sensor first using connect")
        raise typer.Abort("please connect sensor first using connect")




    device_path: MRPHalSerialPortInformation.MRPHalSerialPortInformation = MRPHalSerialPortInformation.MRPHalSerialPortInformation(_path=path, _name=name, _baudrate=baudrate)
    sensor_connection: MRPHal.MRPHal = MRPHalHelper.MRPHalHelper.createHalInstance(device_path)

    sensor_connection.connect()

    if not sensor_connection.is_connected():
        print("sensor connection failed, please check dialout permissions")
        raise typer.Abort("sensor connection failed, please check dialout permissions")

    return sensor_connection

