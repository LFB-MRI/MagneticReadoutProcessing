import numpy as np
import matplotlib.pyplot as plt
from collections import deque

import MRPReading, MRPAnalysis

class MRPDataVisualizationException(Exception):
    def __init__(self, message="MRPDataVisualizationException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPDataVisualization:

    @staticmethod
    def plot_error(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None):
        """
        Plots the deviation and mean values from several readings using two plots

        :param _readings:
        :type _readings: list(MRPReading.MRPReading)

        :param _title: title of the graphic
        :type _title: str

        :param _filename: export graphic to abs filepath with .png
        :type _filename: str
        """

        if _readings is None or len(_readings) <= 0:
            raise MRPDataVisualizationException("no readings in _reading given")


        # ERROR Bar Variables
        x: [int] = []
        y: [float] = []
        error: [float] = []


        # TABLE
        clust_data = []#np.random.random((len(_readings), 5))
        collabel = ("Reading [id:sensor_id]", "Mean", "STD Deviation", "Variance", "Data-Points")
        labels = []

        for idx, reading in enumerate(_readings):
            x.append(idx)

            labels.append('{}:{}'.format(reading.measurement_config.id, reading.measurement_config.sensor_id))

            mean = MRPAnalysis.MRPAnalysis.calculate_mean(reading)
            y.append(mean)

            deviation = MRPAnalysis.MRPAnalysis.calculate_std_deviation(reading)/2.0
            error.append(deviation)

            variance = MRPAnalysis.MRPAnalysis.calculate_variance(reading)

            clust_data.append(['{}:{}'.format(reading.measurement_config.id, reading.measurement_config.sensor_id),"{:.2f}".format(mean), "{:.2f}".format(deviation), "{:.2f}".format(variance), len(reading.data)])

        # error bar values w/ different -/+ errors
        #lower_error = 0.4 * error
        #upper_error = error
        #asymmetric_error = [lower_error, upper_error]

        fig, (ax0, ax1) = plt.subplots(2,1)

        fig.dpi = 300
        # Add a table at the bottom of the axes
        ax0.axis('tight')
        ax0.axis('off')
        ax0.set_title('{} - Error'.format(_title))
        tbl = ax0.table(cellText=clust_data, colLabels=collabel, loc='center')


        ax1.errorbar(x, y, yerr=error, fmt='o')
        ax1.set_xticks(range(0, len(_readings)), labels)
        ax1.set_xlabel("Reading [id:sensor_id]")
        ax1.set_ylabel("Error (Variance)")


        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()

    @staticmethod
    def plot_scatter(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None):
        """
        Plots a1 1d scatter plot of the reading data

        :param _readings:
        :type _readings: list(MRPReading.MRPReading)

        :param _title: title of the graphic
        :type _title: str

        :param _filename: export graphic to abs filepath with .png
        :type _filename: str
        """

        if _readings is None or len(_readings) <= 0:
            raise MRPDataVisualizationException("no readings in _reading given")

        x: [float] = []
        y: [int] = []
        labels: [str] = []
        coloring: [int] = []

        for idx, reading in enumerate(_readings):
            values = reading.to_value_array()
            labels.append('{}:{}'.format(reading.measurement_config.id, reading.measurement_config.sensor_id))
            # TODO USE deque()
            for v in values:
                y.append(idx)
                x.append(v)
                coloring.append('blue') # COLOR DOTS BLACK

            # ADD MEAN DOT
            y.append(idx)
            x.append(MRPAnalysis.MRPAnalysis.calculate_mean(reading))
            coloring.append('orange')  # COLOR MEAN DOT DIFFERENT




        plt.scatter(x, y, color=coloring)
        plt.title('{} - Scatter'.format(_title))
        plt.xlabel("values")
        plt.ylabel("reading [id:sensor_id]")
        plt.yticks(range(0, len(_readings)),  labels)

        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()
