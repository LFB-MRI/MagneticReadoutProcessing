"""Typer base MRPcli interface to allow the user to setup an RotationalSensor"""

__version__ = '0.0.1'



import json
import bleach
import signal
from werkzeug.local import Local, LocalManager
import flask
import typer
from flask import Flask, request, jsonify, make_response, redirect, render_template, g
from flask_cors import CORS, cross_origin
import time
import multiprocessing
from waitress import serve
from threading import Lock
import MRP
import machineid
from moonraker import MoonrakerPrinter
from MRP import MRPPHalRestRequestResponseState, MRPHal


class RSPProxyGlobals:
    sensor_port: MRPHal.MRPHalSerialPortInformation
    sensor: MRPHal.MRPPHal
    mechanic: MoonrakerPrinter
    lock: Lock = Lock()
    initialized: bool = False


    def __init__(self):
        self.sensor_port = MRPHal.MRPHalSerialPortInformation(_path="")
        self.sensor = MRP.MRPHal.MRPPHal = MRP.MRPHal.MRPPHal(self.sensor_port)
        self.mechanic = None
        self.mechanic = MoonrakerPrinter("http://127.0.0.1", no_init=True)


        self.initialized = False

    def init(self, klipperendpoint:str, sensordevice:str, sensorbaud:int = 0, disbaleprecheck:bool = False):


        self.mechanic.set_address("{}".format(klipperendpoint))
        self.mechanic.init()

        self.sensor_port.device_path = sensordevice
        self.sensor.set_serial_port_information(self.sensor_port)

        # CHECK PARAMETERS
        self.mechanic.send_gcode('M115')  # REQUEST VERSION
        got_response = False
        for msg in self.mechanic.get_gcode(count=20):
            if 'FIRMWARE_NAME' in msg or 'FIRMWARE_VERSION' in msg:
                got_response = True
                print(msg)
                break
        if got_response:
            print("PRECHECK: MECHANIC: {}".format(True))
        elif not disbaleprecheck:
            raise Exception("cant connect to klipper/moonrakerusing: {}".format(klipperendpoint))
        # CHECK SENSOR CONNECTION

        try:
            if sensorbaud > 0:
                self.sensor_port.baudrate = sensorbaud

            self.sensor.connect()
            print("PRECHECK: SENSOR: {}".format(self.sensor.get_sensor_id()))
            self.sensor.disconnect()
        except Exception as e:
            if not disbaleprecheck:
                raise Exception("cant connect to sensor using {}: {}".format(sensordevice, str(e)))

        self.initialized = True


app_typer = typer.Typer()
app_flask = Flask(__name__)
cors = CORS(app_flask)
app_flask.config['CORS_HEADERS'] = 'Content-Type'

terminate_flask: bool = False
hardware_instances: RSPProxyGlobals = RSPProxyGlobals()

#local = Local()
#local_manager = LocalManager([local])


def signal_andler(signum, frame):
    global terminate_flask
    terminate_flask = True
    time.sleep(4)
    exit(1)
signal.signal(signal.SIGINT, signal_andler)


@app_flask.errorhandler(404)
def page_not_found(e):
    return redirect("/rsp/status")

