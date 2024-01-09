from abc import ABC, abstractmethod
from MRP import MRPHal, MRPReading, MRPReadingSourceHelper


class MRPReadingSourceException(Exception):
    def __init__(self, message="MRPReadingSource thrown"):
        self.message = message
        super().__init__(self.message)


class MRPReadingSource(ABC):

    @staticmethod
    def createReadingSourceInstance(_hal: MRPHal.MRPHal):
        return MRPReadingSourceHelper.MRPReadingSourceHelper.createReadingSourceInstance(_hal)

    @abstractmethod
    def __init__(self, _hal: MRPHal.MRPHal):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def perform_measurement(self, _measurement_points: int, _average_readings_per_datapoint: int) -> [MRPReading.MRPReading]:
        pass

    @abstractmethod
    def export_visualisation(self, _readings: [MRPReading.MRPReading], _export_file: str):
        pass

