import MRPReading

class MRPDataVisualizationException(Exception):
    def __init__(self, message="MRPDataVisualizationException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPDataVisualization:

    @staticmethod
    def plot_symetrical_error(_reading: MRPReading.MRPReading, _filename: str = None):
        pass

    @staticmethod
    def plot_asymetric_error(_reading: MRPReading.MRPReading, _filename: str = None):
        pass

