"""This class only includes static methods which are able to used in a user defined pipeline"""

import os
import re
from pathlib import Path

import numpy as np
import scipy.optimize as opt

from MRP import MRPReading, MRPHallbachArrayGenerator, MRPPolarVisualization, MRPReadingEntry
from MRP import MRPSimulation
from MRP import MRPAnalysis
from MRP import MRPDataVisualization
from MRPudpp import UDPPLogger, udpp_config


class UDPPFunctionCollectionException(Exception):
    def __init__(self, message="UDPFFunctionCollectionException thrown"):
        self.message = message
        super().__init__(self.message)


class UDPPFunctionCollection:
    """This class only includes static methods which are able to used in a user defined pipeline"""


    @staticmethod
    def apply_sensor_temperature_calibration(_readings_to_calibrate: [MRPReading.MRPReading], _temperature_calibration_readings: [MRPReading.MRPReading]) -> [MRPReading.MRPReading]:
        # REMOVE OFFSET
        zero_offset: float = 0.0
        for reading in _temperature_calibration_readings:
            zero_offset = min([zero_offset, abs(MRPAnalysis.MRPAnalysis.calculate_mean(reading))])
        # EXTRACT TEMPERATURES

        cr_temp: [float] = []
        cr_means: [float] = []
        for r in _temperature_calibration_readings:
            mean_temp: float = MRPAnalysis.MRPAnalysis.calculate_mean(r, _temperature_axis=True)
            cr_temp.append(mean_temp)

        rsorted: [MRPReading.MRPReading] = [v for _, v in sorted(zip(cr_temp, _temperature_calibration_readings))]

        cr_temp: [float] = []
        cr_means: [float] = []
        for r in rsorted:
            mean: float = MRPAnalysis.MRPAnalysis.calculate_mean(r)
            mean_temp: float = MRPAnalysis.MRPAnalysis.calculate_mean(r, _temperature_axis=True)
            cr_means.append(zero_offset - mean)
            cr_temp.append(mean_temp)
            print("reading imported for temp calibration {} m={:.2} c={:.2}".format(r.get_name(), mean_temp, mean))


        # PERFORM LINEAR FUNCTION FITTING
        a: float = 1.0
        b: float = 0.0
        try:
            opt_params, pcov = opt.curve_fit(MRPDataVisualization.MRPDataVisualization.linear_curve_func, cr_temp,cr_means)
            a = opt_params[0]
            b = opt_params[1]


        except Exception as e:
            raise UDPPFunctionCollectionException("cant fit temperature linear funtion")


        return_readings: [MRPReading.MRPReading] = []
        # FINALLY RUN THE CALIBRATION RUN
        for e in _readings_to_calibrate:
            nr: MRPReading.MRPReading = MRPReading.MRPReading()
            nr.load_from_dict(e.dump_to_dict())
            nr.data = []
            for dp in e.data:
                tfp: MRPReadingEntry = dp
                dp_value: float = tfp.value
                dp_temp: float = tfp.temperature
                offset = MRPDataVisualization.MRPDataVisualization.linear_curve_func(dp_temp, a, b)

                print("apply temp offset of {:.2} for m={:.2}".format(offset, dp_temp))
                tfp.value = tfp.value - offset
                nr.data.append(tfp)
            return_readings.append(nr)
        return return_readings


    @staticmethod
    def simulate_magnet(IP_count: int = 1, IP_random_polarisation: bool = False, IP_random_magnetisation: bool = False, IP_name_prefix: str= "simulated_magnet") -> [MRPReading.MRPReading]:
        ret: [MRPReading.MRPReading] = []

        for idx in range(IP_count):
            rnd = MRPSimulation.MRPSimulation.generate_reading(_randomize_magnetization=IP_random_polarisation, _add_random_polarisation=IP_random_magnetisation)
            rnd.set_additional_data("simulate_magnet", idx)

            rnd.set_name("{}_{}".format(IP_name_prefix, idx))
            ret.append(rnd)

        return ret

    @staticmethod
    def readings_passthrough(readings: [MRPReading.MRPReading]) -> [MRPReading.MRPReading]:
        """
        returns the input readings without any modification.
        implemented and used during development

        :param readings: input readings
        :type readings: [MRPReading.MRPReading]

        :returns: returns same readings as given in the readings input parameter
        :rtype: [MRPReading.MRPReading]
        """
        if readings is None or len(readings) <= 0:
            raise UDPPFunctionCollectionException("readings_passthrough: readings parameter empty")

        return readings

    @staticmethod
    def export_readings(readings_to_export: [MRPReading.MRPReading], IP_export_folder: str = ""):
        """
        exports a (modified) reading back to a .ag.json file

        :param readings_to_export: readings to plot
        :type readings_to_export: [MRPReading.MRPReading]

        :param IP_export_folder: if populated export report to folder
        :type IP_export_folder: str
        """
        if readings_to_export is None or len(readings_to_export) <= 0:
            raise UDPPFunctionCollectionException("readings_to_export: readings parameter empty")

        log: UDPPLogger.UDPPLogger = UDPPLogger.UDPPLogger()

        if len(IP_export_folder) > 0:
            if not str(IP_export_folder).startswith('/'):
                IP_export_folder = str(Path(udpp_config.UDPPConfig.get_result_folder()).joinpath(Path(IP_export_folder)).resolve())
            log.run_log("export_readings: IP_export_folder parameter set to {}".format(IP_export_folder))
        else:
            raise UDPPFunctionCollectionException("export_readings: IP_export_folder parameter empty")

        r: MRPReading.MRPReading
        for r in readings_to_export:
            reading_name: str = r.get_name()
            reading_name = reading_name.strip("/.")
            reading_name = "{}_{}".format(reading_name, r.measurement_config.id)
            reading_abs_filepath: str = str(Path(IP_export_folder).joinpath(Path(reading_name)))
            log.run_log("inspect_readings: report exported to {}".format(reading_abs_filepath))
            # CREATE FOLDER
            if not os.path.exists(IP_export_folder):
                os.makedirs(IP_export_folder)
            # EXPORT
            r.dump_to_file(reading_abs_filepath)

    @staticmethod
    def inspect_readings(readings_to_inspect: [MRPReading.MRPReading], IP_export_folder: str = "", IP_log_to_std: bool = True):
        """
        prints some information about a set of readings

        :param readings: readings to inspect
        :type readings: [MRPReading.MRPReading]

        :param IP_export_folder: if populated export report to folder
        :type IP_export_folder: str
        """
        if readings_to_inspect is None or len(readings_to_inspect) <= 0:
            raise UDPPFunctionCollectionException("inspect_readings: readings parameter empty")

        log: UDPPLogger.UDPPLogger = UDPPLogger.UDPPLogger()

        if len(IP_export_folder) > 0:
            if not str(IP_export_folder).startswith('/'):
                IP_export_folder = str(Path(udpp_config.UDPPConfig.get_result_folder()).joinpath(Path(IP_export_folder)).resolve())

            log.run_log("inspect_readings: IP_export_folder parameter set to {}".format(IP_export_folder))

        for r in readings_to_inspect:
            # REPORT TEMPLATE
            report_text: str = """########## READING REPORT ##########
            NAME: %%NAME%%
            No Datapoints: %%NODP%%
            B [uT]: %%BV%%
            Temperature [°C]: %%TEMP%%
            CenterOfGravity [x y z] normalized: %%COG%%
            ######## END READING REPORT ########"""
            # REPLACE TEMPLATE WITH REPORT DATA
            report_text = report_text.replace("%%NAME%%", "{}".format(r.get_name()))
            report_text = report_text.replace("%%NODP%%", "{}".format(len(r.data)))



            report_text = report_text.replace("%%BV%%", "{}".format(MRPAnalysis.MRPAnalysis.calculate_mean(r, _temperature_axis=False)))
            report_text = report_text.replace("%%TEMP%%", "{}".format(MRPAnalysis.MRPAnalysis.calculate_mean(r, _temperature_axis=True)))


            cog = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(r)
            report_text = report_text.replace("%%COG%%", "[{} {} {}]".format(cog[0], cog[1], cog[2]))

            if IP_log_to_std:
                print(report_text)




            # EXPORT TO FILE
            if len(IP_export_folder) > 0:
                reading_name: str = r.get_name()
                reading_name = reading_name.strip("/.") + ".report.txt"
                reading_abs_filepath: str = str(Path(IP_export_folder).joinpath(Path(reading_name)))
                log.run_log("inspect_readings: report exported to {}".format(reading_abs_filepath))
                # CREATE FOLDER
                if not os.path.exists(IP_export_folder):
                    os.makedirs(IP_export_folder, exist_ok=True)
                # WRITE REPORT TEXT TO FILE
                with open(reading_abs_filepath, 'w') as f:
                    f.write(report_text)

    @staticmethod
    def plot_fullsphere(readings_to_plot: [MRPReading.MRPReading], IP_plot_headline_prefix: str = "Plot", IP_export_folder: str = ""):
        """
        plots a full-sphere in 3d plot of a given reading if possible

        :param readings_to_plot: readings to plot
        :type readings_to_plot: [MRPReading.MRPReading]

        :param IP_export_folder: if populated export report to folder
        :type IP_export_folder: str
        """
        if readings_to_plot is None or len(readings_to_plot) <= 0:
            raise UDPPFunctionCollectionException("readings_to_plot: readings parameter empty")

        log: UDPPLogger.UDPPLogger = UDPPLogger.UDPPLogger()

        exp_path = None
        if len(IP_export_folder) > 0:
            if not str(IP_export_folder).startswith('/'):
                IP_export_folder = str(Path(udpp_config.UDPPConfig.get_result_folder()).joinpath(Path(IP_export_folder)).resolve())

                exp_path = IP_export_folder
            else:
                exp_path = IP_export_folder


            if not os.path.exists(exp_path):
                os.makedirs(exp_path, exist_ok=True)

        elif len(IP_export_folder) < 0:
            exp_path = "./"

        log.run_log("readings_to_plot: IP_export_folder parameter set to {}".format(IP_export_folder))


        r: MRPReading.MRPReading
        for r in readings_to_plot:
            filename: str = str(Path(exp_path).joinpath("plot3d_{}.png".format(str(r.get_name()).strip(" /."))))
            visu: MRPPolarVisualization.MRPPolarVisualization = MRPPolarVisualization.MRPPolarVisualization(r)
            visu.set_title("")
            visu.plot3d(filename)

    @staticmethod
    def plot_readings(readings_to_plot: [MRPReading.MRPReading], IP_plot_headline_prefix: str = "Plot", IP_export_folder: str = ""):
        """
        plots some information about a set of readings including mean, std_deviation and more

        :param readings_to_plot: readings to plot
        :type readings_to_plot: [MRPReading.MRPReading]

        :param IP_export_folder: if populated export report to folder
        :type IP_export_folder: str
        """
        if readings_to_plot is None or len(readings_to_plot) <= 0:
            raise UDPPFunctionCollectionException("readings_to_plot: readings parameter empty")

        log: UDPPLogger.UDPPLogger = UDPPLogger.UDPPLogger()

        exp_path = None
        if len(IP_export_folder) > 0:
            if not str(IP_export_folder).startswith('/'):
                IP_export_folder = str(Path(udpp_config.UDPPConfig.get_result_folder()).joinpath(Path(IP_export_folder)).resolve())


                exp_path = IP_export_folder


                # GET LOGGER
            else:
                exp_path = IP_export_folder

            if not os.path.exists(exp_path):
                os.makedirs(exp_path, exist_ok=True)

        elif len(IP_export_folder) < 0:
            exp_path = "./"



        log.run_log("readings_to_plot: IP_export_folder parameter set to {}".format(IP_export_folder))

        MRPDataVisualization.MRPDataVisualization.plot_error(readings_to_plot, IP_plot_headline_prefix , str(Path(exp_path).joinpath("error_plot_{}.png".format(str(IP_plot_headline_prefix).strip(" /.")))))
        MRPDataVisualization.MRPDataVisualization.plot_scatter(readings_to_plot, IP_plot_headline_prefix,str(Path(exp_path).joinpath("scatter_plot_{}.png".format(str(IP_plot_headline_prefix).strip(" /.")))))
        MRPDataVisualization.MRPDataVisualization.plot_temperature(readings_to_plot, IP_plot_headline_prefix,str(Path(exp_path).joinpath("temperature_plot_{}.png".format(str(IP_plot_headline_prefix).strip(" /.")))))

    @staticmethod
    def concat_readings(set_a: [MRPReading.MRPReading], set_b: [MRPReading.MRPReading], IP_random_shuffle: bool = False) -> [MRPReading.MRPReading]:
        """
        Concat two readings array into one.
        Can be used for combining readings from two folders using the import_readings function

        :param set_a: first array of readings
        :type set_a: [MRPReading.MRPReading]

        :param set_b: second array of readings
        :type set_b: [MRPReading.MRPReading]

        :returns: both readings arrays combined
        :rtype: [MRPReading.MRPReading]
        """

        rd: [MRPReading.MRPReading] = []

        for a in set_a:
            rd.append(a)

        for b in set_b:
            rd.append(b)

        return rd

    @staticmethod
    def import_readings(IP_input_folder:str = "./", IP_file_regex: str = "(.)*.mag.json", IP_parse_idx_in_filename: bool = True) -> [MRPReading.MRPReading]:
        """
        Imports all readings found in the folder given from the input_folder.
        It restores all meta-data and datapoints.

        :param IP_input_folder: Folder with .mag.json readings ABS or REL-Paths are allowed
        :type IP_input_folder: str

        :param IP_file_regex: to only allow certain filenames using a regex string
        :type IP_file_regex: str

        :param IP_parse_idx_in_filename: parses string cIDX<YXZ> in filename and set <XYZ> as measurement id, this is used if manual set id from filename should be used
        :type IP_parse_idx_in_filename: bool

        :returns: Returns the imported readings as [MRPReading.MRPReading] instances
        :rtype: [MRPReading.MRPReading]
        """

        if IP_input_folder is None or len(IP_input_folder) <= 0:
            raise UDPPFunctionCollectionException("import_readings: input_folder parameter empty")
        # CHECK FOLDER EXISTS
        input_folder: str = IP_input_folder

        if not str(IP_input_folder).startswith('/'):
            input_folder = str(Path(udpp_config.UDPPConfig.get_readings_folder()).joinpath(Path(IP_input_folder)).resolve())

        # GET LOGGER
        log: UDPPLogger.UDPPLogger = UDPPLogger.UDPPLogger()
        log.run_log("import_readings: input_folder parameter set to {}".format(input_folder))

        # CHECK FOLDER EXISTS
        if not os.path.exists(input_folder):
            raise UDPPFunctionCollectionException("import_readings: input_folder parameter does not exist on the system".format(input_folder))



        # IMPORT READINGS
        readings_to_import: [str] = [f for f in os.listdir(input_folder) if re.match(r'{}'.format(IP_file_regex), f)]
        imported_results: [MRPReading.MRPReading] = []
        for rti in readings_to_import:
            log.run_log("import_readings: import reading {}".format(rti))
            reading: MRPReading.MRPReading = MRPReading.MRPReading()

            reading_abs_filepath: str = str(Path(input_folder).joinpath(Path(rti)))
            reading.load_from_file(reading_abs_filepath)


            if IP_parse_idx_in_filename:
                f: [str] = rti.split("cIDX")
                cIDX: str = ""
                if len(f) > 1:
                    for c in f[1]:
                        if c.isdigit():
                            cIDX = cIDX + str(c)

                if len(cIDX) > 0:
                    reading.measurement_config.id = cIDX
                    reading.set_additional_data("cIDX", cIDX)
                    reading.set_additional_data("IP_parse_idx_in_filename", "1")
                    reading.set_name("{}_cIDX{}".format(reading.get_name(), cIDX))

            imported_results.append(reading)

        return imported_results

    @staticmethod
    def get_best(binning_readings: [MRPReading.MRPReading], IP_bins: int = 0) -> [MRPReading.MRPReading]:
        if binning_readings is None or len(binning_readings) <= 0:
            raise UDPPFunctionCollectionException("apply_binning: binning_readings parameter empty")


        if IP_bins is None or IP_bins <= 0:
            IP_bins = len(binning_readings) / 2
            print("IP_bins is none or 0 so set it to len(binning_readings) / 2  = {}".format(IP_bins))

        # TODO REQWORK
        res: [MRPReading.MRPReading] = []
        v: [float] = []
        lut: dict = {}
        for idx, r in enumerate(binning_readings):
            m: float = MRPAnalysis.MRPAnalysis.calculate_mean(r)
            v.append(m)
            lut[m] = idx

        v.sort()

        for idx in range(IP_bins):
            res.append(binning_readings[lut[v[idx]]])
        return res

    @staticmethod
    def generate_hallbach_slice(readings_for_slice: [MRPReading.MRPReading], IP_2D_projection: bool = True, IP_output_folder:str = "./", IP_output_filename: str = "array.scad"):
        log: UDPPLogger.UDPPLogger = UDPPLogger.UDPPLogger()


        if readings_for_slice is None or len(readings_for_slice) <= 0:
            raise UDPPFunctionCollectionException("generate_hallbach_slice: readings_for_slice parameter empty")

        exp_path = "./"
        if len(IP_output_folder) > 0:
            if not str(IP_output_folder).startswith('/'):
                IP_output_folder = str(Path(udpp_config.UDPPConfig.get_result_folder()).joinpath(Path(IP_output_folder)).resolve())

                exp_path = IP_output_folder
            else:
                exp_path = IP_output_folder

            if not os.path.exists(exp_path):
                os.makedirs(exp_path, exist_ok=True)

        elif len(IP_output_folder) < 0:
            exp_path = "./"


        log.run_log("generate_hallbach_slice: IP_export_folder parameter set to {}".format(exp_path))

        res83d = MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_1k_hallbach_using_polarisation_direction(readings_for_slice)
        MRPHallbachArrayGenerator.MRPHallbachArrayGenerator.generate_openscad_model([res83d], str(Path(exp_path).joinpath(Path(IP_output_filename))), _2d_object_code=IP_2D_projection, _add_annotations=True)

    @staticmethod
    def apply_sensor_bias_offset(bias_readings: [MRPReading.MRPReading], readings_to_calibrate: [MRPReading.MRPReading]) -> [MRPReading.MRPReading]:
        if bias_readings is None or len(bias_readings) <= 0:
            raise UDPPFunctionCollectionException("apply_sensor_bias_offset: bias_readings parameter empty")

        if readings_to_calibrate is None or len(readings_to_calibrate) <= 0:
            raise UDPPFunctionCollectionException("apply_sensor_bias_offset: readings_to_calibrate parameter empty")

        # CALCULATE AVERAGE OF GIVEN BIAS READINGS
        mean_value: float = MRPAnalysis.MRPAnalysis.calculate_mean(bias_readings[0])
        if len(bias_readings) > 1:
            for br in bias_readings:
                v = MRPAnalysis.MRPAnalysis.calculate_mean(br)
                mean_value = mean_value + v
            mean_value = mean_value / len(bias_readings)
        print("apply_sensor_bias_offset calculated sensor bias {}".format(mean_value))

        # DEEP COPY READINGS
        new_readings: [MRPReading.MRPReading] = []

        # APPLY BIAS OFFSET
        for r in readings_to_calibrate:
            nr: MRPReading.MRPReading = MRPReading.MRPReading()
            nr.load_from_dict(r.dump_to_dict())
            nr.data = []
            for dp in r.data:
                new_dp: MRPReadingEntry.MRPReadingEntry = dp
                new_dp.value = new_dp.value - mean_value
                nr.data.append(new_dp)

            new_readings.append(nr)


        for idx, r in enumerate(readings_to_calibrate):
            mean_value: float = MRPAnalysis.MRPAnalysis.calculate_mean(r)
            print("offset calibrated mean value for {} is {}".format(r.get_name(), mean_value))

        return new_readings

    @staticmethod
    def custom_find_similar_values_algorithm(_readings: [MRPReading.MRPReading], IP_return_count: int = -1) -> [MRPReading.MRPReading]:
        import heapq
        heap = []
        # SET RESULT VALUE COUNT
        IP_return_count = int(IP_return_count)
        if IP_return_count < 0:
            IP_return_count = min([int(len(_readings) / 5)], 1)
        # CALCULATE TARGET VALUE: MEAN FROM ALL VALUES
        target_value: float = 0.0
        for idx, r in enumerate(_readings):
            mean: float = MRPAnalysis.MRPAnalysis.calculate_mean(r)
            target_value = target_value + mean
        target_value = (target_value / len(_readings))
        # PUSH READINGS TO HEAP
        for reading in _readings:
            reading_mean: float = MRPAnalysis.MRPAnalysis.calculate_mean(reading)
            # USE DIFF AS PRIORITY VALUE IN MIN-HEAP
            diff: float = abs(reading_mean - target_value)
            heapq.heappush(heap, (diff, reading))
        # RETURN X BEST ITEMS FROM HEAP
        similar_values: [MRPReading.MRPReading] = [item[1] for item in heapq.nsmallest(IP_return_count, heap)]
        # CLEAN UP USED LIBRARIES AND RETURN RESULT
        del heapq
        return similar_values