@app_flask.route("/printer/objects/query?configfile")
@cross_origin()
def __unused__():

    return jsonify( {"result": {"eventtime": 18614.047398108, "status": {"configfile": {"config": {"virtual_sdcard": {"path": "~/printer_data/gcodes", "on_error_gcode": "CANCEL_PRINT"}, "pause_resume": {}, "display_status": {}, "respond": {}, "gcode_macro CANCEL_PRINT": {"description": "Cancel the actual running print", "rename_existing": "CANCEL_PRINT_BASE", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set allow_park = client.park_at_cancel|default(false)|lower == 'true' %}\n{% set retract = client.cancel_retract|default(5.0)|abs %}\n\n{% set park_x = \"\" if (client.park_at_cancel_x|default(none) is none)\nelse \"X=\" ~ client.park_at_cancel_x %}\n{% set park_y = \"\" if (client.park_at_cancel_y|default(none) is none)\nelse \"Y=\" ~ client.park_at_cancel_y %}\n{% set custom_park = park_x|length > 0 or park_y|length > 0 %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if (custom_park or not printer.pause_resume.is_paused) and allow_park %} _TOOLHEAD_PARK_PAUSE_CANCEL {park_x} {park_y} {% endif %}\n_CLIENT_RETRACT LENGTH={retract}\nTURN_OFF_HEATERS\nM106 S0\n\nSET_PAUSE_NEXT_LAYER ENABLE=0\nSET_PAUSE_AT_LAYER ENABLE=0 LAYER=0\nCANCEL_PRINT_BASE"}, "gcode_macro PAUSE": {"description": "Pause the actual running print", "rename_existing": "PAUSE_BASE", "variable_restore_idle_timeout": "0", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set idle_timeout = client.idle_timeout|default(0) %}\n{% set temp = printer[printer.toolhead.extruder].target if printer.toolhead.extruder != '' else 0%}\n{% set restore = False if printer.toolhead.extruder == ''\nelse True  if params.RESTORE|default(1)|int == 1 else False %}\n\nSET_GCODE_VARIABLE MACRO=RESUME VARIABLE=last_extruder_temp VALUE=\"{{'restore': restore, 'temp': temp}}\"\n\n{% if idle_timeout > 0 %}\nSET_GCODE_VARIABLE MACRO=PAUSE VARIABLE=restore_idle_timeout VALUE={printer.configfile.settings.idle_timeout.timeout}\nSET_IDLE_TIMEOUT TIMEOUT={idle_timeout}\n{% endif %}\nPAUSE_BASE\n_TOOLHEAD_PARK_PAUSE_CANCEL {rawparams}"}, "gcode_macro RESUME": {"description": "Resume the actual running print", "rename_existing": "RESUME_BASE", "variable_last_extruder_temp": "{'restore': False, 'temp': 0}", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set sp_move = client.speed_move|default(velocity) %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if printer.idle_timeout.state|upper == \"IDLE\" %}\n{% if last_extruder_temp.restore %} M109 S{last_extruder_temp.temp} {% endif %}\n{% endif %}\n_CLIENT_EXTRUDE\nRESUME_BASE VELOCITY={params.VELOCITY|default(sp_move)}"}, "gcode_macro SET_PAUSE_NEXT_LAYER": {"description": "Enable a pause if the next layer is reached", "gcode": "\n{% set pause_next_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_next_layer %}\n{% set ENABLE = params.ENABLE|default(1)|int != 0 %}\n{% set MACRO = params.MACRO|default(pause_next_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_next_layer VALUE=\"{{ 'enable': ENABLE, 'call': MACRO }}\""}, "gcode_macro SET_PAUSE_AT_LAYER": {"description": "Enable/disable a pause if a given layer number is reached", "gcode": "\n{% set pause_at_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_at_layer %}\n{% set ENABLE = params.ENABLE|int != 0 if params.ENABLE is defined\nelse params.LAYER is defined %}\n{% set LAYER = params.LAYER|default(pause_at_layer.layer)|int %}\n{% set MACRO = params.MACRO|default(pause_at_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_at_layer VALUE=\"{{ 'enable': ENABLE, 'layer': LAYER, 'call': MACRO }}\""}, "gcode_macro SET_PRINT_STATS_INFO": {"rename_existing": "SET_PRINT_STATS_INFO_BASE", "description": "Overwrite, to get pause_next_layer and pause_at_layer feature", "variable_pause_next_layer": "{ 'enable': False, 'call': \"PAUSE\" }", "variable_pause_at_layer": "{ 'enable': False, 'layer': 0, 'call': \"PAUSE\" }", "gcode": "\n{% if pause_next_layer.enable %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_next_layer\" % pause_next_layer.call}'\n{pause_next_layer.call}\nSET_PAUSE_NEXT_LAYER ENABLE=0\n{% elif pause_at_layer.enable and params.CURRENT_LAYER is defined and params.CURRENT_LAYER|int == pause_at_layer.layer %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_at_layer [%d]\" % (pause_at_layer.call, pause_at_layer.layer)}'\n{pause_at_layer.call}\nSET_PAUSE_AT_LAYER ENABLE=0\n{% endif %}\nSET_PRINT_STATS_INFO_BASE {rawparams}"}, "gcode_macro _TOOLHEAD_PARK_PAUSE_CANCEL": {"description": "Helper: park toolhead used in PAUSE and CANCEL_PRINT", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set use_custom     = client.use_custom_pos|default(false)|lower == 'true' %}\n{% set custom_park_x  = client.custom_park_x|default(0.0) %}\n{% set custom_park_y  = client.custom_park_y|default(0.0) %}\n{% set park_dz        = client.custom_park_dz|default(2.0)|abs %}\n{% set sp_hop         = client.speed_hop|default(15) * 60 %}\n{% set sp_move        = client.speed_move|default(velocity) * 60 %}\n\n{% set origin    = printer.gcode_move.homing_origin %}\n{% set act       = printer.gcode_move.gcode_position %}\n{% set max       = printer.toolhead.axis_maximum %}\n{% set cone      = printer.toolhead.cone_start_z|default(max.z) %}\n{% set round_bed = True if printer.configfile.settings.printer.kinematics is in ['delta','polar','rotary_delta','winch']\nelse False %}\n\n{% set z_min = params.Z_MIN|default(0)|float %}\n{% set z_park = [[(act.z + park_dz), z_min]|max, (max.z - origin.z)]|min %}\n{% set x_park = params.X       if params.X is defined\nelse custom_park_x  if use_custom\nelse 0.0            if round_bed\nelse (max.x - 5.0) %}\n{% set y_park = params.Y       if params.Y is defined\nelse custom_park_y  if use_custom\nelse (max.y - 5.0)  if round_bed and z_park < cone\nelse 0.0            if round_bed\nelse (max.y - 5.0) %}\n\n_CLIENT_RETRACT\n{% if \"xyz\" in printer.toolhead.homed_axes %}\nG90\nG1 Z{z_park} F{sp_hop}\nG1 X{x_park} Y{y_park} F{sp_move}\n{% if not printer.gcode_move.absolute_coordinates %} G91 {% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Printer not homed'\n{% endif %}"}, "gcode_macro _CLIENT_EXTRUDE": {"description": "Extrudes, if the extruder is hot enough", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set use_fw_retract = (client.use_fw_retract|default(false)|lower == 'true') and (printer.firmware_retraction is defined) %}\n{% set length = params.LENGTH|default(client.unretract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_unretract)|default(35) %}\n{% set absolute_extrude = printer.gcode_move.absolute_extrude %}\n\n{% if printer.toolhead.extruder != '' %}\n{% if printer[printer.toolhead.extruder].can_extrude %}\n{% if use_fw_retract %}\n{% if length < 0 %}\nG10\n{% else %}\nG11\n{% endif %}\n{% else %}\nM83\nG1 E{length} F{(speed|float|abs) * 60}\n{% if absolute_extrude %}\nM82\n{% endif %}\n{% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Extruder not hot enough'\n{% endif %}\n{% endif %}"}, "gcode_macro _CLIENT_RETRACT": {"description": "Retracts, if the extruder is hot enough", "gcode": "\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set length = params.LENGTH|default(client.retract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_retract)|default(35) %}\n\n_CLIENT_EXTRUDE LENGTH=-{length|float|abs} SPEED={speed|float|abs}"}, "mcu": {"serial": "/dev/ttyAMA0", "restart_method": "command"}, "printer": {"kinematics": "cartesian", "max_velocity": "20", "max_accel": "50", "max_z_velocity": "15", "max_z_accel": "15", "square_corner_velocity": "6.0"}, "idle_timeout": {"timeout": "10"}, "stepper_x": {"step_pin": "gpio11", "dir_pin": "gpio10", "enable_pin": "!gpio12", "rotation_distance": "40", "microsteps": "32", "full_steps_per_rotation": "200", "endstop_pin": "!gpio4", "position_endstop": "0", "position_max": "120", "homing_speed": "20", "homing_retract_dist": "2", "homing_positive_dir": "false"}, "tmc2209 stepper_x": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": "0", "interpolate": "False", "run_current": "1.0", "sense_resistor": "0.110", "stealthchop_threshold": "0", "diag_pin": "^gpio4", "driver_sgthrs": "255"}, "stepper_y": {"step_pin": "gpio6", "dir_pin": "!gpio5", "enable_pin": "!gpio7", "rotation_distance": "40", "microsteps": "32", "full_steps_per_rotation": "200", "endstop_pin": "^gpio3", "position_endstop": "0", "position_max": "2000", "homing_speed": "10", "homing_retract_dist": "10", "homing_positive_dir": "false"}, "tmc2209 stepper_y": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": "2", "interpolate": "False", "run_current": "1.2", "sense_resistor": "0.110", "stealthchop_threshold": "0", "diag_pin": "^gpio3", "driver_sgthrs": "10"}, "stepper_z": {"step_pin": "gpio19", "dir_pin": "!gpio28", "enable_pin": "!gpio2", "rotation_distance": "8", "microsteps": "32", "endstop_pin": "^gpio25", "position_endstop": "120", "position_max": "120", "position_min": "-1.5", "homing_speed": "20", "second_homing_speed": "3.0", "homing_retract_dist": "3.0"}, "tmc2209 stepper_z": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": "1", "interpolate": "False", "run_current": "0.56", "sense_resistor": "0.110", "stealthchop_threshold": "0"}}, "settings": {"mcu": {"serial": "/dev/ttyAMA0", "baud": 250000, "restart_method": "command", "max_stepper_error": 2.5e-05}, "virtual_sdcard": {"path": "~/printer_data/gcodes", "on_error_gcode": "CANCEL_PRINT"}, "pause_resume": {"recover_velocity": 50.0}, "respond": {"default_type": "echo", "default_prefix": "echo:"}, "gcode_macro cancel_print": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set allow_park = client.park_at_cancel|default(false)|lower == 'true' %}\n{% set retract = client.cancel_retract|default(5.0)|abs %}\n\n{% set park_x = \"\" if (client.park_at_cancel_x|default(none) is none)\nelse \"X=\" ~ client.park_at_cancel_x %}\n{% set park_y = \"\" if (client.park_at_cancel_y|default(none) is none)\nelse \"Y=\" ~ client.park_at_cancel_y %}\n{% set custom_park = park_x|length > 0 or park_y|length > 0 %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if (custom_park or not printer.pause_resume.is_paused) and allow_park %} _TOOLHEAD_PARK_PAUSE_CANCEL {park_x} {park_y} {% endif %}\n_CLIENT_RETRACT LENGTH={retract}\nTURN_OFF_HEATERS\nM106 S0\n\nSET_PAUSE_NEXT_LAYER ENABLE=0\nSET_PAUSE_AT_LAYER ENABLE=0 LAYER=0\nCANCEL_PRINT_BASE", "rename_existing": "CANCEL_PRINT_BASE", "description": "Cancel the actual running print"}, "gcode_macro pause": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set idle_timeout = client.idle_timeout|default(0) %}\n{% set temp = printer[printer.toolhead.extruder].target if printer.toolhead.extruder != '' else 0%}\n{% set restore = False if printer.toolhead.extruder == ''\nelse True  if params.RESTORE|default(1)|int == 1 else False %}\n\nSET_GCODE_VARIABLE MACRO=RESUME VARIABLE=last_extruder_temp VALUE=\"{{'restore': restore, 'temp': temp}}\"\n\n{% if idle_timeout > 0 %}\nSET_GCODE_VARIABLE MACRO=PAUSE VARIABLE=restore_idle_timeout VALUE={printer.configfile.settings.idle_timeout.timeout}\nSET_IDLE_TIMEOUT TIMEOUT={idle_timeout}\n{% endif %}\nPAUSE_BASE\n_TOOLHEAD_PARK_PAUSE_CANCEL {rawparams}", "rename_existing": "PAUSE_BASE", "description": "Pause the actual running print", "variable_restore_idle_timeout": "0"}, "gcode_macro resume": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set sp_move = client.speed_move|default(velocity) %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if printer.idle_timeout.state|upper == \"IDLE\" %}\n{% if last_extruder_temp.restore %} M109 S{last_extruder_temp.temp} {% endif %}\n{% endif %}\n_CLIENT_EXTRUDE\nRESUME_BASE VELOCITY={params.VELOCITY|default(sp_move)}", "rename_existing": "RESUME_BASE", "description": "Resume the actual running print", "variable_last_extruder_temp": "{'restore': False, 'temp': 0}"}, "gcode_macro set_pause_next_layer": {"gcode": "\n{% set pause_next_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_next_layer %}\n{% set ENABLE = params.ENABLE|default(1)|int != 0 %}\n{% set MACRO = params.MACRO|default(pause_next_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_next_layer VALUE=\"{{ 'enable': ENABLE, 'call': MACRO }}\"", "description": "Enable a pause if the next layer is reached"}, "gcode_macro set_pause_at_layer": {"gcode": "\n{% set pause_at_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_at_layer %}\n{% set ENABLE = params.ENABLE|int != 0 if params.ENABLE is defined\nelse params.LAYER is defined %}\n{% set LAYER = params.LAYER|default(pause_at_layer.layer)|int %}\n{% set MACRO = params.MACRO|default(pause_at_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_at_layer VALUE=\"{{ 'enable': ENABLE, 'layer': LAYER, 'call': MACRO }}\"", "description": "Enable/disable a pause if a given layer number is reached"}, "gcode_macro set_print_stats_info": {"gcode": "\n{% if pause_next_layer.enable %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_next_layer\" % pause_next_layer.call}'\n{pause_next_layer.call}\nSET_PAUSE_NEXT_LAYER ENABLE=0\n{% elif pause_at_layer.enable and params.CURRENT_LAYER is defined and params.CURRENT_LAYER|int == pause_at_layer.layer %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_at_layer [%d]\" % (pause_at_layer.call, pause_at_layer.layer)}'\n{pause_at_layer.call}\nSET_PAUSE_AT_LAYER ENABLE=0\n{% endif %}\nSET_PRINT_STATS_INFO_BASE {rawparams}", "rename_existing": "SET_PRINT_STATS_INFO_BASE", "description": "Overwrite, to get pause_next_layer and pause_at_layer feature", "variable_pause_next_layer": "{ 'enable': False, 'call': \"PAUSE\" }", "variable_pause_at_layer": "{ 'enable': False, 'layer': 0, 'call': \"PAUSE\" }"}, "gcode_macro _toolhead_park_pause_cancel": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set use_custom     = client.use_custom_pos|default(false)|lower == 'true' %}\n{% set custom_park_x  = client.custom_park_x|default(0.0) %}\n{% set custom_park_y  = client.custom_park_y|default(0.0) %}\n{% set park_dz        = client.custom_park_dz|default(2.0)|abs %}\n{% set sp_hop         = client.speed_hop|default(15) * 60 %}\n{% set sp_move        = client.speed_move|default(velocity) * 60 %}\n\n{% set origin    = printer.gcode_move.homing_origin %}\n{% set act       = printer.gcode_move.gcode_position %}\n{% set max       = printer.toolhead.axis_maximum %}\n{% set cone      = printer.toolhead.cone_start_z|default(max.z) %}\n{% set round_bed = True if printer.configfile.settings.printer.kinematics is in ['delta','polar','rotary_delta','winch']\nelse False %}\n\n{% set z_min = params.Z_MIN|default(0)|float %}\n{% set z_park = [[(act.z + park_dz), z_min]|max, (max.z - origin.z)]|min %}\n{% set x_park = params.X       if params.X is defined\nelse custom_park_x  if use_custom\nelse 0.0            if round_bed\nelse (max.x - 5.0) %}\n{% set y_park = params.Y       if params.Y is defined\nelse custom_park_y  if use_custom\nelse (max.y - 5.0)  if round_bed and z_park < cone\nelse 0.0            if round_bed\nelse (max.y - 5.0) %}\n\n_CLIENT_RETRACT\n{% if \"xyz\" in printer.toolhead.homed_axes %}\nG90\nG1 Z{z_park} F{sp_hop}\nG1 X{x_park} Y{y_park} F{sp_move}\n{% if not printer.gcode_move.absolute_coordinates %} G91 {% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Printer not homed'\n{% endif %}", "description": "Helper: park toolhead used in PAUSE and CANCEL_PRINT"}, "gcode_macro _client_extrude": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set use_fw_retract = (client.use_fw_retract|default(false)|lower == 'true') and (printer.firmware_retraction is defined) %}\n{% set length = params.LENGTH|default(client.unretract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_unretract)|default(35) %}\n{% set absolute_extrude = printer.gcode_move.absolute_extrude %}\n\n{% if printer.toolhead.extruder != '' %}\n{% if printer[printer.toolhead.extruder].can_extrude %}\n{% if use_fw_retract %}\n{% if length < 0 %}\nG10\n{% else %}\nG11\n{% endif %}\n{% else %}\nM83\nG1 E{length} F{(speed|float|abs) * 60}\n{% if absolute_extrude %}\nM82\n{% endif %}\n{% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Extruder not hot enough'\n{% endif %}\n{% endif %}", "description": "Extrudes, if the extruder is hot enough"}, "gcode_macro _client_retract": {"gcode": "\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set length = params.LENGTH|default(client.retract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_retract)|default(35) %}\n\n_CLIENT_EXTRUDE LENGTH=-{length|float|abs} SPEED={speed|float|abs}", "description": "Retracts, if the extruder is hot enough"}, "idle_timeout": {"timeout": 10.0, "gcode": "\n{% if 'heaters' in printer %}\n   TURN_OFF_HEATERS\n{% endif %}\nM84\n"}, "tmc2209 stepper_x": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": 0, "diag_pin": "^gpio4", "run_current": 1.0, "hold_current": 2.0, "sense_resistor": 0.11, "interpolate": False, "stealthchop_threshold": 0.0, "driver_multistep_filt": True, "driver_toff": 3, "driver_hstrt": 5, "driver_hend": 0, "driver_tbl": 2, "driver_iholddelay": 8, "driver_pwm_ofs": 36, "driver_pwm_grad": 14, "driver_pwm_freq": 1, "driver_pwm_autoscale": True, "driver_pwm_autograd": True, "driver_pwm_reg": 8, "driver_pwm_lim": 12, "driver_tpowerdown": 20, "driver_sgthrs": 255}, "stepper_x": {"microsteps": 32, "step_pin": "gpio11", "dir_pin": "gpio10", "rotation_distance": 40.0, "full_steps_per_rotation": 200, "gear_ratio": [], "enable_pin": "!gpio12", "endstop_pin": "!gpio4", "position_endstop": 0.0, "position_min": 0.0, "position_max": 120.0, "homing_speed": 20.0, "second_homing_speed": 10.0, "homing_retract_speed": 20.0, "homing_retract_dist": 2.0, "homing_positive_dir": False}, "tmc2209 stepper_y": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": 2, "diag_pin": "^gpio3", "run_current": 1.2, "hold_current": 2.0, "sense_resistor": 0.11, "interpolate": False, "stealthchop_threshold": 0.0, "driver_multistep_filt": True, "driver_toff": 3, "driver_hstrt": 5, "driver_hend": 0, "driver_tbl": 2, "driver_iholddelay": 8, "driver_pwm_ofs": 36, "driver_pwm_grad": 14, "driver_pwm_freq": 1, "driver_pwm_autoscale": True, "driver_pwm_autograd": True, "driver_pwm_reg": 8, "driver_pwm_lim": 12, "driver_tpowerdown": 20, "driver_sgthrs": 10}, "stepper_y": {"microsteps": 32, "step_pin": "gpio6", "dir_pin": "!gpio5", "rotation_distance": 40.0, "full_steps_per_rotation": 200, "gear_ratio": [], "enable_pin": "!gpio7", "endstop_pin": "^gpio3", "position_endstop": 0.0, "position_min": 0.0, "position_max": 2000.0, "homing_speed": 10.0, "second_homing_speed": 5.0, "homing_retract_speed": 10.0, "homing_retract_dist": 10.0, "homing_positive_dir": False}, "tmc2209 stepper_z": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": 1, "run_current": 0.56, "hold_current": 2.0, "sense_resistor": 0.11, "interpolate": False, "stealthchop_threshold": 0.0, "driver_multistep_filt": True, "driver_toff": 3, "driver_hstrt": 5, "driver_hend": 0, "driver_tbl": 2, "driver_iholddelay": 8, "driver_pwm_ofs": 36, "driver_pwm_grad": 14, "driver_pwm_freq": 1, "driver_pwm_autoscale": True, "driver_pwm_autograd": True, "driver_pwm_reg": 8, "driver_pwm_lim": 12, "driver_tpowerdown": 20, "driver_sgthrs": 0}, "stepper_z": {"microsteps": 32, "step_pin": "gpio19", "dir_pin": "!gpio28", "rotation_distance": 8.0, "full_steps_per_rotation": 200, "gear_ratio": [], "enable_pin": "!gpio2", "endstop_pin": "^gpio25", "position_endstop": 120.0, "position_min": -1.5, "position_max": 120.0, "homing_speed": 20.0, "second_homing_speed": 3.0, "homing_retract_speed": 20.0, "homing_retract_dist": 3.0, "homing_positive_dir": True}, "printer": {"max_velocity": 20.0, "max_accel": 50.0, "max_accel_to_decel": 25.0, "square_corner_velocity": 6.0, "buffer_time_low": 1.0, "buffer_time_high": 2.0, "buffer_time_start": 0.25, "move_flush_time": 0.05, "kinematics": "cartesian", "max_z_velocity": 15.0, "max_z_accel": 15.0}, "force_move": {"enable_force_move": False}}, "warnings": [], "save_config_pending": False, "save_config_pending_items": {}}}}})


@app_flask.route("/rsp/initialize")
@cross_origin()
def initialize():
    global hardware_instances

    #user = request.args.get('user')
    origin = bleach.clean(request.args.get('origin', ''))
    # IF NOT INITILALIZED INIT HARDWARE_INSTANCED_ WITH PROVIDED HARDWARE PARAMETERS
    if not app_flask.config.get('initialized', False):
        with hardware_instances.lock:
            klipperendpoint: str = app_flask.config["syscfg"]["klipperendpoint"]
            sensordevice: str = app_flask.config["syscfg"]["sensordevice"]
            sensorbaud: int = app_flask.config["syscfg"]["sensorbaud"]
            disbaleprecheck: int = app_flask.config["syscfg"]["disbaleprecheck"]

            hardware_instances.init(klipperendpoint, sensordevice, sensorbaud, disbaleprecheck)

            app_flask.config['initialized'] = True


    if len(origin) > 0:
        return redirect(origin)

    return jsonify(app_flask.config)

@app_flask.route("/rsp/disconnect")
@cross_origin()
def disconnect():
    global hardware_lock

    # if system is not initialized redirect to init route first
    if not app_flask.config.get('initialized', False):
        return redirect('/rsp/initialize?origin=/rsp/disconnect')



    return jsonify({"error": False})


@app_flask.route("/rsp/status")
@cross_origin()
def status():
    ret: MRPPHalRestRequestResponseState = MRPPHalRestRequestResponseState.MRPPHalRestRequestResponseState()
    ret.sensortype = "rotationsensor"
    ret.id = machineid.id()
    ret.version = __version__
    # also add startconfig
    resdict: dict = ret.__dict__
    resdict.update(app_flask.config.get('syscfg', {}))

    # if system is not initialized redirect to init route first
    if not app_flask.config.get('initialized', False):
        resdict['initialized'] = False
    else:
        resdict['initialized'] = True

    return jsonify(resdict)


def flask_server_task(_config: dict):
    global hardware_instances
    host: str = _config.get("host", "0.0.0.0")
    port: int = _config.get("port", 5556)
    debug: bool = _config.get("dbg", False)

    app_flask.config.update(_config)
    #with flas
    #    flask.g.test = 0

    #app_flask.app_context().push()
    if debug:
        app_flask.run(host=host, port=port, debug=debug)
    else:
        serve(app_flask, host=host, port=port)




@app_typer.command()
def rotational(typer_ctx: typer.Context, port: int = 5556, host: str = "0.0.0.0", debug: bool = False, klipperendpoint: str = "http://127.0.0.1", sensordevice: str = "/dev/ttyACM0", sensorbaud: int = 0, disbaleprecheck: int = 0):
    global terminate_flask
    #global hardware_instances



    sys_cfg = {
        'klipperendpoint': klipperendpoint,
        'sensordevice': sensordevice,
        'sensorbaud': sensorbaud,
        'disbaleprecheck': disbaleprecheck,
        'initialized': False
    }




    # FINALLY START FLASK

    flask_config = {"port": port, "host": host, "dbg": debug, "syscfg": sys_cfg}
    flask_server: multiprocessing.Process = multiprocessing.Process(target=flask_server_task, args=(flask_config,))
    flask_server.start()

    # STORE user parameter in flask context to access them in each route
    #flask_ctx = app_flask.app_context()




    while( not terminate_flask):
        print("Proxy started. http://{}:{}/".format(host, port))
        if typer.prompt("Terminate  [Y/n]", 'y') == 'y':
            break


    # STOP
    flask_server.terminate()
    flask_server.join()



@app_typer.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass






if __name__ == "__main__":
    app_typer()
