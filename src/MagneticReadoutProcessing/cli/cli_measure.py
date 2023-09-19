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
    for cfgname in configs:

        cfg = cli_datastorage.CLIDatastorage(cfgname)
        print("PRERUN CHECK FOR {} [{}]".format(cfgname, cfg.config_filepath()))

        # check config valid
        c = int(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT))
        if c <= 0 and not ignoreinvalid:
            print("precheckfail: READING_DATAPOINT_COUNT <= 0")
            raise typer.Abort("precheckfail: READING_DATAPOINT_COUNT <= 0")

        c = int(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT))
        if c <= 0 and not ignoreinvalid:
            print("precheckfail: READING_AVERAGE_COUNT <= 0")
            raise typer.Abort("precheckfail: READING_AVERAGE_COUNT <= 0")

        c = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
        if len(c) <= 0 and not ignoreinvalid:
            print("precheckfail: READING_OUTPUT_FOLDER is invalid: {} ".format(c))
            raise typer.Abort("precheckfail: READING_OUTPUT_FOLDER is invalid: {} ".format(c))

        print("> config-test: OK".format())
        

        # check sensor connection
        conn: MRPHal = cli_helper.connect_sensor_using_config(_configname=cfgname)#cli_helper.connect_sensor_using_config(_configname=c)
        if not ignoreinvalid and not conn.is_connected():
            print("precheckfail: sensor connection failed - please run config setupsensor again or check connection")
            raise typer.Abort("precheckfail: sensor connection failed - please run config setupsensor again or check connection")
        print("> sensor-connection-test: OK".format(conn.get_sensor_id()))

        conn.disconnect()



        cfg_to_run.append(c)




@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()