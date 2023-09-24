import os
from pathlib import Path
import yaml

import networkx as nx

from import_MRP import __fix_import__
__fix_import__()


import inspect
from optparse import OptionParser
from UDPPFFunctionCollection import UDPFFunctionCollection




# (a, b, x='blah')

class UDPPFunctionTranslator():



    @staticmethod
    def create_calltree_graph(_pipelines: dict) -> nx.Graph:
        if _pipelines is None or len(_pipelines) <= 0:
            raise Exception("create_calltree: _pipelines parameter empty")

        # using graphs to create the calltree
        # later we use algorithms
        calltree: nx.Graph = nx.Graph()

        # ADD PIPELINE STEPS AS NODES
        for p_k, p_v in _pipelines.items():
            calltree.add_node("{}".format(p_k))

        # ADD EDGES
        #
        for p_k, p_v in _pipelines.items():
            # u -> v
            # check each paramter
            for param_k, param_v in p_v['parameters'].items():
                param_name = str(param_k)
                param_value:str = str(param_v)
                if 'stage ' in param_value:
                    param_value:str = param_value.replace('stage ', '')
                    if param_value in _pipelines:
                        # add edges from function using this parameter to function
                        calltree.add_edge(param_value, p_k)
        #calltree.show("gameofthrones.html")


        # find circles in the graph
        # to avoid processing endless loops
        try:
            circle_edges = nx.find_cycle(calltree, orientation="original") # original = follow edge -> !
            if len(circle_edges) > 0:
                raise Exception("create_calltree:stages contains circles in {}".format(circle_edges))
        except nx.exception.NetworkXNoCycle as e:
            pass
            # all good no cycle :)

        return calltree

    @staticmethod
    def get_startsteps(_pipelines: dict) -> [str]:
        if _pipelines is None or len(_pipelines) <= 0:
            raise Exception("get_startstep: _pipelines parameter empty")
        ret: [str] = []
        for p_k, p_v in _pipelines.items():
            has_stage_input_parameter: bool = False
            for param_k, param_v in p_v['parameters'].items():
                param_value: str = str(param_v)
                if 'stage ' in param_value:
                    has_stage_input_parameter = True
            # no stage input parameter dependencies
            if not has_stage_input_parameter:
                ret.append(p_k)

        return ret


    @staticmethod
    def extract_pipelines_steps(_pipeline: dict):
        if _pipeline is None or len(_pipeline) <= 0:
            raise Exception("extract_pipelines_steps: _pipeline parameter empty")

        result_steps: dict = {}
        step_counter: dict = {}

        for p_k, p_v in _pipeline.items():
            k:str = str(p_k)
            # LEGACY SUPPORT
            k = k.replace('step ', 'stage ')

            if k.startswith('stage '):
                step_name: str = k.split(' ')[1]
                # check for step name
                if step_name is None or len(step_name) <= 0:
                    raise Exception("invalid step name for {}".format(p_k))
                # check for duplicate steps
                if step_name in step_counter:
                    raise Exception("duplicate step  {} exists".format(p_k))
                else:
                    step_counter[step_name] = 1

                result_steps[step_name] = p_v

        return result_steps




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
        enabled_pipelines: dict = {}
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
        method_list: [str] = [func for func in dir(UDPFFunctionCollection) if callable(getattr(UDPFFunctionCollection, func)) and not func.startswith("__")]

        resultdict: dict = {}

        for method in method_list:
            # get function object by name:string
            function_obj = getattr(UDPFFunctionCollection, method)
            # get
            inspect_result: inspect.FullArgSpec = inspect.getfullargspec(function_obj)

            # EXTRACT FUNCTION PARAMETER TYPES
            return_type: str = None
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

    



