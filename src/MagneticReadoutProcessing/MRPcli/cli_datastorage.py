from dotenv import load_dotenv, dotenv_values
import os
from enum import Enum
from tinydb import TinyDB, Query
from pathlib import Path
class CLIDatastorageEntries(Enum):
    SENSOR_SERIAL_DEVICE_PATH = 0
    SENSOR_SERIAL_NAME = 1
    CONFIG_NAME = 2
    READING_PREFIX = 3
    READING_OUTPUT_FOLDER = 4
    READING_DATAPOINT_COUNT = 5
    READING_AVERAGE_COUNT = 6
    READING_MAGNET_TYPE = 7
    SENSOR_SERIAL_BAUDRATE = 8


class CLIDatastorageConfig(object):

    BASE_PATH: str = os.path.dirname(__file__)
    BASE_PATH_CONFIGS: str = BASE_PATH + '/configs/'
    BASEPATH_READINGS: str = BASE_PATH + '/readings/'

    def __init__(self):
        pass



    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CLIDatastorageConfig, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    @staticmethod
    def get_basepath() -> str:
        return CLIDatastorageConfig.BASE_PATH

    @staticmethod
    def set_basepath(_path: str):
        if len(_path) <= 0:
            return
        if not _path.endswith("/"):
            _path += "/"

        CLIDatastorageConfig.BASE_PATH = _path
        CLIDatastorageConfig.BASE_PATH_CONFIGS = _path + 'configs/'
        CLIDatastorageConfig.BASEPATH_READINGS = _path + 'readings/'

        Path(CLIDatastorageConfig.BASE_PATH).mkdir(parents=True, exist_ok=True)
        Path(CLIDatastorageConfig.BASE_PATH_CONFIGS).mkdir(parents=True, exist_ok=True)
        Path(CLIDatastorageConfig.BASEPATH_READINGS).mkdir(parents=True, exist_ok=True)





class CLIDatastorage(object):
    _instance = None

    db: TinyDB
    cfgfp: str = ""
    cfgname: str = "global"


    @staticmethod
    def get_config_basepath() ->str:
        return CLIDatastorageConfig.get_basepath() + '/configs/'

    @staticmethod
    def get_readings_basepath() -> str:
        return CLIDatastorageConfig.get_basepath() + '/readings/'

    @staticmethod
    def get_config_filepath() ->str:
        return CLIDatastorageConfig.get_basepath() + 'global_config.json'

    @staticmethod
    def list_configs():
        bp = CLIDatastorage.get_config_basepath()
        files = [f for f in os.listdir(bp)]
        r = []
        for f in files:
            if f.endswith('_config.json'):
                r.append(os.path.splitext(f)[0].strip('_config'))
        return r


    def __init__(self, _alternative_config_file:str = None):

        pf = CLIDatastorage.get_config_filepath()

        if _alternative_config_file is not None and len(_alternative_config_file) > 0:
            # remove last .extention
            _alternative_config_file = os.path.splitext(_alternative_config_file)[0]
            # append new one todo rework
            if not _alternative_config_file.endswith('_config.json'):
                _alternative_config_file = _alternative_config_file + '_config.json'

            pf = CLIDatastorage.get_config_basepath() + _alternative_config_file

            self.cfgname = _alternative_config_file


        Path(CLIDatastorage.get_config_basepath()).mkdir(parents=True, exist_ok=True)
        self.db = TinyDB(pf)
        self.cfgfp = pf

        # INIT DEFAULT VALUES
        self.init()

    def config_filepath(self) -> str:
        return self.cfgfp


        # lists all found config .json files in folder

    def reset(self):
        self.set_value(CLIDatastorageEntries.SENSOR_SERIAL_DEVICE_PATH, "")
        self.set_value(CLIDatastorageEntries.SENSOR_SERIAL_NAME, "")
        self.set_value(CLIDatastorageEntries.READING_PREFIX, "")
        self.set_value(CLIDatastorageEntries.READING_OUTPUT_FOLDER, CLIDatastorage.get_readings_basepath())
        self.set_value(CLIDatastorageEntries.READING_DATAPOINT_COUNT, "1")
        self.set_value(CLIDatastorageEntries.READING_AVERAGE_COUNT, "1")
        self.set_value(CLIDatastorageEntries.READING_MAGNET_TYPE, "0")
        self.set_value(CLIDatastorageEntries.SENSOR_SERIAL_BAUDRATE, "115200")




    def init(self):
        # check if each key is present int the config file, else add them and write file back
        for data in CLIDatastorageEntries:
            q = Query()
            r = self.db.search(q.key == data.name)
            if len(r) <= 0:
                self.db.insert({'key': data.name, 'value': '', 'cfg_name': self.cfgname})


    def set_value(self, _key: CLIDatastorageEntries, _value:str):
        q = Query()
        self.db.update({'value': str(_value), 'cfg_name': self.cfgname}, q.key == _key.name)


    def get_value(self, _key:CLIDatastorageEntries) -> str:
        q = Query()
        r = self.db.search(q.key == _key.name)
        if len(r) <= 0:
            return ""
        return r[0]['value']

