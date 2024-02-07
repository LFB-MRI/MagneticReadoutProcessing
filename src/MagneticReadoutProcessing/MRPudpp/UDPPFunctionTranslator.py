"""This class is handling all the pipeline translations between the user level and the actual python function execution"""
import os
import queue
import random
import typing
from pathlib import Path
import yaml
import networkx as nx
from matplotlib import pyplot as plt


import inspect
from optparse import OptionParser
from MRPudpp.UDPPFunctionCollection import UDPPFunctionCollection


class UDPPFunctionTranslatorException(Exception):
    def __init__(self, message="UDPPFunctionTranslatorException thrown"):
        self.message = message
        super().__init__(self.message)


class IterableQueue():
    """simple queue pyrhon iterator, which allows iteration and insertion of new items during iteration"""

    def __init__(self, source_queue):
        self.source_queue = source_queue

    def __iter__(self):
        while True:
            try:
                yield self.source_queue.get_nowait()
            except queue.Empty:
                return


# (a, b, x='blah')


class UDPPFunctionTranslator():
    """This class is handling all the pipeline translations between the user level and the actual python function execution"""

    @staticmethod
    def execute_stage_funktion(stage_information: dict, intermediate_results: dict) -> typing.Any:
        stage_function_name: str = stage_information['function']
        function_parameters_from_stages: [dict] = UDPPFunctionTranslator.get_stage_parameters(stage_information)
        function_parameters_from_inspector: [dict] = UDPPFunctionTranslator.get_function_parameters(stage_function_name, _get_inspector_parameter=True)
        # POPULATE PARAMETER DICT
        parameters: dict = {}

        ## PROCESS PARAMETERS FROM FROM OTHER STAGES
        if len(function_parameters_from_stages) > 0:
            for otp_entry in function_parameters_from_stages:
                p_stage_name: str = otp_entry['stage_name']
                p_parameter_name: str = otp_entry['parameter_name']

                if p_stage_name not in intermediate_results:
                    raise Exception("cant find {} in intermediate_results".format(p_parameter_name))

                parameters[p_parameter_name] = intermediate_results[p_stage_name]

        ## PROCESS INSPECTOR PARAMETER
        for ip_entry in function_parameters_from_inspector:
            name: str = ip_entry['id']

            # TODO COMPLEX TYPES as json objects ?

            value = None
            # ASSIGN DEFAULT VALUE
            if 'value' in ip_entry:
                value = ip_entry['value']

            # OVERRIDE USER GIVEN PARAMETER VALUE
            if 'parameters' in stage_information:
                if name in stage_information['parameters']:
                    _value = stage_information['parameters'][name]
                    if _value:
                        value = _value
                    else:
                        value = None

            parameters[name] = value

        # EXECUTE FUNCTION STORE RETURN RESULT
        print("processing function:{}".format(stage_function_name))
        fkt_call_result = UDPPFunctionTranslator.execute_function_by_name(stage_function_name, parameters)

        return fkt_call_result


    @staticmethod
    def execute_function_by_name(_function_name: str, _parameters: dict) -> typing.Any:
        if not _function_name or len(_function_name) <= 0:
            raise Exception("execute_function_by_name: _function_name")

        function_object = getattr(UDPPFunctionCollection, _function_name)
        #try:
        ret: typing.Any = function_object(**_parameters)
        return ret
        #except Exception as e:
        #return None
    @staticmethod
    def get_parameter_from_step(_pipelines: dict, _step: str, _only_step_dependencies: bool = False) -> [str]:
        """
        renders an image of a given nx.Graph for debug purposes

        :param _pipelines: graph to render
        :type _pipelines: nx.DiGraph

        :param _step: export folder of the rendered graph png file
        :type _step: str

        :param _only_step_dependencies: if true only stage input parameters a returned
        :type _only_step_dependencies: str

        :returns: returns the input parameters of a given pipeline stage
        :rtype: [str]
        """
        ret: list[str] = []

        step: dict = _pipelines[_step]
        for param_k, param_v in step['parameters'].items():
            param_value: str = str(param_v)

            if not _only_step_dependencies:
                ret.append(param_value)
            elif 'stage ' in param_value:
                param_value: str = param_value.replace('stage ', '')
                ret.append(param_value)

        return ret

    @staticmethod
    def check_functions_exists(_pipelines: dict):
        """
        checks for every stage that the used function in function: <xY> exists in the UDPPFFuntionCollection file
        Raises exception if not valid
        :param _pipelines: graph to render
        :type _pipelines: nx.DiGraph

        :param _calltree_graph: graph  with the connected functions
        :type _calltree_graph: nx.DiGraph

        :returns: returns if all stage parameters are matched to each other if stages are connected
        :rtype: bool
        """

        functions: [str] = UDPPFunctionTranslator.listfunctions().keys()

        for stage_k, stage_v in _pipelines.items():
            if 'function' in stage_v:
                fkt: str = stage_v['function']
                if not fkt in functions:
                    raise UDPPFunctionTranslatorException(
                        "function value ({}) for stage: {} is invalid or not present in UDPPFunctionCollection".format(
                            fkt, stage_k))
            else:
                raise UDPPFunctionTranslatorException("function is not defined in stage: {}".format(stage_k))

        return True

    @staticmethod
    def get_function(_function_name: str) -> dict:
        functions: dict = UDPPFunctionTranslator.listfunctions()

        if not _function_name in functions:
            raise UDPPFunctionTranslatorException(
                "get_function: function name with this name does not exists {}".format(_function_name))

        function: dict = functions[_function_name]
        return function

    @ staticmethod
    def get_stage_parameters(step_information: dict) -> [dict]:
        ret: [dict] = []
        if 'parameters' in step_information:
            for k,v in step_information.get('parameters').items():
                if 'IP_' not in k and 'stage ' in v:
                    stage_name: str = str(v).replace('stage ', '')
                    parameter_name: str = k
                    ret.append({
                        'stage_name': stage_name,
                        'parameter_name': parameter_name
                    })

        return ret
    @staticmethod
    def get_function_parameters(_function_name: str, _get_inspector_parameter: bool = False, _strip_prefix: bool = False) -> [str]:
        """
        returns the readable version of a function parameters, including name, type and default value

        :param _function_name: function name to get return types from
        :type _function_name: str

        :param _get_inspector_parameter: get all parameters with IP_ prefix for the user inspector view
        :type _get_inspector_parameter: bool

        :param _strip_prefix: strip IP_ prefix if _get_inspector_parameter is set
        :type _strip_prefix: bool

        :returns: returns all function parameters in a list of dicts with name, value and type properties
        :rtype: [str]
        """
        fkt: dict = UDPPFunctionTranslator.get_function(_function_name=_function_name)
        res: [str] = []
        types: dict = fkt['parameter_types']
        defaults: dict = fkt['default']
        for k, v in types.items():
            if _get_inspector_parameter and 'IP_' not in k:
                continue
            elif not _get_inspector_parameter and  'IP_' in k:
                continue

            d = ""
            if k in defaults:
                d = defaults[k]
            res.append({'id': '{}'.format(k), 'name': str(k).replace('IP_',''), 'type': v, 'value': d})
        return res
    @staticmethod
    def get_inspector_parameters(_function_name: str, _strip_prefix: bool = False) -> []:
        """
        returns the readable version of a function inspector parameters selected by IP_ prefix, including name, type and default value

        :param _function_name: function name to get return types from
        :type _function_name: str

        :param _strip_prefix: strip IP_ prefix
        :type _strip_prefix: bool

        :returns: returns all inspector function parameters in a list of dicts with name, value and type properties
        :rtype: [str]
        """
        return UDPPFunctionTranslator.get_function_parameters(_function_name, _get_inspector_parameter=True, _strip_prefix=_strip_prefix)
    @staticmethod
    def get_function_return_parameters(_function_name:str) -> []:
        returns: [] = []
        rt: [str] = UDPPFunctionTranslator.get_function_return_types(_function_name)
        for r in rt:
            if len(r) <= 0:
                continue
            returns.append({'id': '{}'.format(r), 'name': '{}'.format(r), 'type': '{}'.format(r)})
        return returns

    @staticmethod
    def get_node_connection_list( _calltree_graph: nx.DiGraph) -> []:
        """
        Returns all node /edge connections to use for visualization to get the connections between all nodes.
        Speical here is the usage of edge data to store the parameter name in it.
        This function returns the edges as from function parameter to function parameter

        :param _calltree_graph: list of edges with annotated functions/parameter names as dict
        :type _calltree_graph: []


        :returns: returns all inspector function parameters in a list of dicts with name, value and type properties
        :rtype: [str]
        """
        ret: [] = []
        for e in _calltree_graph.edges:
            ed = _calltree_graph.get_edge_data(e[0], e[1])
            if len(ed) > 0 and 'from_parameter_name' in ed and 'to_parameter_name' in ed:
                ret.append({
                    'from': {
                        'stage_name': e[0],
                        'parameter_name': 'return' #str(ed['from_parameter_name']).replace('stage ', '')
                    },
                    'to': {
                        'stage_name': e[1],
                        'parameter_name': ed['to_parameter_name']
                    }
                })

        return ret

    @staticmethod
    def get_function_return_types(_function_name: str) -> [str]:
        """
        returns the readable return type of a given function

        :param _function_name: function name to get return types from
        :type _function_name: str

        :returns: returns if all stage parameters are matched to each other if stages are connected
        :rtype: [str]
        """
        if _function_name is None or len(_function_name) <= 0:
            raise UDPPFunctionTranslatorException("get_function_return_type: _function_name is empty")

        functions: dict = UDPPFunctionTranslator.listfunctions()

        if not _function_name in functions:
            raise UDPPFunctionTranslatorException(
                "get_function_return_type: function name with this name does not exists {}".format(_function_name))

        function: dict = functions[_function_name]
        # extract return type
        # TODO ADD SUPPORT FOR TUPLES
        if 'return' in function and function['return'] is not None:
            return [function['return']]
        return []

    @staticmethod
    def check_parameter_types(_pipelines: dict, _calltree_graph: nx.DiGraph) -> bool:
        """
        checks for each connected pipeline stage the parameter types for input/return value

        :param _pipelines: graph to render
        :type _pipelines: nx.DiGraph

        :param _calltree_graph: graph  with the connected functions
        :type _calltree_graph: nx.DiGraph

        :returns: returns if all stage parameters are matched to each other if stages are connected
        :rtype: bool
        """

        functions: dict = UDPPFunctionTranslator.listfunctions()

        for stage_k, stage_v in _pipelines.items():
            caller_fkt: dict = stage_v['function']
            caller_types: dict = functions[caller_fkt]['parameter_types']
            # get the parameter to which
            # the get_parameter_from_step function returns the input parameter
            stage_stage_input_functions_name: [str] = UDPPFunctionTranslator.get_parameter_from_step(_pipelines,
                                                                                                     stage_k, False)

            for idx, stage_stage_input_function_name in enumerate(stage_stage_input_functions_name):

                if 'stage ' not in stage_stage_input_function_name:
                    continue
                stage_stage_input_function_name_stripped = str(stage_stage_input_function_name).replace('stage ', '')
                callee_function_name: str = _pipelines[stage_stage_input_function_name_stripped]['function']
                callee_function_types: dict = functions[callee_function_name]
                callee_function_type_return: str = callee_function_types['return']

                caller_function_type_input: str = list(caller_types.values())[idx]
                if not caller_function_type_input == callee_function_type_return:
                    raise UDPPFunctionTranslatorException(
                        "connected cuntion type didnt match return {} -> imput_parameter {}".format(
                            callee_function_type_return, caller_function_type_input))

        return True

    @staticmethod
    def plot_graph(graph: nx.DiGraph, _export_graph_plots: str = None, _filename: str = "graphplot",
                   _title: str = "graph_plot"):
        """
        renders an image of a given nx.Graph for debug purposes

        :param graph: graph to render
        :type graph: nx.DiGraph

        :param _export_graph_plots: export folder of the rendered graph png file
        :type _export_graph_plots: str

        :param _filename: filename
        :type _filename: str

        :param _title: headline of the render backed into the image
        :type _title: str
        """
        nx.draw_planar(graph, with_labels=True)
        plt.title("{}".format(_title))
        if _export_graph_plots is not None and len(_export_graph_plots) > 0:
            _export_graph_plots = _export_graph_plots.replace("//", "/")
            # CREATE FOLDER IF NOT EXIST
            if not os.path.exists(_export_graph_plots):
                os.makedirs(_export_graph_plots)
            plt.savefig(_export_graph_plots + "/{}".format(_filename), dpi=1200)
        else:
            plt.show()
        plt.close()

    @staticmethod
    def create_sub_calltrees(_pipelines: dict, _calltree_graph: nx.DiGraph, _start_steps: [str],
                             _export_graph_plots: str = None) -> [nx.DiGraph]:
        """
        parses the user defined stages into a directed grap in order to determ the order of computation for each function.

        :param _pipelines: pipeline stages directly parsed from the yaml
        :type _pipelines: dict

        :param _calltree_graph: the complete calltree graph from create_calltree_graph()
        :type _pipelines: nx.DiGraph

        :param _start_steps: computed start stages from get_startsteps()
        :type _start_steps: [str]

        :param _export_graph_plots: if set to a folder path, the calculated graphs will be exported as image also
        :type _export_graph_plots: [str]

        :returns: a list of all generated sub call trees in the order of right execution stages
        :rtype: [nx.DiGraph]
        """
        if _start_steps is None or len(_start_steps) <= 0:
            raise Exception("create_sub_calltrees: _start_steps parameter empty or has no start steps")

        subgraphs: [nx.Graph] = []
        visited: dict = {}

        for i in _calltree_graph.nodes:
            visited[i] = False
        # CREATE A SUBGRAPHS UNTIL A NODE WITH TWO STAGE INPUTS IS RANGED FROM THE START STEP
        next_nodes_after_startnodes: [str] = []
        # A QUEUE IS NEEDED TO FIRST PROCESS THE START STAGES AND THEN GOING FURTHER AND FURTHER THE OTHER STAGES ALONG
        nodes_to_process: queue.Queue = queue.Queue()
        for i in _start_steps:
            nodes_to_process.put(i)


        for i in _calltree_graph.nodes:
            if i not in nodes_to_process.queue:
                nodes_to_process.put(i)


        # ITERATE OVER ALL START NODES
        for ss in IterableQueue(nodes_to_process):
            if ss == 'b':
                i = 0
            subgraph: nx.DiGraph = nx.DiGraph()

            # CREATE STARTNODE IN NEW SUBGRAPH
            last_node: str = ss
            if last_node not in list(subgraph.nodes):
                subgraph.add_node(last_node)

            dfs_res: [str] = list(nx.bfs_tree(_calltree_graph, ss))
            print("dfs_res: {}".format(dfs_res))
            # REMOVE FIRST ELEMENT WHICH IS ALWAYS THE START DFS NODE
            dfs_res.pop(0)
            # CHECK FOR EACH NODE ALONG THE DFS RESULT
            # UNIT WE FOUND ONE WITH MORE THAN ONE STEP INPUT PARAMTER
            for dfs_step in dfs_res:
                # get function parameters which are connected with
                # using a df search to follow the current node along its next connected stages
                pdep = UDPPFunctionTranslator.get_parameter_from_step(_pipelines, dfs_step, True)

                # == 1 = then its in === out > with > 1 (2,3) the function hast at least two dependencies
                # => so this indicates the end of the sub-call-graph
                if len(pdep) > 1:
                    # ADD NODE WITH AT LEAST TWO DEPENDENCIES AS A NEW START NODE
                    if dfs_step not in next_nodes_after_startnodes:
                        print("added {} to next after startnodes".format(dfs_step))
                        nodes_to_process.put(dfs_step)
                        # next_nodes_after_startnodes.append(dfs_step)
                        break

                else:
                    # ADD NODES TO SUBGRAPH IF NOT PRESENT
                    if last_node not in list(subgraph.nodes):
                        subgraph.add_node(last_node)

                    if dfs_step not in list(subgraph.nodes):
                        subgraph.add_node(dfs_step)

                    # ADD EDGE
                    subgraph.add_edge(last_node, dfs_step)
                    # STORE A PREDECESSOR
                    last_node = dfs_step  # store last node

                    visited[dfs_step] = True

            # ADD AS NEW SUBGRAPH
            subgraphs.append(subgraph)
            print("subgraph {} with {}".format(len(subgraphs), list(nx.dfs_tree(subgraph, ss))))
            # EXPORT SUBGRAPH AS IMAGE
            UDPPFunctionTranslator.plot_graph(subgraph, _export_graph_plots, "sub_calltree_startstage_{}".format(ss),
                                              "SubCallTree for Start-Stages {}".format(ss))

            # CHECK ALL VISITED
            all_visited: bool = True
            for k, v in visited.items():
                if not v:
                    all_visited = False
            if all_visited:
                break

        return subgraphs

    @staticmethod
    def create_calltree_graph(_pipelines: dict, _export_graph_plots: str = None) -> nx.DiGraph:
        """
        parses the user defined stages into a directed grap in order to determ the order of computation for each function.

        :param _pipelines: pipeline stages directly parsed from the yaml
        :type _pipelines: dict

        :returns: returns a directed graph with edges
        :rtype: nx.DiGraph
        """
        if _pipelines is None or len(_pipelines) <= 0:
            raise Exception("create_calltree: _pipelines parameter empty")

        # using graphs to create the calltree
        # later we use algorithms
        calltree: nx.DiGraph = nx.DiGraph()

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
                param_value: str = str(param_v)
                if 'stage ' in param_value:
                    param_value: str = param_value.replace('stage ', '')
                    if param_value in _pipelines:
                        # add edges from function using this parameter to function
                        edge_data = {
                            'from_parameter_name': param_v,
                            'to_parameter_name': param_k
                        }
                        calltree.add_edge(param_value, p_k)
                        calltree.edges[param_value, p_k].update(edge_data)

        # find circles in the graph
        # to avoid processing endless loops
        try:
            circle_edges = nx.find_cycle(calltree, orientation="original")  # original = follow edge -> !
            if len(circle_edges) > 0:
                raise Exception("create_calltree:stages contains circles in {}".format(circle_edges))
        except nx.exception.NetworkXNoCycle as e:
            pass
            # all good no cycle :)

        # EXPORT GRAPH AS IMAGE
        UDPPFunctionTranslator.plot_graph(calltree, _export_graph_plots, "calltree_graph", "CallTree")

        return calltree

    @staticmethod
    def get_startsteps(_pipelines: dict) -> [str]:
        """
        returns all possible start stages with no input parameter dependencies from other stages, e.g. import_reading functions

        :param _pipelines: pipeline stages (directly parsed from yaml)
        :type _pipelines: dict

        :returns: list of start stages names
        :rtype: [str]
        """
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
    def EDITOR_get_stages_as_array(_pipeline: dict, _canvas_view_size_x:int = 100, _canvas_view_size_y:int = 100) -> []:
        """
        returns all pipelines stage a array representation instead of dict.
        this is used for the web editor

        :param _pipeline: pipeline stages (directly parsed from yaml)
        :type _pipeline: dict

        :returns: returns a modified version for the stages used in EDITOR
        :rtype: []
       """
        
        # calculate position of the nodes
        steps = UDPPFunctionTranslator.extract_pipelines_steps(_pipeline)
        graph: nx.DiGraph = UDPPFunctionTranslator.create_calltree_graph(steps)

        node_positions: [] = nx.drawing.planar_layout(graph, scale=150, center=[_canvas_view_size_x/2, _canvas_view_size_y/2])


        stages: [] = []

        for k, v in UDPPFunctionTranslator.extract_pipelines_steps(_pipeline).items():
            params: [] = []
            inspector_params: [] = []



            # RESOLVE function return value in order to set the output connector
            returns: [] = []
            rt: [str] = UDPPFunctionTranslator.get_function_return_types(v['function'])
            for r in rt:
                if len(r) <= 0:
                    continue
                returns.append({'name': '{}'.format(r), 'type': '{}'.format(r), 'direction': 'output'})


            # fixed position present ? => USE
            pos: dict = {}
            # TODO FIX
            if 'position' not in v and k in node_positions:
                # if node position is calculated, use this
                pos['x'] = int(node_positions[k][0])
                pos['y'] = int(node_positions[k][1])
            elif 'position' not in v:
                # else just a random pos
                xc: int = int(_canvas_view_size_x / 2)
                yc: int = int(_canvas_view_size_y / 2)
                pos['x'] = random.randint(int(xc - (xc/2)), int(xc + (xc/2)))
                pos['y'] = random.randint(int(yc - (yc/2)), int(yc + (yc/2)))





            stages.append({
                'name': k,
                'function': v['function'],
                'parameters': UDPPFunctionTranslator.get_function_parameters(v['function']),
                'inspector': UDPPFunctionTranslator.get_inspector_parameters(v['function']),
                'position': pos,
                'returns': returns,

            })

        # ASSEMBLE CONNECTIONS TOGETHER USING A CAllTREE
        connections: [] = UDPPFunctionTranslator.get_node_connection_list(_calltree_graph=graph)

        res: dict = {
            'settings': _pipeline['settings'],
            'stages': stages,
            'connections': connections
        }

        return res

    @staticmethod
    def extract_pipelines_steps(_pipeline: dict) -> dict:
        """
        returns all stage <name> entries from the parsed yaml dict

        :param _pipelines: pipeline stages (directly parsed from yaml)
        :type _pipelines: dict

        :returns: all stages a dict using stage name as key
        :rtype: dict
        """
        if _pipeline is None or len(_pipeline) <= 0:
            raise Exception("extract_pipelines_steps: _pipeline parameter empty")

        result_steps: dict = {}
        step_counter: dict = {}

        for p_k, p_v in _pipeline.items():
            k: str = str(p_k)
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
    def create_empty_pipeline(_name: str, _folder: str) -> dict:
        """
        creates a empty pipeline file

        :param _name: nane of the new pipeline this also will be the later filename with some variations
        :type _name: str

        :param _folder: storage location for pipeline files
        :type _folder: str

        :returns: returns content of pipeline in same format as load_pipelines
        :rtype: dict
        """
        if _name is None or len(_name) <= 0:
            _name = "pipeline"

        if _folder is None or len(_folder) <= 0:
            raise Exception("create_empty_pipeline: input_folder parameter empty")

        filename: str = _name

        filename.replace("./", "").strip(" /")
        if not filename.endswith(".yaml"):
            filename.replace(".", "_")
            filename = filename + ".yaml"

        _name = _name.replace(".yaml", "")

        pipeline_content: dict = {
            'settings': {
                'name': "{}".format(_name),
                'enabled': True,
                'export_intermediate_results': True
            }
        }

        # CHECK FOLDER EXISTS
        if not str(_folder).startswith('/'):
            _folder = str(Path(_folder).resolve())

        print("create_empty_pipeline: storage location folder set to {}".format(_folder))

        # CHECK FOLDER EXISTS
        if not os.path.exists(_folder):
            raise Exception("create_empty_pipeline: _folder parameter does not exist on the system".format(_folder))
        exp_path: Path = Path.joinpath(Path(_folder), Path(filename))

        with open(str(exp_path), 'w') as file:
            yaml.dump(pipeline_content, file)

        res: dict = {}
        res[filename] = pipeline_content
        return res

    @staticmethod
    def load_pipelines(_folder: str, _log: bool = True) -> dict:
        """
        load all found yaml pipeline files into a dict
        but only pipelines with the settings entry enabled set to true.
        so it's possible to enable and disable pipelines during pipeline run command execution

        :param _folder: folder with
        :type _folder: str

        :returns: all enabled pipelines as parsed yaml dict
        :rtype: dict
        """
        if _folder is None or len(_folder) <= 0:
            raise Exception("load_pipelines: input_folder parameter empty")
        # CHECK FOLDER EXISTS
        if not str(_folder).startswith('/'):
            _folder = str(Path(_folder).resolve())

        if _log:
            print("import_readings: input_folder parameter set to {}".format(_folder))

        # CHECK FOLDER EXISTS
        if not os.path.exists(_folder):
            raise Exception("load_pilelines: _folder parameter does not exist on the system".format(_folder))

        # LOAD ALL ENABLES PIPELINES
        yamls_to_import: [str] = [f for f in os.listdir(_folder) if str(f).endswith('.yaml')]
        enabled_pipelines: dict = {}
        for pipeline_yaml_file in yamls_to_import:
            if _log:
                print("loading pipeline {}".format(pipeline_yaml_file))
            # LOAD YAML FILE
            pip: dict = {}
            with open(str(Path(_folder).joinpath(pipeline_yaml_file)), 'r') as file:
                pip = yaml.safe_load(file)

            if pip is None:
                raise Exception(
                    "load_pilelines: failed to load pipeline. file may empty or permissions denied".format(pip))

            # CHECK SETTINGS AND ADD TO LIST IF ENABLED
            if 'settings' in pip and 'enabled' in pip['settings'] and pip['settings']:
                name: str = pipeline_yaml_file
                if 'name' in pip and len(pip['name']) >= 0:
                    name = pip['name']

                enabled_pipelines[name] = pip

        return enabled_pipelines

    @staticmethod
    def strip_function_parameter_types(_typestr: str) -> str:
        """
        simplifies the python object typestring for function parameters e.g.:
        [<class MRPReading>] => list(MRPReading)

        :param _typestr: input from inspect.getfullargspec(function_obj) for a given function as string
        :type _typestr: str

        :returns: returns more human readable name of the type
        :rtype: str
        """
        # type(instance).__name__ doesnt works on [MRP.reading] returns list only
        return _typestr.replace("<class '", "").replace("'>", "").replace("[", "list(").replace("]", ")")


    @staticmethod
    def listfunctions() -> dict:
        """
        returns all functions implemented in the UDPPFunctionCollection.py using the inspect function for live reflection

        :returns: implemented functions as dict with function name as key
        :rtype: dict
        """
        method_list: [str] = [func for func in dir(UDPPFunctionCollection) if callable(getattr(UDPPFunctionCollection, func)) and not func.startswith("__")]

        resultdict: dict = {}

        for method in method_list:
            # get function object by name:string
            function_obj = getattr(UDPPFunctionCollection, method)

            inspect_result: inspect.FullArgSpec = inspect.getfullargspec(function_obj)
            # get signature # todo merge with inspect.getfullargspec
            signature = inspect.signature(function_obj)

            # EXTRACT FUNCTION PARAMETER TYPES
            return_type: str = None
            parameter_types = {}
            for k in inspect_result.annotations:
                v = inspect_result.annotations[k]

                if k == 'return':
                    return_type = UDPPFunctionTranslator.strip_function_parameter_types(str(v))
                else:
                    parameter_types[k] = UDPPFunctionTranslator.strip_function_parameter_types(str(v))

            # TODO FIX USING def
            defaults: dict = {}

            for k, v in signature.parameters.items():
                if v.default is not inspect.Parameter.empty:
                    defaults[k] = str(v.default)

            resultdict[method] = {
                'name': method,
                'parameter_names': inspect_result.args,
                'parameter_types': parameter_types,
                'default': defaults,
                'return': return_type
            }

        return resultdict
