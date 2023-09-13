import numpy as np
import matplotlib.pyplot as plt

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
        clust_data = np.random.random((len(_readings), 4))
        collabel = ("Mean", "STD Deviation", "Variance", "Data-Points")


        for idx, reading in enumerate(_readings):
            x.append(idx)

            mean = MRPAnalysis.MRPAnalysis.calculate_mean(reading)
            y.append(mean)

            deviation = MRPAnalysis.MRPAnalysis.calculate_std_deviation(reading)/2.0
            error.append(deviation)

            variance = MRPAnalysis.MRPAnalysis.calculate_variance(reading)

            clust_data[idx] = [mean, deviation, variance, len(reading.data)]

        # error bar values w/ different -/+ errors
        #lower_error = 0.4 * error
        #upper_error = error
        #asymmetric_error = [lower_error, upper_error]

        fig, (ax0, ax1) = plt.subplots(2,1)


        # Add a table at the bottom of the axes
        ax0.axis('tight')
        ax0.axis('off')
        ax0.set_title('{} - Error'.format(_title))
        tbl = ax0.table(cellText=clust_data, colLabels=collabel, loc='center')


        ax1.errorbar(x, y, yerr=error, fmt='o')
        ax1.set_xticks(range(0, len(_readings)))
        ax1.set_xlabel("Reading Index")
        ax1.set_ylabel("Error")





    # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename)
        else:
            plt.show()

        plt.close()

