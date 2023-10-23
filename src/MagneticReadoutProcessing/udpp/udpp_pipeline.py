"""Typer base cli interface to allow the user to interact with the udppf system"""

import os
from pathlib import Path
from typing import Annotated
import typer
from UDPPFunctionTranslator import UDPPFunctionTranslator
import networkx as nx
import matplotlib.pyplot as plt
import udpp_config
app = typer.Typer()




@app.command(help="lists all available functions for pipeline programming ")
def listfunctions(ctx: typer.Context):
    print(UDPPFunctionTranslator.listfunctions())

@app.command(help="list all found pipelines in pipelines folder")
def listenabledpipelines(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(udpp_config.PIPELINES_FOLDER)
    for k in pipelines:
        print(k)


@app.command()
def run(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(udpp_config.PIPELINES_FOLDER)


    # ITERATE OVER EACH PIPELINE
    for pipeline_k, pipeline_v in pipelines.items():
        # CREATE TEMP FOLDER FOR PIPELINE to store some intermediate results
        pipeline_temp_folder_name: str = str(pipeline_k).replace('.', '_').replace('/', '')
        pipeline_temp_folder_path: str = str(Path(udpp_config.TMP_FOLDER).joinpath("{}/".format(pipeline_temp_folder_name)))

        Path().mkdir(parents=True, exist_ok=True)



        # EXTRACT SETTINGS
        settings: dict = pipeline_v['settings']
        # EXTRACT STEPS
        # also checks duplicate pipeline steps
        steps = UDPPFunctionTranslator.extract_pipelines_steps(pipeline_v)
        print("found following valid steps: {}".format(steps))



        # CREATE CALLTREE
        calltree_graph: nx.DiGraph = UDPPFunctionTranslator.create_calltree_graph(steps, pipeline_temp_folder_path)
        print("calltree generated: {}".format(calltree_graph))

        # CHECK FOR EXISTING FUNCTIONS
        # RAISES AN EXCEPTION IF SOMETHING IS WRONG
        UDPPFunctionTranslator.check_functions_exists(steps)


        # CHECK FOR MATCHING FUNCTION PARAMETERS
        # => raises exception is a parameter is wring
        UDPPFunctionTranslator.check_parameter_types(steps, calltree_graph)


        # get all possible start nodes
        # => with no input parameters from other steps
        startsteps: [str] = UDPPFunctionTranslator.get_startsteps(steps)
        if startsteps is None or len(startsteps) <= 0:
            raise Exception("get_startsteps: no start stages found so cant execute pipeline due missing start stage")
        print("found startsteps: {}".format(startsteps))

        # GENERATE SUBCALLTREES
        # which includes the right computation order for each function
        sub_call_trees: [nx.DiGraph] = UDPPFunctionTranslator.create_sub_calltrees(steps, calltree_graph, startsteps, pipeline_temp_folder_path)
        # traverse calltree to get queue of processing


        # PREPARE INTERMEDIATE RESULT DICT
        # THIS STORES ALL INTERMEDIATE RESULTS DURING COMPUTATION OF THE SUB CALL-TREES
        intermediate_results: dict = {}

        for subcalltree in sub_call_trees:
            for node in subcalltree.nodes:
                intermediate_results[str(node)] = None


        # OPTION TO EXPORT THE EXPORT A SNAPSHOT OF THE CURRENT COMPUTED READING AFTER EACH STEP
        export_intermediate_results: bool = False
        if 'export_intermediate_results' in settings and settings['export_intermediate_results']:
            export_intermediate_results = True


        # TODO
        #subcalltree: nx.DiGraph.
        for subcalltree in sub_call_trees:
            # ITERATE OVER ALL CONNECTED STAGES PRESENT IN THE SUCCESSOR FIELD
            # ALTERNATIVE IS TO USE:
            # ALLE NODES WITH INGRAD 0 AND OUTGRAD > 0
            # ALL REMAINING NODES WITH INGRAD > 0
            for successor in subcalltree.succ:
                stage_name: str = successor
                print("processing:{}".format(stage_name))
                if stage_name not in steps:
                    raise Exception("{} no present in current steps".format(stage_name))
                stage_information: dict = steps[stage_name]
                stage_function_name: str = stage_information['function']

                UDPPFunctionTranslator.get_function(stage_function_name)
                function_parameters_from_stages = UDPPFunctionTranslator.get_function_parameters(stage_function_name)
                function_parameters_from_inspector:[dict] = UDPPFunctionTranslator.get_function_parameters(stage_function_name, _get_inspector_parameter=True)
                # POPULATE PARAMETER DICT
                parameters: dict = {}


                ## PROCESS PARAMETERS FROM FROM OTHER STAGES
                for otpentry in function_parameters_from_stages:
                    pass
                ## PROCESS INSPECTOR PARAMETER
                for ip_entry in function_parameters_from_inspector:
                    name: str = ip_entry['id']
                    type: str = ip_entry['type']

                    # TODO COMPLEX TYPES as json objects ?

                    value = None
                    # ASSIGN DEFAULT VALUE
                    if 'value' in ip_entry:
                        _value = ip_entry['value']
                        if len(_value) > 0:
                            value = _value


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
                intermediate_results[str(stage_name)] = UDPPFunctionTranslator.execute_function_by_name(stage_function_name, parameters)

                i = 0



            # FOR EACH NODE DFS STARTING AT STARTNODE
            
            # READ INPUT PARAMETER FROM YAML IF STAT OR FROM INTERTMEDIATE DICT

            # if parameters required use **parameters dict
            parameters = {}

            # EXECUTE FUNCTION

            # SAVE IN DICT

            # EXPORT IF SET export_intermediate_results

        # SAVE RESULT IN DICT


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    Path(udpp_config.PIPELINES_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(udpp_config.TMP_FOLDER).mkdir(parents=True, exist_ok=True)






if __name__ == "__main__":
    app()
