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




@app.command()
def listfunctions(ctx: typer.Context):
    print(UDPPFunctionTranslator.listfunctions())

@app.command()
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
        for subcalltree in sub_call_trees:
            pass
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
