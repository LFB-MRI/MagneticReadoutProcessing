"""Typer base MRPcli interface to allow the user to interact with the udppf system"""

from pathlib import Path
import typer
from MRPudpp.UDPPFunctionTranslator import UDPPFunctionTranslator
import networkx as nx
from MRPudpp import udpp_config
import pickle

app = typer.Typer()




@app.command(help="lists all available functions for pipeline programming in json notation")
def listfunctionsjson(ctx: typer.Context):
    print(UDPPFunctionTranslator.listfunctions())

@app.command(help="lists all available functions for pipeline programming ")
def listfunctions(ctx: typer.Context):
    print("\n".join(list(UDPPFunctionTranslator.listfunctions().keys())))

@app.command(help="list all found pipelines in pipelines folder")
def listenabledpipelines(ctx: typer.Context):
    print("PIPELINE STORAGE FOLDER: {}".format(udpp_config.UDPPConfig.get_pipeline_folder()))

    pipelines = UDPPFunctionTranslator.load_pipelines(udpp_config.UDPPConfig.get_pipeline_folder(), _log=False)
    for k in pipelines:
        print("> {}".format(k))


@app.command(help="get current pipelines folder path")
def currentpipelinefolder(ctx: typer.Context):
    print("{}".format(udpp_config.UDPPConfig.get_pipeline_folder()))


@app.command()
def run(ctx: typer.Context):
    pipelines = UDPPFunctionTranslator.load_pipelines(udpp_config.UDPPConfig.get_pipeline_folder())


    # ITERATE OVER EACH PIPELINE
    for pipeline_k, pipeline_v in pipelines.items():
        # CREATE TEMP FOLDER FOR PIPELINE to store some intermediate results
        pipeline_temp_folder_name: str = str(pipeline_k).replace('.', '_').replace('/', '')
        pipeline_temp_folder_path: str = str(Path(udpp_config.UDPPConfig.get_tmp_folder()).joinpath("{}/".format(pipeline_temp_folder_name)))

        Path().mkdir(parents=True, exist_ok=True)



        # EXTRACT SETTINGS
        settings: dict = pipeline_v['settings']

        # CHECK IF PIPELINE ENABLED
        if 'enabled' in settings and not settings['enabled']:
            print("skipping pipeline {} => enabled is set to False or key is missing".format(settings['name']))
            continue
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




        # OPTION TO EXPORT THE EXPORT A SNAPSHOT OF THE CURRENT COMPUTED READING AFTER EACH STEP
        export_intermediate_results: bool = False
        if 'export_intermediate_results' in settings and settings['export_intermediate_results']:
            export_intermediate_results = True



        # EXECUTE STARTSTEPS FIRST
        # THIS ACCELERATES THE PROCESSING LASTER ON
        for st in startsteps:
            print("=====> {} {} ".format(st, st))
            stage_information: dict = steps[st]
            fkt_call_result = UDPPFunctionTranslator.execute_stage_funktion(stage_information, intermediate_results)

            if fkt_call_result is not None:
                print("warning result value of stage {} is None".format(st))
            intermediate_results[st] = fkt_call_result


        for subcalltree in sub_call_trees:

            if subcalltree.nodes is not None and len(subcalltree.nodes) == 1:
                if list(subcalltree.nodes)[0] in startsteps:
                    continue

            # ITERATE OVER ALL CONNECTED STAGES PRESENT IN THE SUCCESSOR FIELD
            # ALTERNATIVE IS TO USE:
            # ALLE NODES WITH INGRAD 0 AND OUTGRAD > 0
            # ALL REMAINING NODES WITH INGRAD > 0
            last_successor = None

            n = None
            for successor in subcalltree.succ:
                n = successor
                break
            dfs_res: [str] = list(nx.dfs_tree(subcalltree, n))


            for stage_name in dfs_res:


                if stage_name not in steps:
                    raise Exception("{} no present in current steps".format(stage_name))

                if stage_name in intermediate_results:
                    continue

                stage_information: dict = steps[stage_name]

                print("=====> execute stage {}".format(stage_name))

                fkt_call_result = UDPPFunctionTranslator.execute_stage_funktion(stage_information, intermediate_results)

                if fkt_call_result:
                    intermediate_results[str(stage_name)] = fkt_call_result

                print("end processing:{}".format(stage_name))

                if export_intermediate_results:
                    with open(str(Path(pipeline_temp_folder_path).joinpath(Path("intermediate_results_{}".format(str(stage_name))))), 'wb') as outp:  # Overwrites any existing file.
                        pickle.dump(intermediate_results, outp, pickle.HIGHEST_PROTOCOL)







@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    Path(udpp_config.UDPPConfig.get_pipeline_folder()).mkdir(parents=True, exist_ok=True)
    Path(udpp_config.UDPPConfig.get_tmp_folder()).mkdir(parents=True, exist_ok=True)



if __name__ == "__main__":
    app()
