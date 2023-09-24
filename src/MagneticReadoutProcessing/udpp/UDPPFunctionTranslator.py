import os
import queue
from pathlib import Path
import yaml
from queue import Queue
import networkx as nx
from matplotlib import pyplot as plt

from import_MRP import __fix_import__
__fix_import__()


import inspect
from optparse import OptionParser
from UDPPFFunctionCollection import UDPFFunctionCollection





class IterableQueue():
    def __init__(self,source_queue):
            self.source_queue = source_queue
    def __iter__(self):
        while True:
            try:
               yield self.source_queue.get_nowait()
            except queue.Empty:
               return



# (a, b, x='blah')

class UDPPFunctionTranslator():

    @staticmethod
    def get_parameter_from_step(_pipelines: dict, _step: str, _only_step_dependencies:bool = False) -> [str]:
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
    def plot_graph(graph: nx.DiGraph, _export_graph_plots: str = None, _filename: str = "graphplot" ,_title: str = "graph_plot"):
        nx.draw_planar(graph, with_labels=True)
        plt.title("{}".format(_title))
        if _export_graph_plots is not None and len(_export_graph_plots) > 0:
            _export_graph_plots = _export_graph_plots.replace("//", "/")
            plt.savefig(_export_graph_plots + "/{}".format(_filename), dpi=1200)
        else:
            plt.show()
        plt.close()



    @staticmethod
    def create_sub_calltrees(_pipelines: dict, calltree_graph:nx.DiGraph, _start_steps: [str], _export_graph_plots: str = None) -> [nx.DiGraph]:
        if _start_steps is None or len(_start_steps) <= 0:
            raise Exception("create_sub_calltrees: _start_steps parameter empty or has no start steps")

        subgraphs: [nx.Graph] = []
        visited: dict = {}

        for i in calltree_graph.nodes:
            visited[i] = False
        # CREATE A SUBGRAPHS UNTIL A NODE WITH TWO STAGE INPUTS IS RANGED FROM THE START STEP
        next_nodes_after_startnodes: [str] = []
        # A QUEUE IS NEEDED TO FIRST PROCESS THE START STAGES AND THEN GOING FURTHER AND FURTHER THE OTHER STAGES ALONG
        nodes_to_process: queue.Queue = queue.Queue()
        for i in _start_steps:
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


            dfs_res: [str] = list(nx.dfs_tree(calltree_graph, ss))
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



                    if dfs_step not in next_nodes_after_startnodes:
                        print("added {} to next after startnodes".format(dfs_step))
                        nodes_to_process.put(dfs_step)
                        #next_nodes_after_startnodes.append(dfs_step)
                        break

                else:

                    # ADD NODES TO SUBGRAPH IF NOT PRESENT
                    if last_node not in list(subgraph.nodes):
                        subgraph.add_node(last_node)

                    if dfs_step not in list(subgraph.nodes):
                        subgraph.add_node(dfs_step)

                    # ADD EDGE
                    subgraph.add_edge(last_node, dfs_step)

                    last_node = dfs_step  # store last node

                    visited[dfs_step] = True

            # ADD AS NEW SUBGRAPH
            subgraphs.append(subgraph)
            print("subgraph {} with {}".format(len(subgraphs), list(nx.dfs_tree(subgraph, ss))))
            # EXPORT SUBGRAPH AS IMAGE
            UDPPFunctionTranslator.plot_graph(subgraph,_export_graph_plots, "sub_calltree_startstage_{}".format(ss), "SubCallTree for Start-Stages {}".format(ss))


        # AFTER ITERATING OVER THE START NODES
        # PROCESS THE UNVISITED NODES USNG A DFS
        # TODO REWORK




        return subgraphs

    @staticmethod
    def create_calltree_graph(_pipelines: dict, _export_graph_plots: str = None) -> nx.DiGraph:
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
                param_value:str = str(param_v)
                if 'stage ' in param_value:
                    param_value:str = param_value.replace('stage ', '')
                    if param_value in _pipelines:
                        # add edges from function using this parameter to function
                        calltree.add_edge(param_value, p_k)

        # find circles in the graph
        # to avoid processing endless loops
        try:
            circle_edges = nx.find_cycle(calltree, orientation="original") # original = follow edge -> !
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

    



