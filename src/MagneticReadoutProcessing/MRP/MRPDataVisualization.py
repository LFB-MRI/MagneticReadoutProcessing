""" collection of reading data plotting functions """
import math
import re

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec, mlab
import scipy.optimize as opt
import matplotlib.scale as mscale
from MRP import MRPReading, MRPAnalysis, MRPDataVisualisationHelper

class MRPDataVisualizationException(Exception):
    def __init__(self, message="MRPDataVisualizationException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPDataVisualization:

    @staticmethod
    def linear_curve_func(x, a, b):
        return a*x + b
    @staticmethod
    def plot_temperature_deviation(_readings: [MRPReading.MRPReading], max_value: float = None, min_value: float = None, _title: str = '', _filename: str = None, _uni_temp: str = "°C", _unit_mag: str = "$\mu$T"):
        """
        Plots the temperature deviation  several readings

        :param _readings:
        :type _readings: list(MRPReading.MRPReading)

        :param _title: title of the graphic
        :type _title: str

        :param _filename: export graphic to abs filepath with .png
        :type _filename: str
        """
        if _readings is None or len(_readings) <= 0:
            raise MRPDataVisualizationException("no readings in _reading given")
        elif len(_readings) <= 3:
            raise MRPDataVisualizationException("_readings list need at least three entries")



        fig = plt.figure()
        fig.suptitle('{}'.format(_title), fontsize=10)

        gs = gridspec.GridSpec(1, 1)



        raw_y = []
        xlabels = []
        raw_plot = plt.subplot(gs[0, :])
        raw_plot.set_xlabel('Temperature {}'.format(_uni_temp), fontsize=8)
        raw_plot.set_ylabel('Sensor Raw Value [{}]'.format(_unit_mag), fontsize=8)

        zero_offset: float = 0.0
        for reading in _readings:
            zero_offset = min([zero_offset, abs(MRPAnalysis.MRPAnalysis.calculate_mean(reading))])


        min_temp: int = 1000000
        max_temp: int = -1000000


        temps: [int] = []
        for r in _readings:
            mean: float = MRPAnalysis.MRPAnalysis.calculate_mean(r)
            raw_y.append(zero_offset-mean)
            temperature = "-"
            was_in :bool = False
            for ne in r.get_name().split("_"):
                if ne.startswith("TEMPERATURE="):
                    temperature = ne.split("TEMPERATURE=")[1]
                    was_in = True
                    temps.append(int(temperature))

                    max_temp = max([max_temp, int(temperature)])
                    min_temp = min([min_temp, int(temperature)])

            if not was_in:
                temps.append(0)
            xlabels.append("{}".format(temperature, _uni_temp))

        raw_y = [v for _, v in sorted(zip(temps, raw_y))]
        #raw_y = raw_y.reverse()

        xlabels = [v for _, v in sorted(zip(temps, xlabels))]
        temps = [v for _, v in sorted(zip(temps, temps))]


        # FILL FRONT UP
        raw_x = np.linspace(min([min_temp, 0]), max_temp, max_temp, dtype=np.int32)
        needed_fill_up_values = min([min_temp]) - 0
        v_to_add = raw_y[0]
        for i in range(needed_fill_up_values-1):
           raw_y.insert(0, v_to_add)
        raw_plot.plot(raw_x, raw_y, linewidth=0.8, label="Raw Values") #label='Raw Values at {}{} with '.format(temperature, _uni_temp) + '$\mu_'+'{'+ 'mtd{}'.format(temperature) +'}'+'={:.2f}${}'.format(mean, _unit_mag))





        max_temp_dev: float = 0.0
        temp_dev_mean: float = 0.0
        for i in range(0, len(temps) - 1):
            temp_diff: float = temps[i+1] - temps[i]
            mag_diff: float = raw_y[i+1] - raw_y[i]

            u_per_c: float = mag_diff / temp_diff

            temp_dev_mean = temp_dev_mean + u_per_c
            max_temp_dev = min(max_temp_dev, u_per_c)

        temp_dev_mean = temp_dev_mean / len(temps)


        raw_plot.axhline(y=raw_y[0], color='red', linestyle='--', linewidth=1, label='Ideal baseline $\mu_{bl}$=' + '{:.2f}{}'.format(raw_y[0], _unit_mag))

        try:
            opt_params, pcov = opt.curve_fit(MRPDataVisualization.linear_curve_func, raw_x[needed_fill_up_values:], raw_y[needed_fill_up_values:])
            a = opt_params[0]
            b = opt_params[1]
            ideal_y: [float] = []

            temp_dev_mean = a

            for xe in raw_x[needed_fill_up_values:]:
                ideal_y.append(MRPDataVisualization.linear_curve_func(xe, a, b))
            v_to_add = ideal_y[0]
            for i in range(needed_fill_up_values):
                ideal_y.insert(0, v_to_add)
            raw_plot.plot(raw_x, ideal_y, linewidth=0.5, color='orange', linestyle='--', label='Fitted curve f(c)={:.2f}c+'.format(temp_dev_mean) + "$\mu_{bl}$")
        except Exception as e:
            pass

        raw_plot.set_title("With maximum deviation of d={:.2f}{}/{} and ".format(max_temp_dev, _unit_mag, _uni_temp) + "$\mu_{td}$" + "={:.2f}{}/{}".format(temp_dev_mean, _unit_mag, _uni_temp), fontsize=7)

        raw_plot.set_xlim([min_temp, max_temp])
        #raw_plot.set_xticks([min_temp, max_temp])
        #raw_plot.set_xticks(raw_x[needed_fill_up_values:], raw_x[needed_fill_up_values:], fontsize=5)
        if min_value is not None and max_value is not None:
            raw_plot.set_ylim(min_value, max_value)
        #else:
        #    raw_plot.set_ylim([min(raw_y)*1.3, max(raw_y)*1.3])
        raw_plot.legend(fontsize=7)


        fig.tight_layout()
        plt.interactive(False)
        #plt.show()
        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()

    @staticmethod
    def inverse_proportional_curve_func(x, a, b, c):
        return a * np.exp(-b * x) + c
    @staticmethod
    def plot_linearity(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None, _unit: str = "$\mu$T", _as_linear_fkt: bool = False, _max_y: int = None,_min_y: int = None):
        """
        Plots the linearity from several readings

        :param _readings:
        :type _readings: list(MRPReading.MRPReading)

        :param _title: title of the graphic
        :type _title: str

        :param _filename: export graphic to abs filepath with .png
        :type _filename: str
        """
        if _readings is None or len(_readings) <= 0:
            raise MRPDataVisualizationException("no readings in _reading given")

        x = list(range(len(_readings)))
        xlabels: [str] = []
        distance_array: [float] = []
        avg = "1000"
        zero_offset: float = 0.0
        for reading in _readings:
            zero_offset = min([zero_offset, abs(MRPAnalysis.MRPAnalysis.calculate_mean(reading))])



        for reading in _readings:
            name: str = reading.get_name().replace(".mag.json", "").split("_")
            distance_was_in: bool = False
            for n in name:
                if 'DISTANCE=' in n:
                    distance_was_in = True
                    d = n.split('DISTANCE=')[1]
                    xlabels.append(d)

                    distance_array.append(int(re.findall(r'\d+', d)[0]))
                elif 'AVG' in n:
                    avg = avg.split('AVG=')[1]
            if not distance_was_in:
                xlabels.append('0mm')
                distance_array.append(0)


        y: [float] = []
        for reading in _readings:
            y.append(zero_offset - MRPAnalysis.MRPAnalysis.calculate_mean(reading))

        #min_value = abs(min(y))
        y = [abs(e) for e in y]
        #raw_y = _reading.to_value_array()



        #RESORT ARRAY TO DISTANCE
        y = [v for _,v in sorted(zip(distance_array, y))]



        # Create 2x2 sub plots
        gs = gridspec.GridSpec(1, 1)

        if _as_linear_fkt:
            mscale.register_scale(MRPDataVisualisationHelper.SquareRootScale)


        fig = plt.figure()
        fig.suptitle('{}'.format(_title), fontsize=10)

        distance_plot = plt.subplot(gs[0, 0])

        distance_plot.set_xlabel('Distance between sensor IC package and N45 12x12x12mm cubic magnet [mm]', fontsize=8)
        distance_plot.set_ylabel('Sensor mean value $\mu_{nl}$ ['+ _unit + '] using ' + avg + ' samples per captured datapoint', fontsize=8)

        if len(xlabels) < 20:
            distance_plot.set_xticklabels(xlabels)

        distance_plot.plot(x, y, linewidth=0.8, linestyle='-', label='Sensor Value')

        #plt.show()
        try:
            opt_params, pcov = opt.curve_fit(MRPDataVisualization.inverse_proportional_curve_func, x, y)
            a = opt_params[0]
            b = opt_params[1]
            c = opt_params[2]
            ideal_y: [float] = []

            for xe in x:
                ideal_y.append(MRPDataVisualization.inverse_proportional_curve_func(xe, a, b, c))
            distance_plot.plot(x, ideal_y, linewidth=0.5, color='red', linestyle='--', label='Ideal curve')
        except Exception as e:
            pass




        deviation: [float] = []
        deviation_ut: [float] = []
        for idx, xe in enumerate(x):
            t = abs(1.0 - (ideal_y[idx] / y[idx]))
            deviation_ut.append(t * ideal_y[idx])
            deviation.append(t)

        deviation_mu: float = np.sum(deviation) / len(deviation)
        deviation__ut_mu: float = np.sum(deviation_ut) / len(deviation_ut)

        deviation_variance: float = 0
        for value in deviation:
            deviation_variance += value ** 2

        sigma: float = np.sqrt(deviation_variance)
        distance_plot.set_title('Sensor linearity with mean deviation $\mu_{sl}' + '={:.2f}$% ({:.2f}{}) '.format(deviation_mu, deviation__ut_mu, _unit) + 'and $\sigma_{sl}' + '={:.2f}$% from ideal curve'.format(sigma), fontsize=8)
        distance_plot.legend(loc='lower left', fontsize=8)

        if _max_y is not None:
            distance_plot.set_ylim([0, _max_y])
        if _min_y is not None and _max_y is not None:
            distance_plot.set_ylim([_min_y, _max_y])

        if _as_linear_fkt:
            distance_plot.set_yscale('squareroot')

        fig.tight_layout()
        plt.interactive(False)
        # plt.show()
        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()

    @staticmethod
    def plot_histogram(_reading: MRPReading.MRPReading, _title: str = '', _filename: str = None, _unit: str = "$\mu$T"):
        """
        Plots the histogram and line plot of an reading

        :param _readings:
        :type _readings: list(MRPReading.MRPReading)

        :param _title: title of the graphic
        :type _title: str

        :param _filename: export graphic to abs filepath with .png
        :type _filename: str
        """

        if _reading is None:
            raise MRPDataVisualizationException("no reading given")

        raw_x = np.linspace(0, _reading.len(), _reading.len(), dtype=np.int32)
        raw_y = _reading.to_value_array()

        mean: float = MRPAnalysis.MRPAnalysis.calculate_mean(_reading)
        raw_stddeviation: float = MRPAnalysis.MRPAnalysis.calculate_std_deviation(_reading)
        noise_y: [float] = []

        for v in raw_y:
            deviation = v - mean
            noise_y.append(deviation)

        noise_mean: float = np.sum(noise_y) / len(noise_y)
        noise_variance: float = 0
        for value in noise_y:
            noise_variance += (noise_mean - value) ** 2
        noise_variance = noise_variance / len(noise_y)




        # Create 2x2 sub plots
        gs = gridspec.GridSpec(3, 2)


        fig = plt.figure()
        fig.suptitle('{}'.format(_title), fontsize=12)








        raw_plot = plt.subplot(gs[0, :])
        raw_plot.plot(raw_x, raw_y, linewidth=0.8, label='Raw Values')
        ylim = max(abs(raw_y.max()), abs(raw_y.min())) * 1.3
        raw_plot.set_xlim([0, _reading.len()])
        raw_plot.axhline(y=mean, color='red', linestyle='--', linewidth=1, label='Sensor Raw Mean $\mu_{rv}$')
        raw_plot.set_xlabel('Data-Point Index', fontsize=8)
        raw_plot.set_ylabel('Raw Value\n[{}]'.format(_unit), fontsize=8)
        raw_plot.set_title('Raw Sensor Values $\mu_{rv}'+'={:.2f}${}'.format(MRPAnalysis.MRPAnalysis.calculate_mean(_reading), _unit) + '   $\sigma_{rv}$'+'={:.2f}{}'.format(raw_stddeviation, _unit), fontsize=9)
        raw_plot.legend(fontsize=4)





        # ADD HEATMAP COLORPLOT
        temperature_plot = plt.subplot(gs[2, :])
        temperature_mean: float = (np.sum(_reading.to_temperature_value_array())/_reading.len())
        temperature_plot.plot(raw_x, _reading.to_temperature_value_array(), linewidth=0.8, label='Sensor Raw Temperature')
        temperature_plot.set_xlim([0, _reading.len()])
        temperature_plot.axhline(y=temperature_mean, color='red', linestyle='--', linewidth=1, label='Temperature Mean $\mu_{t}$')
        temperature_plot.set_xlabel('Data-Point Index', fontsize=7)
        temperature_plot.set_ylabel('Temperature\n[$^\circ\mathrm{C}$]', fontsize=7)
        temperature_plot.set_title('Sensor Temperature $\mu_{t}'+'={:.2f}$'.format(temperature_mean) + '$^\circ\mathrm{C}$'+'   $\sigma_{t}$'+'={:.2f}'.format(MRPAnalysis.MRPAnalysis.calculate_std_deviation(_reading, True), _unit) + '$^\circ\mathrm{C}$', fontsize=8)
        temperature_plot.legend(fontsize=3)

        box_plot = plt.subplot(gs[1, 1])
        ##### Set style options here #####
        boxprops = dict(linestyle='-', linewidth=1.0, color='#00145A')
        flierprops = dict(marker='o', markersize=1,
                          linestyle='none')
        whiskerprops = dict(color='#fe7f2e')
        capprops = dict(color='#fe7f2e')
        medianprops = dict(linewidth=1.0, linestyle='-', color='#fe161d')

        box_plot.boxplot(raw_y, vert=False, notch=False, boxprops=boxprops, whiskerprops=whiskerprops,capprops=capprops, flierprops=flierprops, medianprops=medianprops,showmeans=False)
        box_plot.set_title('Boxplot'.format(), fontsize=8)
        box_plot.set_xlabel('Raw Sensor Values [{}]'.format(_unit), fontsize=8)
        box_plot.set_yticklabels([""])
        box_plot.tick_params(left=False)
        box_plot.xaxis.set_ticks_position('none')


        hist_plot = plt.subplot(gs[1, 0])
        hist_mu: float = MRPAnalysis.MRPAnalysis.calculate_mean(_reading)
        hist_sigma: float = MRPAnalysis.MRPAnalysis.calculate_std_deviation(_reading)
        num_bins: int = int(math.log(_reading.len()) * 4)
        ## the histogram of the data
        n, bins, patches = hist_plot.hist(raw_y, num_bins, density=True)
        ## add a 'best fit' line
        hist_best_fit_y = ((1 / (np.sqrt(2 * np.pi) * hist_sigma)) * np.exp(-0.5 * (1 / hist_sigma * (bins - hist_mu)) ** 2))
        hist_plot.plot(bins, hist_best_fit_y, '--', linewidth=0.8, label='Standard Deviation $\sigma_{nl}$')
        hist_plot.set_ylabel('Raw Value [{}]'.format(_unit), fontsize=7)
        hist_plot.axvline(hist_mu, color='red', linestyle='--', linewidth=1, label='Sensor Raw Mean $\mu_{rv}$')
        hist_plot.set_ylabel('Probability\ndensity', fontsize=7)
        hist_plot.set_title('Histogram using {} bins'.format( num_bins), fontsize=8)
        hist_plot.set_xlabel('Raw Sensor Values [{}]'.format(_unit), fontsize=8)
        hist_plot.legend(fontsize=4)


        fig.tight_layout()
        #fig.legend()


        #
        plt.interactive(False)
        #plt.show()

        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()

    @staticmethod
    def plot_error(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None, _unit: str = "$\mu$T"):
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
        collabel = ("Reading [id:sensor_id]", "Mean [{}]".format(_unit), "STD Deviation [{}]".format(_unit), "Variance [{}]".format(_unit), "Count Data-Points")
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

        fig.dpi = 1200
        # Add a table at the bottom of the axes
        ax0.axis('tight')
        ax0.axis('off')
        ax0.set_title('{} Error'.format(_title))
        tbl = ax0.table(cellText=clust_data, colLabels=collabel, loc='center')


        ax1.errorbar(x, y, yerr=error, fmt='o')
        ax1.set_xticks(range(0, len(_readings)), labels)
        ax1.set_xlabel("Reading [id:sensor_id]")
        ax1.set_ylabel("Error (Variance) [{}]".format(_unit))


        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()

    @staticmethod
    def plot_scatter(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None, _unit: str = "$\mu$T"):
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
        plt.title('{} Scatter'.format(_title))
        plt.xlabel("value [{}]".format(_unit))
        plt.ylabel("reading [id:sensor_id]")
        plt.yticks(range(0, len(_readings)),  labels)

        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()

    @staticmethod
    def plot_temperature(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None, _unit: str = "°C"):
        """
        Plots a temperature plot of the reading data

        :param _readings:
        :type _readings: list(MRPReading.MRPReading)

        :param _title: title of the graphic
        :type _title: str

        :param _filename: export graphic to abs filepath with .png
        :type _filename: str
        """

        if _readings is None or len(_readings) <= 0:
            raise MRPDataVisualizationException("no readings in _reading given")
        num_readings = len(_readings)

        # TABLE
        clust_data = []  # np.random.random((len(_readings), 5))
        collabel = ("Reading [id:sensor_id]", "Mean [{}]".format(_unit), "STD Deviation [{}]".format(_unit), "Variance [{}]".format(_unit), "Count Data-Points")
        labels = []

        for idx, reading in enumerate(_readings):

            labels.append('{}:{}'.format(reading.measurement_config.id, reading.measurement_config.sensor_id))

            mean = MRPAnalysis.MRPAnalysis.calculate_mean(reading, _temperature_axis=True)
            deviation = MRPAnalysis.MRPAnalysis.calculate_std_deviation(reading, _temperature_axis=True) / 2.0
            variance = MRPAnalysis.MRPAnalysis.calculate_variance(reading, _temperature_axis=True)

            clust_data.append(['{}:{}'.format(reading.measurement_config.id, reading.measurement_config.sensor_id),
                               "{:.2f}".format(mean), "{:.2f}".format(deviation), "{:.2f}".format(variance),
                               len(reading.data)])

        ## TEMP HEATMAP PlOT
        ylabels: [str] = []

        max_len_datapoints = 0
        for r in _readings:
            max_len_datapoints = max([max_len_datapoints, len(r.data)])

        heatmap = np.empty((num_readings, max_len_datapoints))
        heatmap[:] = np.nan

        for reading_idx, reading in enumerate(_readings):
            # add reading label
            ylabels.append('{}:{}'.format(reading.measurement_config.id, reading.measurement_config.sensor_id))
            # add datapoints for each reading
            for idx, dp in enumerate(reading.data):
                heatmap[reading_idx, idx] = dp.temperature

        # Plot the heatmap, customize and label the ticks
        fig, (ax1, ax0) = plt.subplots(2,1, figsize=(16, num_readings*2)) # num_readings*2 for height for table and heatmap plot

        ax1.axis('tight')
        ax1.axis('off')
        ax1.set_title('{} - PolarPlot'.format(_title))
        tbl = ax1.table(cellText=clust_data, colLabels=collabel, loc='center')


        # ADD HEATMAP COLORPLOT
        ratio = (num_readings*max_len_datapoints) / max_len_datapoints
        im = ax0.imshow(heatmap, interpolation='nearest', origin = 'upper', extent=[0, max_len_datapoints, 0, num_readings], aspect=ratio)
        ax0.set_yticks(range(num_readings))
        ax0.set_yticklabels(ylabels)
        ax0.set_xlabel('Data-Point Index')
        ax0.set_ylabel('reading [id:sensor_id]')
        ax0.set_title('{} Temperature'.format(_title))
        # ADD COLOR BAR
        cbar = fig.colorbar(mappable=im, orientation='horizontal')
        cbar.set_label('Temperature, $^\circ\mathrm{C}$')

        #plt.show()

        # SAVE FIGURE IF NEEDED
        if _filename is not None:
            plt.savefig(_filename, dpi=1200)
        else:
            plt.show()

        plt.close()





