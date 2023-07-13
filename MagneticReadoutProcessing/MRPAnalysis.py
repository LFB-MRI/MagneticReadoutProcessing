""" Provides functions to merge two reading, apply calibration measurements"""

import numpy
from MagneticReadoutProcessing import MRPReading

class MRPAnalysisException(Exception):
    def __init__(self, message="ReadingAnalysisException thrown"):
        self.message = message
        super().__init__(self.message)



class MRPAnalysis(object):
    # TODO BINNING IMPLEMENTIEREN
    #
    @staticmethod
    def merge_two_90drg_measurements_to_full_sphere(_reading_top: MRPReading, _reading_bottom: MRPReading) -> MRPReading:
        top_n_theta = _reading_top.measurement_config['n_theta']
        top_theta_radians = _reading_top.measurement_config['theta_radians']

        bottom_n_theta = _reading_bottom.measurement_config['n_theta']
        bottom_theta_radians = _reading_bottom.measurement_config['theta_radians']

        # CHECK AXIS LIMITS
        # # TODO CURRENTLY LIMITS NEEDS TO BE EQUALLY... FIX THIS LATER TO ALLOW OTHER n_theta values E.G. MERGE 90DEGREE AND 45 DEGREE READING
        # ONLY CHECK n_phi and radius
        for key in ['n_phi', 'phi_radians', 'sensor_distance_radius']:
            top_value = _reading_top.measurement_config[key]
            bottom_value = _reading_bottom.measurement_config[key]
            if top_value != bottom_value:
                raise MRPAnalysisException("mismatching {0} _reading_top:{1} _reading_bottom:{2}".format(key, top_value, bottom_value))



        # CREATE NEW READING WITH MODIFED SIZE
        ret = MRPReading.MRPReading(None)
        ret.measurement_config = _reading_top.measurement_config
        # NEW VALUES FOR THE VERTICAL AXIS WHICH GOINT FROM + (top scan) to - (bottom scan)
        #ret.measurement_config['n_theta'] = bottom_n_theta
        ret.measurement_config['theta_radians'] = top_theta_radians + bottom_theta_radians

        print("new calculated n_theta:{0} theta_radians:{1}".format(ret.measurement_config['n_theta'], ret.measurement_config['theta_radians']))
        # MERGE DATA
        max_theta = 0.0
        max_reading_index_phi = 0
        max_reading_index_theta = 0
        for entry in _reading_top.data:
            value = entry['value']
            phi = entry['phi']
            # THEATA IS PONTING DOWN
            theta = entry['theta']
            reading_index_phi = entry['reading_index_phi']
            reading_index_theta = entry['reading_index_theta']
            # GET LIMITS FOR INSERTING THE BOTTOM DATA CORRECT ORDER
            max_reading_index_phi = max(max_reading_index_phi, reading_index_phi)
            max_reading_index_theta = max(max_reading_index_theta, reading_index_theta)
#           # INSERT DATA
            ret.insert_reading(value, phi, theta, reading_index_phi, reading_index_theta)

        for entry in _reading_bottom.data:
            value = entry['value']
            phi = entry['phi']
            # THEATA IS PONTING DOWN
            # HERE WE NEED TO ADD A OFFSET TO COVER TO BOTTOM HALF
            theta =   top_theta_radians - entry['theta']
            reading_index_phi = max_reading_index_phi + entry['reading_index_phi']
            reading_index_theta = max_reading_index_theta + entry['reading_index_theta']
            ret.insert_reading(value, phi, theta, reading_index_phi, reading_index_theta)
        return ret


    @staticmethod
    def apply_calibration_data_inplace(_calibration_reading: MRPReading, _current_reading: MRPReading) -> None:
        # GET NUMPY ARRAY
        np_cal = _calibration_reading.to_numpy_polar()
        np_curr = _current_reading.to_numpy_polar()

        # CHECK FOR ARRAY SHAPE
        if not numpy.shape(np_cal) == numpy.shape(np_curr):
            raise MRPAnalysisException("array shape check failed")
        # SUBTRACT CALC FROM CURRENT DATA
        new_array = numpy.subtract(np_curr, np_cal)
        # UPDATE INPLACE
        _current_reading.update_data_from_numpy_polar(new_array)


    def apply_binning(self, _calibrated_readings: list[MRPReading.MRPReading], _reference_reading: MRPReading, _bins:int = None) -> list[MRPReading.MRPReading]:
        if _calibrated_readings is None or len(_calibrated_readings) <= 0:
            raise MRPAnalysisException("_calibrated_readings is none or empty")
        if _reference_reading is None:
            raise MRPAnalysisException("_reference_reading is None")

        if _bins is None:
            _bins = len(_calibrated_readings) + 1
            print("set _bins (bin count) to {0}".format(_bins))

        # CALCULATE ABS DEVIATION FROM BASE READING
        mean_deviations_ref_base = []
        np_ref = _reference_reading.to_numpy_polar()
        for r in _calibrated_readings:
            np_curr = r.to_numpy_polar()
            # TODO SUBTRACT
            deviation_array = numpy.subtract(np_curr, np_ref)
            abs_deviation = numpy.sum(deviation_array)
            mean_deviations_ref_base.append(abs_deviation)

        # SAVE MIN MAX DEVIATION
        mean_deviations_ref_base = numpy.array(mean_deviations_ref_base)
        abs_min_dev = numpy.min(mean_deviations_ref_base)
        abs_max_dev = numpy.max(mean_deviations_ref_base)
        abs_range = abs(abs_min_dev) + abs(abs_max_dev)

        #bin_ranges =

        # CREATE BIN RANGES FROM BINS AND MIN MAX DEVIATION
        # GROUP READINGS IN RETURN AS DICT
        return []


    def __init__(self, _reading: MRPReading):
        pass





    # cube = magpy.magnet.Cuboid(magnetization=(0,0,100), dimension=(1,1,1))
    def calculate_magnetization(self):
        pass


    def create_magpy_magnet(self):
        pass


