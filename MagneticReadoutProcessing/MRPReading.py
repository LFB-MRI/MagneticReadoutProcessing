import os.path
import pickle
from datetime import datetime

import numpy as np
from .MRPConfig import MRPConfig
import pickle
import sys
import math
from MRPHelpers import translate as reading_helper_translate


class MRPReading(object):


    #time_start = None
    #time_end = None
    #data = []
    #measurement_config = dict()
    #config = dict()
    #additional_data = dict()

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
                'sensor_distance_radius': self.config['MEASUREMENT']['MEASUREMENT_SENSOR_MAGNET_DISTANCE']
            })

        # THE SENSOR RADIUS CAN DIFFER
        if _sensor_radius is not None:
            self.measurement_config['sensor_distance_radius'] = _sensor_radius

        if _sensor_id is not None:
            self.measurement_config['sensor_id'] = _sensor_id

    def load(self, _filepath_name: str):
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

    def to_numpy_cartesian(self, _normalize: bool = False, _fill_empty_datapoints_with_zero: bool = True) -> np.array:
        # X Y Z GRID
        sensor_distance_radius = self.measurement_config['sensor_distance_radius']
        polar = self.to_numpy_polar(_normalize, _fill_empty_datapoints_with_zero)
        #x = sensor_distance_radius * np.sin(self.theta) * np.cos(self.phi)
        #y = sensor_distance_radius * np.sin(self.theta) * np.sin(self.phi)
        #z = sensor_distance_radius * np.cos(self.theta)
    # TODO MERGE WITH VISUALISATION ROUTINES AND ALLOW NORMALISATION FLAG
    def to_numpy_polar(self, _normalize: bool = False, _fill_empty_datapoint_with_zero: bool = True) -> np.array:
        n_theta = self.measurement_config['n_theta']
        n_phi = self.measurement_config['n_phi']
        theta_radians = self.measurement_config['theta_radians']
        phi_radians = self.measurement_config['phi_radians']

        # CREATE A POLAR COORDINATE GRID
        theta, phi = np.mgrid[0.0:theta_radians:n_theta * 1j, 0.0:phi_radians:n_phi * 1j]

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

        inp = []  # 1D ARRAY WILL BE RESHAPED LATER ON
        for j in phi[0, :]:
            for i in theta[:, 0]:
                added = False
                # CHECK IF DATA EXSITS
                for r in self.data:
                    dj = r['phi']
                    di = r['theta']

                    if j == dj and i == di:
                        value = r['value']
                        # NORMALIZE IF NEEDED
                        if _normalize:
                            normalized_value = reading_helper_translate(value, min_val, max_val, -1.0, 1.0)
                            inp.append([j, i, normalized_value])
                        else:
                            inp.append([j, i, value])
                        added = True
                        break
                # FILL EMPTY POINTS WITH ZERO IF ENABLED
                if not added and _fill_empty_datapoint_with_zero:
                    inp.append([j, i, 0.0])

        # PERFORM RESHAPE AND NUMPY CONVERSION
        inp = np.array(inp)
        # reshape the input array to the shape of the x,y,z arrays.
        reshaped_reading_results = inp[:, 2].reshape((n_phi, n_theta)).T

        return reshaped_reading_results


    def update_data_from_numpy_polar(self, _numpy_array: np.ndarray):
        n_theta = self.measurement_config['n_theta']
        n_phi = self.measurement_config['n_phi']
        theta_radians = self.measurement_config['theta_radians']
        phi_radians = self.measurement_config['phi_radians']
        # CREATE A POLAR COORDINATE GRID
        theta, phi = np.mgrid[0.0:theta_radians:n_theta * 1j, 0.0:phi_radians:n_phi * 1j]

        for j in self.phi[0, :]:
            for i in theta[:, 0]:
                added = False
                # CHECK IF DATA EXSITS
                for r in self.data:
                    dj = r['phi']
                    di = r['theta']
        # TODO FIX
        # DELETE OLD DATA INSERT NEW DATA
        # SO ITERATE THROUGH NP ARRAY AND SPLIT THE THREE COMPONETNS


    def insert_reading(self, _reading: float, _phi: float, _theta: float, _reading_index_phi: int,
                       _reading_index_theta: int, _temp: float = None) -> None:
        if len(self.data) <= 0:
            self.time_start = datetime.now()
        self.time_end = datetime.now()
        entry = dict({
            "value": _reading,
            "phi": _phi,
            "theta": _theta,
            "reading_index_phi": _reading_index_phi,
            "reading_index_theta": _reading_index_theta,
            "temperature": _temp
        })
        self.data.append(entry)

    def dump(self) -> bytes:
        dump_time = datetime.now()

        final_dataset = dict({
            'dump_time': datetime.now(),
            'time_start': self.time_start,
            'time_end': self.time_end,
            'config': self.config,
            'data': self.data,
            'measurement_config': self.measurement_config,
            'additional_data': self.additional_data
        })
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
        try:
            fout = open(_filepath_name, 'wb')
            fout.write(self.dump())
            fout.close()
        except Exception as e:
            sys.stderr.write(str(e))
            return None
        return _filepath_name
