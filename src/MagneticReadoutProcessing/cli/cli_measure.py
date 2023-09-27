import os
from pathlib import Path
from typing import Annotated
import typer
import cli_helper
import cli_datastorage

from import_MRP import __fix_import__
__fix_import__()
from MRP import  MRPHal, MRPReading, MRPMeasurementConfig, MRPMagnetTypes, MRPReadingEntry, MRPReadingEntry, MRPBaseSensor

app = typer.Typer()



def perform_measurement(configname: str):
    print("perform_measurement for {}".format(configname))
    cfg: cli_datastorage.CLIDatastorage = cli_datastorage.CLIDatastorage(configname)
    hal: MRPHal.MRPPHal = cli_helper.connect_sensor_using_config(_configname=configname)
    sensor_count = hal.get_sensor_count()


    # SENSOR SETUP
    sensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(hal)



    for idxsen in range(sensor_count):
        # CREATE A MEASUREMENT CONFIG
        mmc: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()

        # TODO REMOVE
        mmc.configure_fullsphere()

        mmc.id = hal.get_sensor_id()
        mmc.sensor_id = idxsen
        # CREATE A READING WITH CONDIG
        reading: MRPReading.MRPReading = MRPReading.MRPReading(mmc)



        mag = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_MAGNET_TYPE)
        # SET MAGNET TYPE
        if len(mag) > 0 and MRPMagnetTypes.MagnetType.from_int(int(mag)) is not MRPMagnetTypes.MagnetType.NOT_SPECIFIED:
            reading.set_magnet_type(MRPMagnetTypes.MagnetType.from_int(int(mag)))
        else:
            reading.set_magnet_type(MRPMagnetTypes.MagnetType.NOT_SPECIFIED)

        # ADD THE MEASUREMENT CONFIGURATION
        for kv in cli_datastorage.CLIDatastorageEntries:
            k = kv.name
            v = cfg.get_value(kv)
            reading.set_additional_data(str(k), str(v))

        # ADD MORE METADATA
        reading.set_additional_data('configname', configname)
        reading.set_additional_data('runner', 'cli')
        reading.set_additional_data('sensor_capabilities', str(hal.get_sensor_capabilities()))

        # SET THE NAME
        reading.set_name("{}_ID{}_SID{}_MAG{}".format(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX), mmc.id, mmc.sensor_id, reading.get_magnet_type().name))

        # ADD METADATA ABOUT THE SENSOR
        max_datapoints = int(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT))
        max_avg = int(cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT))
        # LOOP OVER ALL DATAPOINTS
        print("sampling {} datapoints with {} average readings".format(max_datapoints, max_avg))
        for dp_idx in range(max_datapoints):
            avg_temp: float = 0.0
            avg_bf: float = 0.0
            # CALCULATE AVERAGE
            for avg_idx in range(max_avg):
                # READOUT SENSOR
                sensor.query_readout()
                avg_temp = avg_temp + sensor.get_temp(_sensor_id=idxsen)
                avg_bf = avg_bf + sensor.get_b(_sensor_id=idxsen)

            avg_temp = avg_temp / max_avg
            avg_bf = avg_bf / max_avg

            # APPEND READING
            print("SID{} DP{} B{} TEMP{}".format(idxsen, dp_idx, avg_bf, avg_temp))
            rentry: MRPReadingEntry.MRPReadingEntry = MRPReadingEntry.MRPReadingEntry(p_id=dp_idx, p_value=avg_bf, p_temperature=avg_temp, p_is_valid=True)
            reading.insert_reading_instance(rentry, _autoupdate_measurement_config=False)

            # EXPORT TO FILESYSTEM
            filename = (reading.get_name() + "_cIDX{}".format(dp_idx)).replace('/', '').replace('.', '')
            target_folder = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
            # RESOLVE REL TO ABS PATH
            if not str(target_folder).startswith('/'):
                target_folder = str(Path(target_folder).resolve())
            # CREATE COMPLETE PATH WITH FILENAME
            complete_path = os.sep.join([target_folder, filename])
            # EXPORT
            print("exported reading: ".format(reading.dump_to_file(complete_path)))



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
    app()