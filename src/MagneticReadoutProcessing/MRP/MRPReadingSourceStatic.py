from MRP import MRPHal, MRPReading, MRPReadingSource, MRPBaseSensor, MRPMeasurementConfig, MRPReadingEntry


class MRPReadingSourceStaticException(Exception):
    def __init__(self, message="MRPReadingSourceStaticException thrown"):
        self.message = message
        super().__init__(self.message)


class MRPReadingSourceStatic(MRPReadingSource.MRPReadingSource):


    @staticmethod
    def get_base_sensor_reading(_sensor: MRPBaseSensor.MRPBaseSensor, _reading: MRPReading.MRPReading, _average_readings_per_datapoint: int) -> [MRPReadingEntry.MRPReadingEntry]:
        index: int = len(_reading.data) + 1
        print("sampling {} datapoints with {} average readings".format(index,_average_readings_per_datapoint))
        ret: [MRPReadingEntry.MRPReadingEntry] = []
        for s_idx in range(_sensor.sensor_count):

            avg_temp: float = 0.0
            avg_bf: float = 0.0
            # CALCULATE AVERAGE
            for avg_idx in range(_average_readings_per_datapoint):
                # READOUT SENSOR
                _sensor.query_readout()
                avg_temp = avg_temp + _sensor.get_temp(_sensor_id=s_idx)
                avg_bf = avg_bf + _sensor.get_b(_sensor_id=s_idx)

            avg_temp = avg_temp / _average_readings_per_datapoint
            avg_bf = avg_bf / _average_readings_per_datapoint

            # APPEND READING
            print("SID{} DP{} B{} TEMP{}".format(s_idx, index, avg_bf, avg_temp))
            rentry: MRPReadingEntry.MRPReadingEntry = MRPReadingEntry.MRPReadingEntry(p_id=index, p_value=avg_bf,
                                                                                      p_temperature=avg_temp,
                                                                                      p_is_valid=True)
            ret.append(rentry)
        return ret



    hal_instance: MRPHal.MRPHal = None
    def __init__(self, _hal: MRPHal.MRPHal):
        if not _hal.is_connected():
            _hal.connect()

        if not 'static' in _hal.get_sensor_capabilities():
            raise MRPReadingSourceStaticException("invalid get_sensor_capabilities for this reading source static is required")

        self.hal_instance = _hal



    def __del__(self):
        if self.hal_instance:
            self.hal_instance.disconnect()

    def perform_measurement(self, _measurement_points: int, _average_readings_per_datapoint: int) -> [MRPReading.MRPReading]:
        if not self.hal_instance.is_connected():
            self.hal_instance.connect()

        sensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(self.hal_instance)
        result_readings: [MRPReading.MRPReading] = []

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
            rentry: [MRPReadingEntry.MRPReadingEntry] = MRPReadingSourceStatic.get_base_sensor_reading(sensor, result_readings[m_idx], _average_readings_per_datapoint)

            for idx, _ in enumerate(result_readings):
                result_readings[idx].insert_reading_instance(rentry[idx], _autoupdate_measurement_config=False)


        return result_readings

