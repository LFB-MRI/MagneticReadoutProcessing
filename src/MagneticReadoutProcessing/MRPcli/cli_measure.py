import os
from pathlib import Path
from typing import Annotated, List
import typer
from MRPcli import cli_helper
from MRPcli import cli_datastorage


from MRP import MRPHal, MRPReading, MRPMeasurementConfig, MRPMagnetTypes, MRPReadingEntry, MRPReadingEntry, MRPBaseSensor, MRPReadingSourceHelper, MRPReadingSource

app = typer.Typer()

def perform_measurement_rotationalsensor(configname: str):
    pass

def perform_measurement(configname: str, alternativefilename: str = "", generate_plots: bool =  False):
    print("perform_measurement for {}".format(configname))
    cfg: cli_datastorage.CLIDatastorage = cli_datastorage.CLIDatastorage(configname)

    # CREATE HAL INSTANCE
    hal: MRPHal.MRPPHal = cli_helper.create_hal_instance_using_config(_configname=configname)

    # CREATE READING SOURCE INSTANCE USING HAL
    # IT MANAGES THE AUTOMATIC SENSOR DETECTION
    reading_source: MRPReadingSource.MRPReadingSource = MRPReadingSourceHelper.MRPReadingSourceHelper.createReadingSourceInstance(hal)

    READING_AVERAGE_COUNT: int = int(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT))
    READING_DATAPOINT_COUNT: int = int(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT))


    result_readings: [MRPReading.MRPReading] = reading_source.perform_measurement(READING_DATAPOINT_COUNT, READING_AVERAGE_COUNT)


    for idx, r in enumerate(result_readings):

        # ADD METADATA
        for kv in cli_datastorage.CLIDatastorageEntries:
            k = kv.name
            v = cfg.get_value(kv)
            r.set_additional_data(str(k), str(v))
        r.set_additional_data('configname', configname)
        r.set_additional_data('runner', 'MRPcli')

        # SET MAGNET TYPE
        mag = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_MAGNET_TYPE)
        # SET MAGNET TYPE
        if len(mag) > 0 and MRPMagnetTypes.MagnetType.from_int(int(mag)) is not MRPMagnetTypes.MagnetType.NOT_SPECIFIED:
            r.set_magnet_type(MRPMagnetTypes.MagnetType.from_int(int(mag)))
        else:
            r.set_magnet_type(MRPMagnetTypes.MagnetType.NOT_SPECIFIED)


        # MODIFY NAME

        name: str = r.get_name()

        if alternativefilename is not None and len(alternativefilename):
            name = alternativefilename
        else:
            name = "{}_{}_{}".format(configname, cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX), name)
        r.set_name(name)

        # EXPORT READING TO FILESYSTEM
        filename = (r.get_name() + "_cIDX{}".format(idx)).strip('/').strip('.')
        target_folder = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
        # RESOLVE REL TO ABS PATH

        if not str(target_folder).startswith('/'):
            target_folder = str(Path(cli_datastorage.CLIDatastorageConfig.get_basepath()).joinpath(Path(target_folder).resolve()))
        print("target_folder: {}".format(target_folder))
        # CREATE COMPLETE PATH WITH FILENAME
        complete_path = os.sep.join([target_folder, filename])
        # EXPORT
        print("exported reading: ".format(r.dump_to_file(complete_path)))


    # GENERATE VISUALISATION GRAPHICS
    if generate_plots:
        visu_name = "{}_{}".format(configname, cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX))
        visu_target_folder = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
        if not str(visu_target_folder).startswith('/'):
            visu_target_folder = str(Path(visu_target_folder).resolve())
        visu_exp_path: str = os.sep.join([visu_target_folder, visu_name])
        reading_source.export_visualisation(result_readings, visu_exp_path)









@app.command()
def run(ctx: typer.Context, configname: Annotated[str, typer.Argument()] = "", alternativefilename: str = "", generate_plots: bool = False, ignoreinvalid: bool = False, ignoremeasurementerror: bool = True):

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
        # CREATE FOLDER IF NEEDED
        if not os.path.exists(c):
            if not str(c).startswith('/'):
                c = str(Path(c).resolve())
                Path(c).mkdir(parents=True, exist_ok=True)


        print("> config-test: OK".format())


        # check sensor connection
        conn: MRPHal.MRPHal = cli_helper.create_hal_instance_using_config(_configname=cfgname)
        if not ignoreinvalid and not conn.is_connected():
            print("precheckfail: sensor connection failed - please run config setupsensor again or check connection")
            raise typer.Abort("precheckfail: sensor connection failed - please run config setupsensor again or check connection")
        print("> sensor-connection-test: OK".format(conn.get_sensor_id()))

        cfg_to_run.append(c)
        conn.disconnect()


    print("START MEASUREMENT CYCLE".format())
    for cfg in cfg_to_run:
        try:
            perform_measurement(configname, alternativefilename, generate_plots)
        except Exception as e:
            print(e)
            if not ignoremeasurementerror:
                raise typer.Abort(e)





@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    app()