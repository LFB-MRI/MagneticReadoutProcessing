import random
import signal
import string
import time
from typing import Annotated
import typer
import socket
import sys
import os


app = typer.Typer()

terminate: bool = False


def signal_andler(signum, frame):
    global terminate
    terminate = True
    time.sleep(4)
    exit(1)


signal.signal(signal.SIGINT, signal_andler)


def getMachine_addr():
    os_type = sys.platform.lower()
    command: str = ""
    if "linux" in os_type:
        command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
        #command = "ioreg -l | grep IOPlatformSerialNumber"
        command = "cat /proc/cpuinfo | grep Serial"
    elif "windows" in os_type:
        command = "wmic bios get serialnumber"

    if len(command) > 0:
        return os.popen(command).read().strip("\n \"=|:").replace("IOPlatformSerialNumber", "").replace("Serial", "")

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

@app.command()
def start(ctx: typer.Context, advertised_port: Annotated[int, typer.Argument()] = 10001,
          advertised_sensor_id: Annotated[str, typer.Argument()] = ""):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', 9434)

    sock.bind(server_address)
    if len(advertised_sensor_id) <= 0:
        advertised_sensor_id = getMachine_addr()
    response = 'pfgipresponseserv_{}_{}'.format(advertised_port, advertised_sensor_id)
    print("configured: {} starting udp broadcast {}".format(response, 9434))
    while (not terminate):

        if typer.prompt("Terminate  [Y/n]", 'y') == 'y':
            break

        data, address = sock.recvfrom(4096)
        data = str(data.decode('UTF-8'))
        # print('Received ' + str(len(data)) + ' bytes from ' + str(address))
        # print('Data:' + data)

        if data == 'pfg_ip_broadcast_cl':
            print('responding...')
            sent = sock.sendto(response.encode(), address)
            # print('Sent confirmation back')

        time.sleep(0.1)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass


if __name__ == "__main__":
    app()
