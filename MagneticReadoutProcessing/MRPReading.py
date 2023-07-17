""" Stores the raw sensor data, including metadata and import/export functions"""

import os.path
import pickle
from datetime import datetime
import numpy as np
from MagneticReadoutProcessing import MRPConfig
import pickle
import sys
import math
from MagneticReadoutProcessing import MRPHelpers

class MRPReadingException(Exception):
    def __init__(self, message="MRPReadingException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPReading(object): # object is needed for pickle export



    def __init__(self, _config: MRPConfig = None, _sensor_id: int = 0, _sensor_radius: int = 10) -> None:
        #: Doc comment for instance attribute qux.
        self.time_start = None
        self.time_end = None
        self.data = []
        self.measurement_config = dict()
        self.sensor_id = 0
        # ADD ONLY THE IMPORTANT MEASUREMENT CONFIG ENTRIES
        self.config = dict()
        self.additional_data = dict()
        self.additional_data['name'] = 'unknown'
        # POPULATE SOMA DEFAULT DATA ABOUT THE READING
        self.measurement_config = dict()
        self.measurement_config['sensor_distance_radius'] = 1.0
        self.measurement_config['sensor_id'] = 0

        if _config is not None:
            self.config = _config.get_as_dict()
            self.measurement_config.update({
                'n_phi': self.config['MEASUREMENT']['HORIZONTAL_RESOLUTION'],
                'n_theta': self.config['MEASUREMENT']['VERTICAL_RESOLUTION'],
                'phi_radians': math.radians(self.config['MEASUREMENT']['HORIZONTAL_AXIS_DEGREE']),
                'theta_radians': math.radians(self.config['MEASUREMENT']['VERTICAL_AXIS_DEGREE']),
                'sensor_distance_radius': self.config['MEASUREMENT']['SENSOR_MAGNET_DISTANCE']
            })

        # THE SENSOR RADIUS CAN DIFFER
        if _sensor_radius is not None:
            self.measurement_config['sensor_distance_radius'] = _sensor_radius
        #else:
        #    self.measurement_config['sensor_distance_radius'] = 10

        if _sensor_id is not None:
            self.measurement_config['sensor_id'] = _sensor_id
        else:
            self.measurement_config['sensor_id'] = 0



    def loads(self, _pickle_binaray: bytes):
        pl = pickle.loads(_pickle_binaray)

        self.time_start = pl['time_start']
        self.time_end = pl['time_end']
        self.data = pl['data']
        self.measurement_config = pl['measurement_config']
        # ADD ONLY THE IMPORTANT MEASUREMENT CONFIG ENTRIES
        self.config = pl['config']
        self.additional_data = pl['additional_data']
        self.measurement_config = pl['measurement_config']


    def load_from_file(self, _filepath_name: str):
        try:
            fint = open(_filepath_name, 'rb')
            pl = pickle.load(fint)

            self.time_start = pl['time_start']
            self.time_end = pl['time_end']
            self.data = pl['data']
            self.measurement_config = pl['measurement_config']
            # ADD ONLY THE IMPORTANT MEASUREMENT CONFIG ENTRIES
            self.config = pl['config']
            self.additional_data = pl['additional_data']
            self.measurement_config = pl['measurement_config']

            # CLOSE FILE
            fint.close()
            return pl
        except Exception as e:
            sys.stderr.write(str(e))

    def set_additional_data(self, _k: str, _v: any):
        if _k is not None and len(_k) > 0:
            self.additional_data[str(_k)] = _v

    def set_name(self, _name: str = "unknown"):
        self.additional_data['name'] = _name



    def to_numpy_cartesian(self, _normalize: bool = True, _use_sensor_distance: bool = False) -> np.array:
        # X Y Z GRID
        sensor_distance_radius = self.measurement_config['sensor_distance_radius']
        polar = self.to_numpy_polar(_normalize)

        inp = []

        for entry in polar:

            phi = entry[0]
            theta = entry[1]
            value = entry[2]

            if _use_sensor_distance:
                cart =  MRPHelpers.asCartesian((value, theta, phi))
            else:
                cart = MRPHelpers.asCartesian((sensor_distance_radius, theta, phi))

            inp.append(cart)
        #return np.hypot(x, y), np.degrees(np.arctan2(y, x))

        return inp

    # TODO MERGE WITH VISUALISATION ROUTINES AND ALLOW NORMALISATION FLAG
    def to_numpy_polar(self, _normalize: bool = False) -> np.array:
        # NORMALIZE DATA
        min_val = float('inf')
        max_val = -float('inf')
        # GET MIN MAX VALUE
        if _normalize:
            for r in self.data:
                value = r['value']
                if value < min_val:
                    min_val = value - 0.1
                if value > max_val:
                    max_val = value + 0.1

        arr_1d_data = []  # 1D ARRAY WILL BE RESHAPED LATER ON

        # CONVERT AND NORMALIZE DATA
        for r in self.data:
            phi = r['phi']
            theta = r['theta']
            value = r['value']
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
        :param _numpy_array:
        :return: None
        """

        # CHECK FOR ARRAY/DATA SHAPE
        # given 1d array [phi, theta, value]
        if np.shape(_numpy_array)[1] != 3:
            raise MRPReadingException("array shape check failed")
        #if not np.shape(_numpy_array) == numpy.shape(np_curr):
        #    raise MRPAnalysisException("array shape check failed")

        # SKIP IF UPDATE DATA ARE ENTRY
        if len(_numpy_array) <= 0:
            return


        for update in _numpy_array:
            update_phi = update[0]
            update_theta = update[1]
            update_value = update[2]

            for idx, data_entry in enumerate(self.data):
                phi = data_entry['phi']
                theta = data_entry['theta']
                if phi == update_phi and theta == update_theta:
                    self.data[idx]['value'] = update_value
                    break
        # TODO OPTIMIZE

        # ITERATE OVER UPDATE DATA ENTRIES AND FIND IN DATA DICT
        # SO IMPORT/EXPORT IS POSSIBLE

    def insert_reading(self, _reading: float, _phi: float, _theta: float, _reading_index_phi: int,
                       _reading_index_theta: int, _temp: float = None, _is_valid: bool = True) -> None:
        if len(self.data) <= 0:
            self.time_start = datetime.now()
        self.time_end = datetime.now()
        entry = dict({
            "value": _reading,
            "phi": _phi,
            "theta": _theta,
            "reading_index_phi": _reading_index_phi,
            "reading_index_theta": _reading_index_theta,
            "temperature": _temp,
            "is_valid": _is_valid
        })
        self.data.append(entry)

    def dump(self) -> bytes:
        final_dataset = dict({
            'dump_time': datetime.now(),
            'time_start': self.time_start,
            'time_end': self.time_end,
            'config': self.config,
            'data': self.data,
            'measurement_config': self.measurement_config,
            'additional_data': self.additional_data
        })
        # TODO REMOVE REDUNDANCY ?
        # ADD ADDITIONAL USERDATA
        if self.additional_data is not None:
            for item in self.additional_data.items():
                final_dataset[str(item[0])] = item[1]
        # DUMP TO PICKLE BYTES
        return pickle.dumps(final_dataset)

    def dump_to_file(self, _filepath_name: str) -> str:
        if '.pkl' not in _filepath_name:
            _filepath_name = _filepath_name + '.pkl'
        print("dump_to_file with {0}".format(_filepath_name))

        # STORE SOME EXPORT METADATA
        self.set_additional_data('export_filepath', _filepath_name)
        self.set_additional_data('export_filename', os.path.basename(_filepath_name))

        if self.additional_data['name'] != 'unknown':
            self.set_additional_data('name', os.path.basename(_filepath_name))

        # FINALLY EXPORT TO FILE USING THE self.dump option
        try:
            fout = open(_filepath_name, 'wb')
            fout.write(self.dump())
            fout.close()
        except Exception as e:
            sys.stderr.write(str(e))
            return None
        return _filepath_name
