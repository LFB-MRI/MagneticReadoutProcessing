from typing import Annotated
import typer
import cli_helper
import cli_datastorage
import  MRPHal

app = typer.Typer()




@app.command()
def run(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = "", ignoreinvalid: Annotated[bool, typer.Argument()] = True):

    configs:[str] = []
    if configname is not None and len(configname) > 0:
        configs.append(configname.replace('_config', '').replace('.json', ''))
    else:
        configs = cli_datastorage.CLIDatastorage.list_configs()


    print("STARTING MEASUREMENT RUN WITH FOLLOWING CONFIGS: {}".format(configs))

    cfg_to_run: [str] = []
    for c in configs:

        cfg = cli_datastorage.CLIDatastorage(c)
        print("PRERUN CHECK FOR {} [{}]".format(c, cfg.config_filepath()))


        # check config valid

        # check sensor connection

        print("> sensor-connection-test".format())
        conn: MRPHal = cli_helper.connect_sensor_using_config(c)

        if not ignoreinvalid and not conn.is_connected():
            print("precheckfail: sensor connection failed - please run config setupsensor again or check connection")
            raise typer.Abort("precheckfail: sensor connection failed - please run config setupsensor again or check connection")

        print("> sensor-connection-test: OK".format(conn.get_sensor_id()))
        
        conn.disconnect()



        cfg_to_run.append(c)




@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    ctx.obj = cli_datastorage.Common()






if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()