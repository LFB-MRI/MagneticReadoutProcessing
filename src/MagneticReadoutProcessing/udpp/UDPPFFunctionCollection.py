"""This class only includes static methods which are able to used in a user defined pipeline"""

import os
import re
from pathlib import Path

from import_MRP import __fix_import__
__fix_import__()


from MRP import MRPReading
import  UDPPFLogger
from UDPPFLogger import UDPFLogger as logger


class UDPFFunctionCollectionException(Exception):
    def __init__(self, message="UDPFFunctionCollectionException thrown"):
        self.message = message
        super().__init__(self.message)


class UDPFFunctionCollection:
    """This class only includes static methods which are able to used in a user defined pipeline"""

    @staticmethod
    def concat_readings(set_a: [MRPReading.MRPReading], set_b: [MRPReading.MRPReading]) -> [MRPReading.MRPReading]:
        pass
    @staticmethod
    def import_readings(input_folder:str = "", file_regex: str = "(.)*.mag.json") -> [MRPReading.MRPReading]:
        """
        Imports all readings found in the folder given from the input_folder.
        It restores all meta-data and datapoints.

        :param input_folder: Folder with .mag.json readings ABS or REL-Paths are allowed
        :type input_folder: str

        :param file_regex: to only allow certain filenames using a regex string
        :type file_regex: str

        :returns: Returns the imported readings as [MRPReading.MRPReading] instances
        :rtype: [MRPReading.MRPReading]
        """

        if input_folder is None or len(input_folder) <= 0:
            raise UDPFFunctionCollectionException("import_readings: input_folder parameter empty")
        # CHECK FOLDER EXISTS
        if not str(input_folder).startswith('/'):
            input_folder = str(Path(input_folder).resolve())
        # GET LOGGER
        log: logger = UDPPFLogger.UDPFLogger()
        log.run_log("import_readings: input_folder parameter set to {}".format(input_folder))

        # CHECK FOLDER EXISTS
        if not os.path.exists(input_folder):
            raise UDPFFunctionCollectionException("import_readings: input_folder parameter does not exist on the system".format(input_folder))



        # IMPORT READINGS
        readings_to_import: [str] = [f for f in os.listdir(input_folder) if re.match(r'{}'.format(file_regex), f)]
        imported_results: [MRPReading.MRPReading] = []
        for rti in readings_to_import:
            log.run_log("import_readings: import reading {}".format(rti))
            reading: MRPReading.MRPReading = MRPReading.MRPReading()
            reading.load_from_file(rti)
            imported_results.append(reading)

        return imported_results






# TODO ADD FUNTIONS HERE AND PREPARE INPUT OUTPUT