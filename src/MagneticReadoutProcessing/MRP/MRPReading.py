"""  stores all reading relevant information values, datapoints, meta-data """

import os.path
from datetime import datetime
import numpy as np
import json
import sys

import scipy

from MRP import MRPHelpers, MRPReadingEntry, MRPMagnetTypes, MRPMeasurementConfig



class MRPReadingException(Exception):
    def __init__(self, message="MRPReadingException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPReading():
    """ Stores the raw sensor data, including metadata and import/export functions"""
    EXPORT_TIME_FORMAT: str = "%a %b %d %H:%M:%S %Y"



    def __init__(self, _config: MRPMeasurementConfig.MRPMeasurementConfig = None, _magnet_id:int = 0):
        """
        The constructor create a new empty reading with some predefined meta-data.

        :param _config:
        :type _config: MRPMeasurementConfig.MRPMeasurementConfig
        """
        self.time_start: datetime = datetime.now()
        self.time_end: datetime = datetime.now()
        # holds the reading data samples
        self.data: [MRPReadingEntry.MRPReadingEntry] = []
        # stores import measurement information like
        self.measurement_config: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()
        # user defined metadata storage as kv pair
        self.additional_data: dict = dict()
        self.additional_data['name'] = 'unknown'
        # POPULATE SOMA DEFAULT DATA ABOUT THE READING
        self.measurement_config: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()



        if _config is not None:
            # using deepcopy without using deepcopy :)
            self.measurement_config.from_dict(_config.to_dict())
        else:
            self.measurement_config = MRPMeasurementConfig.MRPMeasurementConfig()
            self.measurement_config.configure_fullsphere()
            self.measurement_config.sensor_distance_radius = 1
            self.measurement_config.sensor_id = 0

            if _magnet_id is not None:
                self.measurement_config.id = _magnet_id
            else:
                self.measurement_config.id = 0

    import_scale_factor: float = 1.0
    def set_unit_import_scale_factor(self, _factor: float = 1.0):
        self.import_scale_factor = _factor

    def load_from_dict(self, _jsondict: dict):
        self.time_start = None
        if len(_jsondict['time_start']) > 0:
            t = _jsondict['time_start']
            self.time_start = datetime.strptime(t, self.EXPORT_TIME_FORMAT)
        self.time_end = None
        if len(_jsondict['time_end']) > 0:
            self.time_end = datetime.strptime(_jsondict['time_end'], self.EXPORT_TIME_FORMAT)

        # HANDLE DATA IMPORT DIFFERENTLY
        # DUE WE NEED TO CONVERT IT TO MRPReadingEntry
        self.data = []
        for idx, entry in enumerate(_jsondict['data']):
            _re = MRPReadingEntry.MRPReadingEntry()
            _re.from_dict(entry, self.import_scale_factor)
            self.data.append(_re)

        self.measurement_config = MRPMeasurementConfig.MRPMeasurementConfig()
        self.measurement_config.from_dict(_jsondict['measurement_config'])

        # ADD ONLY THE IMPORTANT MEASUREMENT CONFIG ENTRIES
        self.additional_data = _jsondict['additional_data']

    def load_from_file(self, _filepath_name: str):
        """
        Loads a given .mag.json file from a previous dump_to_file().
        It restores all meta-data and datapoints.

        :param _filepath_name: ABS or REL Filepath-string filepath to .mag.pkl
        :type _filepath_name: str
        """
        try:
            fint = open(_filepath_name, 'r')
            pl = json.load(fint)
            self.load_from_dict(pl)
            # CLOSE FILE
            fint.close()
            return pl
        except Exception as e:
            sys.stderr.write(str(e))

    def set_additional_data(self, _k: str, _v: any):
        """
        Set a custom user meta-data entry.
        For example if the ``apply_calibration_data_inplace`` is used on a reading, a custom entry `is_calibrated`=1 is added to the reading using this function.

        :param _k: Key
        :type _k: str

        :param _v: Value
        :type _v: str
        """
        if _k is not None and len(_k) > 0:
            self.additional_data[str(_k)] = _v


    def get_name(self) -> str:
        """
        Returns the name of the reading

        :returns: Returns reading name set using set_name(_name_)
        :rtype: str
        """
        if 'name' not in self.additional_data:
            self.set_name('unknown')
        return self.additional_data['name']
    def set_name(self, _name: str = 'unknown'):
        """
        Sets the name of the reading

        :param _name: name of the reading
        :type _name: str
        """
        self.additional_data['name'] = _name

    def set_magnet_type(self, _type: MRPMagnetTypes.MagnetType):
        self.measurement_config.magnet_type = _type

    def get_magnet_type(self) -> MRPMagnetTypes.MagnetType:
        return self.measurement_config.magnet_type

    def savemat(self):
        import scipy.io
        scipy.io.savemat('test.mat', dict(x=x, y=y))

    def to_numpy_cartesian(self, _normalize: bool = True, _use_sensor_distance: bool = False) -> np.array:

        # X Y Z GRID
        sensor_distance_radius = self.measurement_config.sensor_distance_radius

        inp = []
        # TO ENSURE
        for entry in self.data:

            phi = entry.phi
            theta = entry.theta
            value = entry.value

            if _use_sensor_distance:
                cart = MRPHelpers.asCartesian((value, theta, phi))
            else:
                cart = MRPHelpers.asCartesian((sensor_distance_radius, theta, phi))

            inp.append(cart)

        return inp

    def to_value_array(self) -> np.ndarray:
        """
        Returns all values as 1d array in order of insertion.

        :returns: Returns [value, value]
        :rtype: np.ndarray
        """
        ret = []
        for entry in self.data:
            ret.append(entry.value)
        return np.array(ret)

    def len(self) -> int:
        return len(self.data)
    def to_temperature_value_array(self) -> np.ndarray:
        """
        Returns all temperature values as 1d array in order of insertion.

        :returns: Returns [value, value]
        :rtype: np.ndarray
        """
        ret: [float] = []
        for entry in self.data:
            ret.append(entry.temperature * 1.0)
        return np.array(ret)


    def to_numpy_matrix(self) -> np.ndarray:
        """
        Generates a matrix representation of the reading.
        Here eah datapoint will be
        Note: only the value entry is included
        RETURN FORMAT: [[phi, theta, value],...]

        :returns: Returns the matrix with shape ()
        :rtype: np.ndarray
        """

        # CHECK FOR CONTINUOUS NUMBERING
        n_phi = self.measurement_config.n_phi
        n_theta = self.measurement_config.n_theta

        if not len(self.data) == (n_phi * n_theta):
            raise MRPReadingException("data length count invalid")

        values_present_phi = {}
        values_present_theta = {}

        for entry in self.data:
            values_present_phi[str(entry.reading_index_phi)] = 1
            values_present_theta[str(entry.reading_index_theta)] = 1

        for i in range(n_phi):
            if str(i) not in values_present_phi:
                raise MRPReadingException("CHECK FOR CONTINUOUS NUMBERING FAILED FOR PHI")

        for i in range(n_theta):
            if str(i) not in values_present_theta:
                raise MRPReadingException("CHECK FOR CONTINUOUS NUMBERING FAILED FOR THETA")

        # CREATE MATRIX
        result_matrix = np.zeros((n_theta, n_phi))
        # https://towardsdatascience.com/spherical-projection-for-point-clouds-56a2fc258e6c
        # https://www.quora.com/Can-we-project-a-sphere-in-a-2-dimensional-surface

        # CONVERT TO XYZ + value
        # XYZ TO UV + value
        # MAP UV TO MATRIX = value

        polar = self.to_numpy_polar(_normalize=False)
        min_value = np.min(polar)
        max_value = np.max(polar)
        polar_normalized = self.to_numpy_polar(_normalize=True)

        # for entry in self.data:
        #    p = entry['reading_index_phi']
        #    t = entry['reading_index_theta']
        #    v = entry['value']
        #    result_matrix.itemset((t, p), v)
        return result_matrix

    # TODO MERGE WITH VISUALISATION ROUTINES AND ALLOW NORMALISATION FLAG
    def to_numpy_polar(self, _normalize: bool = False) -> np.ndarray:
        """
        Generates a 2D numpy array from the stored datapoints.
        Note: only the value entry is included
        RETURN FORMAT: [[phi, theta, value],...]

        :param _normalize: Optional; If True the currently stored values will be normalized from -1.0 to 1.0
        :type _normalize: bool

        :returns: Returns currently saved data as numpy polar array [[phi, theta, value],...]
        :rtype: (np.ndarray, float, float)
        """
        # NORMALIZE DATA
        min_val = float('inf')
        max_val = -float('inf')
        # GET MIN MAX VALUE
        if _normalize:
            for r in self.data:
                value = r.value
                if value < min_val:
                    min_val = value - 0.1
                if value > max_val:
                    max_val = value + 0.1

        arr_1d_data = []  # 1D ARRAY WILL BE RESHAPED LATER ON

        # CONVERT AND NORMALIZE DATA
        for r in self.data:
            phi = r.phi
            theta = r.theta
            value = r.value
            # NORMALIZE IF NEEDED
            if _normalize:
                normalized_value = MRPHelpers.translate(value, min_val, max_val, -1.0, 1.0)
                arr_1d_data.append([phi, theta, normalized_value])
            else:
                arr_1d_data.append([phi, theta, value])

        # PERFORM RESHAPE AND NUMPY CONVERSION
        arr_1d_data_np = np.array(arr_1d_data)
        return arr_1d_data_np

    def update_data_from_numpy_polar(self, _numpy_array: np.ndarray):
        """
        _numpy_array is a (x, 3) shaped array with [[phi, theta, value],...] structured data
        each matching phi, theta combination in the reading.data structure will be updated with the corresponding value from the _numpy_array entry

        :param _numpy_array: datapoints to update: [[phi, theta, value],...]
        :type _numpy_array: np.ndarray
        """

        # CHECK FOR ARRAY/DATA SHAPE
        # given 1d array [phi, theta, value]
        if np.shape(_numpy_array)[1] != 3:
            raise MRPReadingException("array shape check failed")
        # if not np.shape(_numpy_array) == numpy.shape(np_curr):
        #    raise MRPAnalysisException("array shape check failed")

        # SKIP IF UPDATE DATA ARE ENTRY
        if len(_numpy_array) <= 0:
            return

        for update in _numpy_array:
            update_phi = update[0]
            update_theta = update[1]
            update_value = update[2]

            for idx, data_entry in enumerate(self.data):
                phi = data_entry.phi
                theta = data_entry.theta
                if phi == update_phi and theta == update_theta:
                    self.data[idx].value = update_value
                    break
        # TODO OPTIMIZE

        # ITERATE OVER UPDATE DATA ENTRIES AND FIND IN DATA DICT
        # SO IMPORT/EXPORT IS POSSIBLE


    def insert_reading_instance(self, _measurement: MRPReadingEntry.MRPReadingEntry, _autoupdate_measurement_config:bool = True):
        """
        Inserts a new reading into the dataset using an instance of MRPReadingEntry

        :param _measurement: reading measurement
        :type _measurement: MRPReadingEntry.MRPReadingEntry

        :param _autoupdate_measurement_config:
        :type _autoupdate_measurement_config: bool
        """
        if _measurement is None:
            raise MRPReadingException()

        self.data.append(_measurement)

        if _autoupdate_measurement_config:
            self.measurement_config.phi_radians = max(self.measurement_config.phi_radians, _measurement.phi)
            self.measurement_config.theta_radians = max(self.measurement_config.theta_radians, _measurement.theta)
            self.measurement_config.n_phi = max(self.measurement_config.n_phi, _measurement.reading_index_phi)
            self.measurement_config.n_theta = max(self.measurement_config.n_theta, _measurement.reading_index_theta)

    def insert_reading(self, _read_value: float, _phi: float, _theta: float, _reading_index_phi: int,
                       _reading_index_theta: int, _is_valid: bool = True, _autoupdate_measurement_config: bool = True):
        """
        Inserts a new reading into the dataset.
        The _phi, _theta values need to be valid polar coordinates

        :param _read_value: hallsensor reading in [mT]
        :type _read_value: float

        :param _phi: polar coordinates of the datapoint: phi
        :type _phi: float

        :param _theta: polar coordinates of the datapoint: theta
        :type _theta: float

        :param _reading_index_phi: index of the phi coordinate count = resolution for phi axis
        :type _reading_index_phi: int

        :param _reading_index_theta: index of the theta coordinate count = resolution for theta axis
        :type _reading_index_theta: int

        :param _autoupdate_measurement_config:
        :type _autoupdate_measurement_config: bool

        """
        if len(self.data) <= 0:
            self.time_start = datetime.now()
        self.time_end = datetime.now()
        entry = MRPReadingEntry.MRPReadingEntry(len(self.data), _read_value, _phi, _theta, _reading_index_phi,
                                                _reading_index_theta, _is_valid)

        self.insert_reading_instance(entry, _autoupdate_measurement_config)


    def dump_to_dict(self) -> dict:
        final_dataset = dict({
            'dump_time': datetime.now().strftime(self.EXPORT_TIME_FORMAT),
            'time_start': self.time_start.strftime(self.EXPORT_TIME_FORMAT),
            'time_end': self.time_end.strftime(self.EXPORT_TIME_FORMAT),
            'additional_data': self.additional_data
        })

        # TODO REAL OBJECT SERIALIZATION
        final_dataset['data'] = []
        for entry in self.data:
            final_dataset['data'].append(entry.to_dict())

        final_dataset['measurement_config'] = self.measurement_config.to_dict()
        # TODO REMOVE REDUNDANCY ?
        # ADD ADDITIONAL USERDATA
        if self.additional_data is not None:
            for item in self.additional_data.items():
                final_dataset[str(item[0])] = item[1]
        return  final_dataset

    def dump(self) -> str:
        # DUMP TO BYTES
        return json.dumps(self.dump_to_dict())

    def dump_to_file(self, _filepath_name: str) -> str:
        """
        Dumps the reading class instance into a binary file.
        Including datapoints, config, measurement_config and additional_data as metadata

        :param _filepath_name: File path to which the file will be exported
        :type _filepath_name: str

        :returns: File path to which the file is exported, including filename
        :rtype: str
        """
        if '.mag.json' not in _filepath_name:
            _filepath_name = _filepath_name + '.mag.json'
        print("dump_to_file with {0}".format(_filepath_name))

        # STORE SOME EXPORT METADATA
        self.set_additional_data('export_filepath', _filepath_name)
        self.set_additional_data('export_filename', os.path.basename(_filepath_name))

        if self.additional_data['name'] != 'unknown':
            self.set_additional_data('name', os.path.basename(_filepath_name))

        # FINALLY EXPORT TO FILE USING THE self.dump option
        try:
            fout = open(_filepath_name, 'w')
            fout.write(self.dump())
            fout.close()
        except Exception as e:
            sys.stderr.write(str(e))
        return _filepath_name


    def dump_savemat(self, _filepath_name: str) -> str:
        """
        Dumps the reading class instance into a matlab .mat file
        Includes datapoints only

        :param _filepath_name: File path to which the file will be exported
        :type _filepath_name: str

        :returns: File path to which the file is exported, including filename
        :rtype: str
        """
        if '.mat' not in _filepath_name:
            _filepath_name = _filepath_name + '.mat'
        print("dump_to_file with {0}".format(_filepath_name))


        # FINALLY EXPORT TO FILE USING SCIPY AS EXPORT MIDDLEWARE
        try:
            scipy.io.savemat(_filepath_name, dict(x=self.to_value_array(), y=self.to_temperature_value_array()))
        except Exception as e:
            sys.stderr.write(str(e))
        return _filepath_name


