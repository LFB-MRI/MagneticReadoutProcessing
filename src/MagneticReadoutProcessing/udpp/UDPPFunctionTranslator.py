import os
from pathlib import Path
import yaml

from MRP import MRPReading, MRPAnalysis

import inspect
from optparse import OptionParser
from UDPPFFunctionCollection import UDPFFunctionCollection
def foo(a, b, x='blah'):
    pass


# (a, b, x='blah')

class UDPPFunctionTranslator():

    @staticmethod
    def load_pipelines(_folder: str) -> dict:
        if _folder is None or len(_folder) <= 0:
            raise Exception("load_pilelines: input_folder parameter empty")
        # CHECK FOLDER EXISTS
        if not str(_folder).startswith('/'):
            _folder = str(Path(_folder).resolve())

        print("import_readings: input_folder parameter set to {}".format(_folder))

        # CHECK FOLDER EXISTS
        if not os.path.exists(_folder):
            raise Exception("load_pilelines: _folder parameter does not exist on the system".format(_folder))

        # LOAD ALL ENABLES PIPELINES
        yamls_to_import: [str] = [f for f in os.listdir(_folder) if str(f).endswith('.yaml')]
        enabled_pipelines:dict = {}
        for pipeline_yaml_file in yamls_to_import:
            print("loading pipeline {}".format(pipeline_yaml_file))
            # LOAD YAML FILE
            pip: dict = {}
            with open(str(Path(_folder).joinpath(pipeline_yaml_file)), 'r') as file:
                pip = yaml.safe_load(file)

            if pip is None:
                raise Exception("load_pilelines: failed to load pipeline. file may empty or permissions denied".format(pip))

            # CHECK SETTINGS AND ADD TO LIST IF ENABLED
            if 'settings' in pip and 'enabled' in pip['settings'] and pip['settings']:
                name: str = pipeline_yaml_file
                if 'name' in pip and len(pip['name']) >= 0:
                    name = pip['name']

                enabled_pipelines[name] = pip

        return enabled_pipelines
    @staticmethod
    def strip_function_parameter_types(_typestr: str) -> str:
        # type(instance).__name__ doesnt works on [MRP.reading] returns list only
        return _typestr.replace("<class '", "").replace("'>", "").replace("[", "list(").replace("]", ")")

    @staticmethod
    def listfunctions() -> dict:
        method_list = [func for func in dir(UDPFFunctionCollection) if callable(getattr(UDPFFunctionCollection, func)) and not func.startswith("__")]

        resultdict = {}

        for method in method_list:
            # get function object by name:string
            function_obj = getattr(UDPFFunctionCollection, method)
            # get
            inspect_result: inspect.FullArgSpec = inspect.getfullargspec(function_obj)

            # EXTRACT FUNCTION PARAMETER TYPES
            return_type = None
            parameter_types = {}
            for k in inspect_result.annotations:
                v= inspect_result.annotations[k]

                if k == 'return':
                    return_type = UDPPFunctionTranslator.strip_function_parameter_types(str(v))
                else:
                    parameter_types[k] = UDPPFunctionTranslator.strip_function_parameter_types(str(v))

            resultdict[method] = {
                'name': method,
                'parameter_names': inspect_result.args,
                'parameter_types': parameter_types,
                'default': inspect_result.defaults,
                'return': return_type
            }

        return resultdict
    def __init__(self):
        pass


