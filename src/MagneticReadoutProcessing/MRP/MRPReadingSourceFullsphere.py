
from MRP import MRPHal, MRPReading, MRPReadingSource, MRPBaseSensor, MRPReadingEntry, MRPMeasurementConfig, \
    MRPReadingSourceStatic


class MRPReadingSourceFullsphereException(Exception):
    def __init__(self, message="MRPReadingSourceFullsphereException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPReadingSourceFullsphere(MRPReadingSource.MRPReadingSource):

    hal_instance: MRPHal.MRPHal = None

    # GOCDES TO RUN TO INIT THE SYSTEM
    MEASUREMENT_INIT_GCODE: [str] = [
        # LOG FIRMWARE VERSION
        "M115",
        # SET SPEED LIMITS
        "SET_VELOCITY_LIMIT VELOCITY=10",
        "SET_VELOCITY_LIMIT ACCEL=5",
        "SET_VELOCITY_LIMIT ACCEL_TO_DECEL=5",
        "SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1",
        # HOME
        "G28 Y",
        # DISABLE MOTORS AGAIN
        "M84",

    ]
    # ALL GCODE COMMANDS WHICH ARE NEEDED BEFORE STARTING A MEASUREMENT
    MEASUREMENT_START_GCODE: [str] = [
        # HOME MECHANIC
        "G28 Y"
    ]

    MEASUREMENTS_END_GCODE: [str] = [
        # HOME AGAIN
        "G28 Y",
        # DISABLE MOTORS
        "M84"
    ]

    MEASUREMENT_CONFIG: dict = {
        "MAX_THETA_MECHANIC": 78.0,
        "MAX_PHI_MECHANIC": 10,
        "MOVE_MECHANIC_GCODE": "G1 Y{theta:.2f} F10"
    }





    def __init__(self, _hal: MRPHal.MRPHal):
        if not _hal.is_connected():
            _hal.connect()

        if not 'static' in _hal.get_sensor_capabilities() or not 'fullsphere' in _hal.get_sensor_capabilities():
            raise MRPReadingSourceFullsphereException("invalid get_sensor_capabilities for this reading source static and fullsphere is required")

        cmdlist: [str] = _hal.get_sensor_commandlist()
        if not 'gcode' in cmdlist:
            raise MRPReadingSourceFullsphereException("invalid commands: gcode command is not supported by this hal. is MRPHalKlipper present ? got: {} ".format(cmdlist))

        # TEST CONNECTION
        for cmd in self.MEASUREMENT_INIT_GCODE:
            _hal.query_command_str("gcode {}".format(cmd))
        self.hal_instance = _hal

    def __del__(self):
        if self.hal_instance:
            self.hal_instance.disconnect()

    def perform_measurement(self, _measurement_points: int, _average_readings_per_datapoint: int) -> [MRPReading.MRPReading]:
        if not self.hal_instance.is_connected():
            self.hal_instance.connect()

        sensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(self.hal_instance)
        result_readings: [MRPReading.MRPReading] = []


        # PREPRRE MECHANIC FOR MEASUREMENT
        for cmd in self.MEASUREMENT_START_GCODE:
            self.hal_instance.query_command_str("gcode {}".format(cmd))


        for s_idx in range(_measurement_points):
            # CREATE MEASUREMENT CONFIG
            mmc: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()
            mmc.configure_fullsphere()
            mmc.id = self.hal_instance.get_sensor_id()
            mmc.sensor_id = s_idx
            # CREATE A READING WITH CREATED CONFIG
            reading: MRPReading.MRPReading = MRPReading.MRPReading(mmc)
            # SET READING NAME
            reading.set_name("ID{}_SID{}_MAG{}".format(  mmc.id, mmc.sensor_id, reading.get_magnet_type().name))
            result_readings.append(reading)




        for m_idx in range(_measurement_points):
            # PERFORM READING FOR EACH USER SET DATAPOINT
            # LOOP OVER ALL DATAPOINTS
            rentry: [MRPReadingEntry.MRPReadingEntry] = MRPReadingSourceStatic.MRPReadingSourceStatic.get_base_sensor_reading(sensor, result_readings[m_idx], _average_readings_per_datapoint)

            for idx, _ in enumerate(result_readings):
                result_readings[idx].insert_reading_instance(rentry[idx], _autoupdate_measurement_config=False)

        # RESET MECHANIC AFTER MEASUREMENT
        for cmd in self.MEASUREMENTS_END_GCODE:
            self.hal_instance.query_command_str("gcode {}".format(cmd))

        return result_readings

