
from MRP import MRPHal, MRPReading, MRPReadingSource, MRPBaseSensor, MRPReadingEntry, MRPMeasurementConfig


class MRPReadingSourceFullsphereException(Exception):
    def __init__(self, message="MRPReadingSourceFullsphereException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPReadingSourceFullsphere(MRPReadingSource.MRPReadingSource):

    hal_instance: MRPHal.MRPHal = None

    # ALL GCODE COMMANDS WHICH ARE NEEDED BEFORE STARTING A MEASUREMENT
    MEASUREMENT_START_GCODE: [str] = [
        # SET SPEED LIMITS
        "SET_VELOCITY_LIMIT VELOCITY=10",
        "SET_VELOCITY_LIMIT ACCEL=5",
        "SET_VELOCITY_LIMIT ACCEL_TO_DECEL=5",
        "SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1"
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

        if not 'gcode' in _hal.get_sensor_commandlist():
            raise MRPReadingSourceFullsphereException("invalid commands: gcode command is not supported by this hal. is MRPHalKlipper present ? ")

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



        for s_idx in range(sensor.sensor_count):
            # CREATE MEASUREMENT CONFIG
            mmc: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()
            mmc.configure_fullsphere()
            mmc.id = self.hal_instance.get_sensor_id()
            mmc.sensor_id = s_idx
            # CREATE A READING WITH CREATED CONFIG
            reading: MRPReading.MRPReading = MRPReading.MRPReading(mmc)
            # SET READING NAME
            reading.set_name("ID{}_SID{}_MAG{}".format(  mmc.id, mmc.sensor_id, reading.get_magnet_type().name))



            # PERFORM READING FOR EACH USER SET DATAPOINT
            # LOOP OVER ALL DATAPOINTS
            print("sampling {} datapoints with {} average readings".format(_measurement_points, _average_readings_per_datapoint))
            for dp_idx in range(_measurement_points):
                avg_temp: float = 0.0
                avg_bf: float = 0.0
                # CALCULATE AVERAGE
                for avg_idx in range(_average_readings_per_datapoint):
                    # READOUT SENSOR
                    sensor.query_readout()
                    avg_temp = avg_temp + sensor.get_temp(_sensor_id=s_idx)
                    avg_bf = avg_bf + sensor.get_b(_sensor_id=s_idx)

                avg_temp = avg_temp / _average_readings_per_datapoint
                avg_bf = avg_bf / _average_readings_per_datapoint

                # APPEND READING
                print("SID{} DP{} B{} TEMP{}".format(s_idx, dp_idx, avg_bf, avg_temp))
                rentry: MRPReadingEntry.MRPReadingEntry = MRPReadingEntry.MRPReadingEntry(p_id=dp_idx, p_value=avg_bf, p_temperature=avg_temp, p_is_valid=True)
                reading.insert_reading_instance(rentry, _autoupdate_measurement_config=False)


            result_readings.append(reading)


        return result_readings

