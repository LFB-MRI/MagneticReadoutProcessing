import os
from typing import Annotated
import typer
import cli_helper
import cli_datastorage
import  MRPHal
import MRPReading
import MRPMeasurementConfig

app = typer.Typer()



def perform_measurement(configname: str):
    print("perform_measurement for".format(configname))
    cfg: cli_datastorage.CLIDatastorage = cli_datastorage.CLIDatastorage(configname)
    hal: MRPHal.MRPPHal = cli_helper.connect_sensor_using_config(_configname=configname)
    sensor_count = hal.get_sensor_count()



    for idxsen in range(sensor_count):
        # CREATE A MEASUREMENT CONFIG
        mmc: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()
        mmc.id = hal.get_sensor_id()

        mmc.sensor_id = idxsen
        #mmc.magnet_type =


        reading: MRPReading.MRPReading = MRPReading.MRPReading(mmc)

        for entry in cli_datastorage.CLIDatastorageEntries.READING_PREFIX:
            k =
            v = cfg.get_value(entry)
            reading.set_magnet_type(str(k), str(v))
        # ADD ALl
        reading.additional_data()
        reading.set_name("{}_ID{}_SID{}_MAG{}".format(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX), mmc.id, mmc.sensor_id, reading.get_magnet_type().name))




@app.command()
def run(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = "", ignoreinvalid: Annotated[bool, typer.Argument()] = False, ignoremeasurementerror: Annotated[bool, typer.Argument()] = True):

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
        if len(c) <= 0 and not os.path.isdir(c) and not ignoreinvalid:
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



    print("START MEASUREMENT CYCLE".format())
    for cfg in cfg_to_run:
        try:
            perform_measurement(configname)
        except Exception as e:
            print(e)
            if not ignoremeasurementerror:
                raise typer.Abort(e)





@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()