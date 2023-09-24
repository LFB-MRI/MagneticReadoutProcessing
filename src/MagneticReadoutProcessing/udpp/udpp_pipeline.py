import os
from pathlib import Path
from typing import Annotated
import typer
from UDPPFunctionTranslator import UDPPFunctionTranslator
import networkx as nx


app = typer.Typer()

PIPELINES_FOLDER = str(Path(str(os.path.dirname(__file__))).parent.joinpath("pipelines"))

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
        # EXTRACT SETTINGS
        settings: dict = pipeline_v['settings']
        # EXTRACT STEPS
        # also checks duplicate pipeline steps
        steps = UDPPFunctionTranslator.extract_pipelines_steps(pipeline_v)
        print("found following valid steps: {}".format(steps))

        calltree_graph:nx.Graph = UDPPFunctionTranslator.create_calltree_graph(steps)
        print("calltree generated: {}".format(calltree_graph))

         # get all possible start nodes
        startsteps = UDPPFunctionTranslator.get_startsteps(steps)
        print("found startstesp: {}".format(startsteps))
        # => with no input parameters from other steps

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
    pass






if __name__ == "__main__":
    app()
