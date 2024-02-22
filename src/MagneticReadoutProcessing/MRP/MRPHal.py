from abc import ABC, abstractmethod

from MRP import MRPHalSerialPortInformation


class MRPHalException(Exception):
    def __init__(self, message="MRPHalException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPHal(ABC):

    @abstractmethod
    def __init__(self, _selected_port: MRPHalSerialPortInformation, _type: MRPHalSerialPortInformation.MRPRemoteSensorType = MRPHalSerialPortInformation.MRPRemoteSensorType.Unknown):
        pass
    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def set_serial_port_information(self, _port: MRPHalSerialPortInformation):
        pass

    def get_serial_port_information(self) ->MRPHalSerialPortInformation:
        pass

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @staticmethod
    def read_value(self):
        pass

    @abstractmethod
    def send_command(self, _cmd: str) -> [str]:
        pass

    @abstractmethod
    def query_command_str(self, _cmd: str) -> str:
        pass

    @abstractmethod
    def query_command_int(self, _cmd: str) -> int:
        pass

    @abstractmethod
    def query_command_float(self, _cmd: str) -> float:
        pass

    @abstractmethod
    def get_sensor_id(self) -> str:
        pass

    @abstractmethod
    def get_sensor_count(self) -> int:
        pass

    @abstractmethod
    def get_sensor_capabilities(self) -> [str]:
        pass

    @abstractmethod
    def get_sensor_commandlist(self) -> [str]:
        pass

    @abstractmethod
    def get_sensor_names(self) -> [str]:
        pass
