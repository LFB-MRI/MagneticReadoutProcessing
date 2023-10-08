"""This class only includes static methods which are able to used in a user defined pipeline"""

import os
import re
from pathlib import Path

from import_MRP import __fix_import__
__fix_import__()


from MRP import MRPReading
from MRP import MRPSimulation
import  UDPPFLogger
from UDPPFLogger import UDPFLogger as logger


class UDPPFunctionCollectionException(Exception):
    def __init__(self, message="UDPFFunctionCollectionException thrown"):
        self.message = message
        super().__init__(self.message)


class UDPPFunctionCollection:
    """This class only includes static methods which are able to used in a user defined pipeline"""


    @staticmethod
    def simulate_magnet(IP_count: int = 1, IP_random_polarisation: bool = False, IP_random_magnetisation: bool = False) -> [MRPReading.MRPReading]:
        ret: [MRPReading.MRPReading] = []

        for idx in range(IP_count):
            rnd = MRPSimulation.MRPSimulation.generate_reading(_randomize_magnetization=IP_random_polarisation, _add_random_polarisation=IP_random_magnetisation)
            rnd.set_additional_data("simulate_magnet", idx)
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
    def inspect_readings(readings: [MRPReading.MRPReading]):
        """
        prints some information about a set of readings

        :param readings: readings to inspect
        :type readings: [MRPReading.MRPReading]
        """
        if readings is None or len(readings) <= 0:
            raise UDPPFunctionCollectionException("inspect_readings: readings parameter empty")

        for r in readings:
            print(r.get_name())

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
    def import_readings(IP_input_folder:str = "", IP_file_regex: str = "(.)*.mag.json") -> [MRPReading.MRPReading]:
        """
        Imports all readings found in the folder given from the input_folder.
        It restores all meta-data and datapoints.

        :param IP_input_folder: Folder with .mag.json readings ABS or REL-Paths are allowed
        :type IP_input_folder: str

        :param IP_file_regex: to only allow certain filenames using a regex string
        :type IP_file_regex: str

        :returns: Returns the imported readings as [MRPReading.MRPReading] instances
        :rtype: [MRPReading.MRPReading]
        """

        if IP_input_folder is None or len(IP_input_folder) <= 0:
            raise UDPPFunctionCollectionException("import_readings: input_folder parameter empty")
        # CHECK FOLDER EXISTS
        if not str(IP_input_folder).startswith('/'):
            input_folder = str(Path(IP_input_folder).resolve())
        # GET LOGGER
        log: logger = UDPPFLogger.UDPFLogger()
        log.run_log("import_readings: input_folder parameter set to {}".format(IP_input_folder))

        # CHECK FOLDER EXISTS
        if not os.path.exists(IP_input_folder):
            raise UDPPFunctionCollectionException("import_readings: input_folder parameter does not exist on the system".format(input_folder))



        # IMPORT READINGS
        readings_to_import: [str] = [f for f in os.listdir(IP_input_folder) if re.match(r'{}'.format(IP_file_regex), f)]
        imported_results: [MRPReading.MRPReading] = []
        for rti in readings_to_import:
            log.run_log("import_readings: import reading {}".format(rti))
            reading: MRPReading.MRPReading = MRPReading.MRPReading()
            reading.load_from_file(rti)
            imported_results.append(reading)

        return imported_results


