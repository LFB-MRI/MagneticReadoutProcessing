from typing import Optional
from tqdm import tqdm
import typer

import MRPHal

app = typer.Typer()

sensor_connection: MRPHal.MRPPHal

@app.command()
def connect_sensor(path: Optional[str] = None):

    device_path: MRPHal.MRPHalSerialPortInformation = None

    if path is None or len(path) <= 0:
        ports = MRPHal.MRPPHal.list_serial_ports()
        if len(ports) <= 0:
            raise typer.Abort("no connected sensors found")


        for idx, port in enumerate(ports):
            print("{} > {} - {}".format(idx, port.name, port.device_path))

        selected_sensor:int = -1
        while (not selected_sensor) or selected_sensor < 0:
            resp = typer.prompt("Please select one of the found sensors [0-{}]".format(len(ports)-1))
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


    if not device_path.is_valid():
        raise typer.Abort("given device path {} is not valid".format(device_path.device_path))


    # Open the port
    sensor_connection = MRPHal.MRPPHal(device_path)
    sensor_connection.connect()

    print(f"sensor connected: {sensor_connection.is_connected()}")







if __name__ == "__main__":
    app()