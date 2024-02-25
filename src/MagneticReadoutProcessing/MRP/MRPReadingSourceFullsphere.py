import math
import os
import time

import numpy as np

from MRP import MRPHal, MRPReading, MRPReadingSource, MRPBaseSensor, MRPReadingEntry, MRPMeasurementConfig, \
    MRPReadingSourceStatic, MRPDataVisualization, MRPPolarVisualization


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
        "SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=3",
        "M220 S100"
    ]
    # ALL GCODE COMMANDS WHICH ARE NEEDED BEFORE STARTING A MEASUREMENT
    MEASUREMENT_START_GCODE: [str] = [
        # HOME MECHANIC
        "G28 Y",
        "G28 X",
        "SET_IDLE_TIMEOUT TIMEOUT=3600",
        "M220 S8000"
    ]

    MEASUREMENTS_END_GCODE: [str] = [
        # HOME AGAIN
        "G28 Y",
        "G28 X",
        # DISABLE MOTORS
        "M84",
        "SET_IDLE_TIMEOUT TIMEOUT=10",
        "M220 S100"
    ]

    MEASUREMENT_CONFIG: dict = {
        # AXIS LIMITS
        # 0-180 DEGREE
        "MAX_THETA_MECHANIC": 20.0,
        "MIN_THETA_MECHANIC": 0.0,
        # 0- 360 DEGREE
        "MIN_PHI_MECHANIC": 0.0,
        "MAX_PHI_MECHANIC": 78.0,

        "MOVE_MECHANIC_GCODE": "G1 Y{phi:.2f} X{theta:.2f} F10", # "G1 Y{phi:.2f} F10",
        "MOVE_DELAY": -1.0 #1.0 # SET TO -1.0 TO DISABLE
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

    def mapf(self, _x: float, _in_min: float, _in_max:float, _out_min:float, _out_max:float) -> float:
        return (_x - _in_min) * (_out_max - _out_min) / (_in_max - _in_min) + _out_min

    def perform_measurement(self, _measurement_points: int, _average_readings_per_datapoint: int) -> [MRPReading.MRPReading]:
        if not self.hal_instance.is_connected():
            self.hal_instance.connect()

        sensor: MRPBaseSensor.MRPBaseSensor = MRPBaseSensor.MRPBaseSensor(self.hal_instance)
        result_readings: [MRPReading.MRPReading] = []



        # CALCULATE ROATION NEEDED

        # PREPRRE MECHANIC FOR MEASUREMENT
        for cmd in self.MEASUREMENT_START_GCODE:
            self.hal_instance.query_command_str("gcode {}".format(cmd))


        for s_idx in range(sensor.sensor_count):
            # CREATE MEASUREMENT CONFIG
            mmc: MRPMeasurementConfig.MRPMeasurementConfig = MRPMeasurementConfig.MRPMeasurementConfig()
            mmc.configure_fullsphere_custom(_measurement_points=_measurement_points)
            mmc.id = self.hal_instance.get_sensor_id()
            mmc.sensor_id = s_idx
            # CREATE A READING WITH CREATED CONFIG
            reading: MRPReading.MRPReading = MRPReading.MRPReading(mmc)
            # SET READING NAME
            reading.set_name("SID{}".format(mmc.id, mmc.sensor_id, reading.get_magnet_type().name))
            result_readings.append(reading)

        # CALCULATE POSITIONS
        n_theta: int = result_readings[0].measurement_config.n_theta
        n_phi: int = result_readings[0].measurement_config.n_phi

        theta_radians: float = result_readings[0].measurement_config.theta_radians
        phi_radians: float = result_readings[0].measurement_config.phi_radians
        # CALCULATE GRID
        theta, phi = np.mgrid[0.0:theta_radians:n_theta * 1j, 0.0:phi_radians:n_phi * 1j]

        # MOVE MECHANIC TO EACH POLAR POSITION
        reading_index_theta: int = 0
        reading_index_phi: int = 0
        for p in phi[0, :]:
            reading_index_phi = reading_index_phi + 1
            reading_index_theta = 0
            for t in theta[:, 0]:
                reading_index_theta = reading_index_theta + 1

                phi_abs_pos = self.mapf(p, 0.0, phi_radians, self.MEASUREMENT_CONFIG['MIN_PHI_MECHANIC'], self.MEASUREMENT_CONFIG['MAX_PHI_MECHANIC'])
                theta_abs_pos = self.mapf(t, 0.0, theta_radians, self.MEASUREMENT_CONFIG['MIN_THETA_MECHANIC'], self.MEASUREMENT_CONFIG['MAX_THETA_MECHANIC'])



                # MOVE TO CALCULATED POSTION
                move_gcode: str = self.MEASUREMENT_CONFIG['MOVE_MECHANIC_GCODE'].format(theta=theta_abs_pos, phi=phi_abs_pos)
                self.hal_instance.query_command_str("gcode {}".format(move_gcode))
                self.hal_instance.query_command_str("gcode {}".format("M400"))

                # ADD ADDITIONAL DELAY IF NEEDED
                if 'MOVE_DELAY' in self.MEASUREMENT_CONFIG:
                    ad_delay: float = self.MEASUREMENT_CONFIG['MOVE_DELAY']
                    if ad_delay > 0.0:
                        time.sleep(ad_delay)

                print(move_gcode)
                # PERFORM MEASUREMENT WITH CALCULATED POSTION VALUES

                for m_idx in range(sensor.sensor_count):
                    # PERFORM READING FOR EACH USER SET DATAPOINT
                    # LOOP OVER ALL DATAPOINTS
                    rentry: [MRPReadingEntry.MRPReadingEntry] = MRPReadingSourceStatic.MRPReadingSourceStatic.get_base_sensor_reading(sensor, result_readings[m_idx], _average_readings_per_datapoint)

                    for idx, _ in enumerate(result_readings):
                        # MODIFY ENTRY AND SET POSITION DATA
                        entry: MRPReadingEntry.MRPReadingEntry = rentry[idx]
                        # SET READING INDEX
                        entry.reading_index_phi = reading_index_phi
                        entry.reading_index_theta = reading_index_theta
                        # SET READING POSITION
                        entry.phi = p
                        entry.theta = t
                        # ADD READING ENTRY TO MEASUREMENT
                        result_readings[idx].insert_reading_instance(entry, _autoupdate_measurement_config=True)



        # RESET MECHANIC AFTER MEASUREMENT
        for cmd in self.MEASUREMENTS_END_GCODE:
            self.hal_instance.query_command_str("gcode {}".format(cmd))

        return result_readings

    def export_visualisation(self, _readings: [MRPReading.MRPReading], _export_file: str):

        MRPDataVisualization.MRPDataVisualization.plot_error(_readings, _filename=_export_file)
        MRPDataVisualization.MRPDataVisualization.plot_scatter(_readings, _filename=_export_file)
        MRPDataVisualization.MRPDataVisualization.plot_temperature(_readings, _filename=_export_file)

        for idx, reading in enumerate(_readings):
            # ADDITIONAL PLOT 3D
            visu = MRPPolarVisualization.MRPPolarVisualization(reading)

            # 3D PLOT TO FILE
            visu.plot3d("RID{}_{}{}".format(idx, _export_file, "_plot3d"))
            visu.plot2d_top("RID{}_{}{}".format(idx, _export_file, "_plot2dtop"))
            visu.plot2d_side("RID{}_{}{}".format(idx, _export_file, "_plot2dside"))
