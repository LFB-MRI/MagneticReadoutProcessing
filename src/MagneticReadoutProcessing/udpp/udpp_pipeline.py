import os
from pathlib import Path
from typing import Annotated
import typer
from UDPPFunctionTranslator import UDPPFunctionTranslator
import networkx as nx
import matplotlib.pyplot as plt

app = typer.Typer()

PIPELINES_FOLDER = str(Path(str(os.path.dirname(__file__))).parent.joinpath("pipelines"))
TMP_FOLDER = str(Path(PIPELINES_FOLDER).joinpath("generated/"))


@app.command()
def listfunctions(ctx: typer.Context):
    print(UDPPFunctionTranslator.listfunctions())

@app.command()
def listenabledpipelines(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(PIPELINES_FOLDER)
    for k in pipelines:
        print(k)


@app.command()
def run(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(PIPELINES_FOLDER)


    # ITERATE OVER EACH PIPELINE
    for pipeline_k, pipeline_v in pipelines.items():
        # CREATE TEMP FOLDER FOR PIPELINE to store some intermediate results
        pipeline_temp_folder_name: str = str(pipeline_k).replace('.', '_').replace('/', '')
        pipeline_temp_folder_path: str = str(Path(TMP_FOLDER).joinpath("{}/".format(pipeline_temp_folder_name)))

        Path().mkdir(parents=True, exist_ok=True)



        # EXTRACT SETTINGS
        settings: dict = pipeline_v['settings']
        # EXTRACT STEPS
        # also checks duplicate pipeline steps
        steps = UDPPFunctionTranslator.extract_pipelines_steps(pipeline_v)
        print("found following valid steps: {}".format(steps))

        calltree_graph:nx.DiGraph = UDPPFunctionTranslator.create_calltree_graph(steps, pipeline_temp_folder_path)
        print("calltree generated: {}".format(calltree_graph))

        # get all possible start nodes
        # => with no input parameters from other steps
        startsteps = UDPPFunctionTranslator.get_startsteps(steps)
        print("found startstesp: {}".format(startsteps))

        # traverse
        sct = UDPPFunctionTranslator.create_sub_calltrees(steps, calltree_graph, startsteps, pipeline_temp_folder_path)
        # traverse calltree to get queue of processing

        #start_step: str = UDPPFunctionTranslator.get_startstep(_pipelines)
        #if start_step is None:
        #    raise Exception("create_calltree: no start stage found")

        #traversed = nx.edge_bfs(calltree, start_step, 'original')
        #for e in traversed:
        #    print(e)
        #return traversed
        # CHECK INPUT OUTPUT PARAMETER TYPES

        # EXECUTE ALL STAGES WITH no iNPUT FROM OTHER STAGES
        # SAVE RESULT IN DICT


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    Path(PIPELINES_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(TMP_FOLDER).mkdir(parents=True, exist_ok=True)






if __name__ == "__main__":
    app()
