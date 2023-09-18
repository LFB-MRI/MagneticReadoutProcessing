from dotenv import load_dotenv, dotenv_values
import os
from dataclasses import dataclass
from enum import Enum
from tinydb import TinyDB, Query

class CLIDatastorageEntries(Enum):
    SENSOR_SERIAL_DEVICE_PATH = 0
    SENSOR_SERIAL_NAME = 1
    READING_PREFIX = 2
    READING_OUTPUT_FOLDER = 3
    READING_DATAPOINT_COUNT = 4
    READING_AVERAGE_COUNT = 5

class CLIDatastorage:


    db: TinyDB
    @staticmethod
    def get_dotenv_path() ->str:
        return (os.path.dirname(__file__)+'/config.json')


    def __init__(self):
        self.db = TinyDB(CLIDatastorage.get_dotenv_path())


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


    def get_value(self, _key:CLIDatastorageEntries) -> str:
        q = Query()
        r = self.db.search(q.key == _key.name)
        if len(r) <= 0:
            return ""
        return r[0]['value']





@dataclass
class Common:
    storage: CLIDatastorage = None

