"""  stores all reading relevant information values, datapoints, meta-data """

import os.path
from datetime import datetime
import numpy as np
import json
import sys

import scipy

from MRP import MRPHelpers, MRPReadingEntry, MRPMagnetTypes, MRPMeasurementConfig



class MRPReadingException(Exception):
    """
    Custom exception class for handling errors related to MRP (Magnetometer Reading Processing).

    Args:
        message (str, optional): The error message to be displayed when the exception is raised.
                                 Defaults to "MRPReadingException thrown".

    This class extends the built-in `Exception` class to provide a specific exception type for 
    errors encountered during MRP-related operations. The message can be customized or will 
    default to a standard message.
    """

    def __init__(self, message="MRPReadingException thrown"):
        self.message = message  # Set the exception message
        super().__init__(self.message)  # Call the base class constructor


class MRPReading():
    """ Stores the raw sensor data, including metadata and import/export functions"""
    EXPORT_TIME_FORMAT: str = "%a %b %d %H:%M:%S %Y"

    import_scale_factor: float = 1.0


    def __init__(self, _config: MRPMeasurementConfig.MRPMeasurementConfig = None, _magnet_id: int = 0):
        """
        Initializes a new instance of the reading class with default or provided configuration settings.

        Args:
            _config (MRPMeasurementConfig.MRPMeasurementConfig, optional): Configuration object for the measurement.
                                                                        If None, a default configuration is used.
            _magnet_id (int, optional): The ID of the magnet used for the measurement. Defaults to 0.

        This constructor sets up an empty reading object with some predefined metadata, including start and end times,
        an empty list for reading data samples, and user-defined metadata storage. If no configuration is provided, 
        a default full-sphere configuration is applied with a default sensor distance and ID.
        """

        # Start and end times of the reading, initialized to the current time
        self.time_start: datetime = datetime.now()
        self.time_end: datetime = datetime.now()

        # Holds the reading data samples (empty list of MRPReadingEntry objects)
        self.data: [MRPReadingEntry.MRPReadingEntry] = []

        # Stores import measurement information
        self.measurement_config: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()

        # User-defined metadata storage as key-value pairs
        self.additional_data: dict = dict()
        self.set_additional_data('name', 'unknown')  # Default name for the reading

        # Populate some default data for the reading
        self.measurement_config: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()

        # If a configuration is provided, deep copy its values into measurement_config
        if _config is not None:
            self.measurement_config.from_dict(_config.to_dict()) # Deep copy
        else:
            # Use default configuration settings when no config is provided
            self.measurement_config = MRPMeasurementConfig.MRPMeasurementConfig()
            self.measurement_config.configure_fullsphere()  # Set a full-sphere configuration
            self.measurement_config.sensor_distance_radius = 1  # Default sensor distance radius
            self.measurement_config.sensor_id = 0  # Default sensor ID

            # Set the magnet ID, if provided
            if _magnet_id is not None:
                self.measurement_config.id = _magnet_id
            else:
                self.measurement_config.id = 0

        # Set the unit import scale factor (default is 1.0)
        self.set_unit_import_scale_factor()
    


    def set_unit_import_scale_factor(self, _factor: float = 1.0):
        """
        Sets the import scale factor for unit conversions or data imports.

        Args:
            _factor (float, optional): The scale factor to be applied during data import or unit conversion.
                                    Defaults to 1.0.

        This function updates the `import_scale_factor` attribute, which can be used to scale imported data 
        or convert units as needed. By default, the factor is set to 1.0, indicating no scaling.
        """
        # Update the import_scale_factor attribute with the provided scale factor
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


    def has_additional_data_keys(self, _keys: list[str]) -> bool:
        """
        Checks if all the provided keys exist in the `additional_data` dictionary.

        Args:
            _keys (list[str]): A list of keys to be checked in the `additional_data` dictionary.

        Returns:
            bool: 
                - True if all keys in the list exist in `additional_data`.
                - False if any key in the list is missing from `additional_data`.

        This function iterates over a list of keys and checks if each one exists in the 
        `additional_data` dictionary by calling the `has_additional_data` method for each key. 
        If any key is missing, the function returns `False`; otherwise, it returns `True` when all keys are present.
        """
        # Iterate over each key in the provided list of keys
        for k in _keys:
            # If any key is not found in additional_data, return False
            if not self.has_additional_data(k):
                return False
        # If all keys are found, return True
        return True
    

    def has_additional_data(self, _k: str) -> bool:
        """
        Checks if the provided key exists and is valid in the `additional_data` dictionary.

        Args:
            _k (str): The key to be checked in the `additional_data` dictionary.

        Returns:
            bool: 
                - True if the key exists and is non-empty.
                - False if the key is None, empty, or not found in `additional_data`.

        The function first ensures that the input key `_k` is not None and has a length greater than zero. 
        If the key passes this condition, it checks if the key exists in the `additional_data` dictionary.
        """
        if _k is not None and len(_k) > 0:
            # If the key exists in the additional_data dictionary, return its value
            if _k in self.additional_data:
                return True
        return False



    def get_additional_data(self, _k: str) -> any:
        """
        Retrieve additional data associated with the given key from the instance's 
        additional_data dictionary.

        Parameters:
        - _k (str): The key for which to retrieve the associated data. This should 
        be a non-empty string.

        Returns:
        - any: The value associated with the specified key if it exists; otherwise, 
        returns None.
        """
    
        # Check if the provided key is not None and has a length greater than 0
        if _k is not None and len(_k) > 0:
            # If the key exists in the additional_data dictionary, return its value
            if _k in self.additional_data:
                return self.additional_data.get(_k, None)

        # Return None if the key is invalid or does not exist
        return None
    
    def set_additional_data(self, _k: str, _v: any):
        """
        Set a custom user meta-data entry.
        For example if the ``apply_calibration_data_inplace`` is used on a reading, a custom entry `is_calibrated`=1 is added to the reading using this function.

        :param _k: Key
        :type _k: str

        :param _v: Value
        :type _v: str
        """
        if self.additional_data is None:
            self.additional_data = {
                
            }

        if _k is not None and len(_k) > 0:
            self.additional_data[str(_k)] = _v


    def get_name(self) -> str:
        """
        Returns the name of the reading

        :returns: Returns reading name set using set_name(_name_)
        :rtype: str
        """
        if not self.has_additional_data("name"):
            self.set_name('unknown')
        return self.get_additional_data("name")
    

    def set_name(self, _name: str = 'unknown'):
        """
        Sets the name of the reading

        :param _name: name of the reading
        :type _name: str
        """
        self.set_additional_data('name', _name)

    def set_magnet_type(self, _type: MRPMagnetTypes.MagnetType):
        """
        Sets the magnet type in the `measurement_config` configuration.

        Args:
            _type (MRPMagnetTypes.MagnetType): The magnet type to be set.

        This function updates the `magnet_type` attribute in the `measurement_config` object 
        with the provided `_type` value. The `_type` should be a valid `MagnetType` from 
        the `MRPMagnetTypes` class.
        """
        # Update the magnet_type attribute in the measurement_config with the provided type
        self.measurement_config.magnet_type = _type

    def get_magnet_type(self) -> MRPMagnetTypes.MagnetType:
        """
        Retrieves the current magnet type from the `measurement_config` configuration.

        Returns:
            MRPMagnetTypes.MagnetType: The currently set magnet type from the `measurement_config`.

        This function accesses the `measurement_config` object and returns the current 
        magnet type that is stored in the `magnet_type` attribute.
        """
        # Return the current magnet type from the measurement_config
        return self.measurement_config.magnet_type

  
    def to_numpy_cartesian(self, _normalize: bool = True, _use_sensor_distance: bool = False) -> np.array:
        """
        Converts spherical coordinate data to Cartesian coordinates and returns them as a NumPy array.

        Args:
            _normalize (bool, optional): Whether to normalize the data (currently not used in the function). Defaults to True.
            _use_sensor_distance (bool, optional): Whether to use the sensor distance radius for the conversion. Defaults to False.

        Returns:
            np.array: A NumPy array containing the converted Cartesian coordinates.

        This function iterates over the spherical data (`phi`, `theta`, and `value`) in the `data` list. 
        It converts the spherical coordinates to Cartesian using `MRPHelpers.asCartesian()`. 
        If `_use_sensor_distance` is True, it uses the sensor distance radius from the `measurement_config` 
        for the conversion; otherwise, it uses the `value` from the data for the conversion.
        """

        # Get the sensor distance radius from the measurement configuration
        sensor_distance_radius = self.measurement_config.sensor_distance_radius

        # Initialize an empty list to store Cartesian coordinates
        inp = []

        # Iterate over the spherical data in self.data
        for entry in self.data:
            phi = entry.phi    # Azimuthal angle
            theta = entry.theta  # Polar angle
            value = entry.value  # Radial distance

            # Convert to Cartesian coordinates using sensor distance or value
            if _use_sensor_distance:
                cart = MRPHelpers.asCartesian((value, theta, phi))  # Use value from data
            else:
                cart = MRPHelpers.asCartesian((sensor_distance_radius, theta, phi))  # Use fixed sensor distance radius

            # Append the Cartesian coordinates to the list
            inp.append(cart)

        # Return the list of Cartesian coordinates as a NumPy array
        return np.array(inp)


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


    def to_measurement_entry_array(self) -> list[MRPReadingEntry.MRPReadingEntry]:
        """
        Returns all values as 1d array in order of insertion.

        :returns: Returns [value, value]
        :rtype: list[MRPReadingEntry]
        """

        return self.data

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
        """
        Serializes the current object into a dictionary format for data export.

        Returns:
            dict: A dictionary containing the serialized data of the object, including 
                timestamps, additional data, the measurement configuration, and the main dataset.

        This function creates a dictionary containing key pieces of information about the current object:
        - `dump_time`: The time when the dump occurs.
        - `time_start` and `time_end`: The start and end times of the measurement, formatted based on the export time format.
        - `additional_data`: A dictionary containing any additional metadata associated with the object.
        - `data`: The main dataset, with each entry converted to a dictionary.
        - `measurement_config`: Serialized measurement configuration.

        The function also ensures that any extra user data stored in `additional_data` is directly added to the final dictionary. 
        A placeholder comment is added for potential serialization of more complex objects.
        """

        # Create the base dictionary with time and additional metadata
        final_dataset = dict({
            'dump_time': datetime.now().strftime(self.EXPORT_TIME_FORMAT),  # Time of the dump
            'time_start': self.time_start.strftime(self.EXPORT_TIME_FORMAT),  # Measurement start time
            'time_end': self.time_end.strftime(self.EXPORT_TIME_FORMAT),  # Measurement end time
            'additional_data': self.additional_data  # Extra metadata
        })

        # TODO: Implement real object serialization for more complex data structures
        # Initialize an empty list for storing the serialized data entries
        final_dataset['data'] = []

        # Convert each entry in self.data to a dictionary and append to the list
        for entry in self.data:
            final_dataset['data'].append(entry.to_dict())

        # Serialize the measurement configuration to a dictionary
        final_dataset['measurement_config'] = self.measurement_config.to_dict()

        # TODO: Remove redundancy if necessary
        # If additional data exists, add it to the final dataset dictionary
        # This adds user-defined additional data directly to the top-level dictionary
        if self.additional_data is not None:
            for item in self.additional_data.items():
                final_dataset[str(item[0])] = item[1]

        # Return the fully serialized dictionary
        return final_dataset



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

        if not self.has_additional_data("name"):
            self.set_name(os.path.basename(_filepath_name))

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


