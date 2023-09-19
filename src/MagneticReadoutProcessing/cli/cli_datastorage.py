from dotenv import load_dotenv, dotenv_values
import os
from dataclasses import dataclass
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

class CLIDatastorage:


    db: TinyDB


    @staticmethod
    def get_config_basepath() ->str:
        return (os.path.dirname(__file__)+'/configs/')

    @staticmethod
    def get_config_filepath() ->str:
        return (CLIDatastorage.get_config_basepath() + 'global_config.json')



    def __init__(self, _alternative_config_file:str = None):

        pf = CLIDatastorage.get_config_filepath()

        if _alternative_config_file is not None and len(_alternative_config_file) > 0:
            # remove last .extention
            _alternative_config_file = os.path.splitext(_alternative_config_file)[0]
            # append new one todo rework
            if not _alternative_config_file.endswith('_config.json'):
                _alternative_config_file = _alternative_config_file + '_config.json'

            pf = CLIDatastorage.get_config_basepath() + _alternative_config_file


        Path(CLIDatastorage.get_config_basepath()).mkdir(parents=True, exist_ok=True)
        self.db = TinyDB(pf)
        self.init()

    def list_configs(self):
        bp = CLIDatastorage.get_config_basepath()
        files = [f for f in os.listdir(bp) if os.path.isfile(f) and f.endswith('_config.json')]
        return files

        # lists all found config .json files in folder


    def init(self):
        # check if each key is present int the config file, else add them and write file back
        for data in CLIDatastorageEntries:
            q = Query()
            r = self.db.search(q.key == data.name)
            if len(r) <= 0:
                self.db.insert({'key': data.name, 'value': ''})


    def set_value(self, _key: CLIDatastorageEntries, _value:str):
        q = Query()
        self.db.update({'value': _value}, q.key == _key.name)
        #self.db.storage.


    def get_value(self, _key:CLIDatastorageEntries) -> str:
        q = Query()
        r = self.db.search(q.key == _key.name)
        if len(r) <= 0:
            return ""
        return r[0]['value']





@dataclass
class Common:
    storage: CLIDatastorage = None

