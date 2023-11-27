from requests import get, post
from MRP import MRPHal, MRPHalSerialPortInformation


class MMRPHalKlipperException(Exception):
    def __init__(self, message="MMRPHalKlipperException thrown"):
        self.message = message
        super().__init__(self.message)

class MRPHalKlipper(MRPHal.MRPHal):
    """
    Baseclass for sending commands to a klipper/moonraker instance
    It contains functions to send rec commands from/to a klipper/moonraker interface
    """


    printercfg: dict = {"result": {"eventtime": 18614.047398108, "status": {"configfile": {"config": {"virtual_sdcard": {"path": "~/printer_data/gcodes", "on_error_gcode": "CANCEL_PRINT"}, "pause_resume": {}, "display_status": {}, "respond": {}, "gcode_macro CANCEL_PRINT": {"description": "Cancel the actual running print", "rename_existing": "CANCEL_PRINT_BASE", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set allow_park = client.park_at_cancel|default(false)|lower == 'true' %}\n{% set retract = client.cancel_retract|default(5.0)|abs %}\n\n{% set park_x = \"\" if (client.park_at_cancel_x|default(none) is none)\nelse \"X=\" ~ client.park_at_cancel_x %}\n{% set park_y = \"\" if (client.park_at_cancel_y|default(none) is none)\nelse \"Y=\" ~ client.park_at_cancel_y %}\n{% set custom_park = park_x|length > 0 or park_y|length > 0 %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if (custom_park or not printer.pause_resume.is_paused) and allow_park %} _TOOLHEAD_PARK_PAUSE_CANCEL {park_x} {park_y} {% endif %}\n_CLIENT_RETRACT LENGTH={retract}\nTURN_OFF_HEATERS\nM106 S0\n\nSET_PAUSE_NEXT_LAYER ENABLE=0\nSET_PAUSE_AT_LAYER ENABLE=0 LAYER=0\nCANCEL_PRINT_BASE"}, "gcode_macro PAUSE": {"description": "Pause the actual running print", "rename_existing": "PAUSE_BASE", "variable_restore_idle_timeout": "0", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set idle_timeout = client.idle_timeout|default(0) %}\n{% set temp = printer[printer.toolhead.extruder].target if printer.toolhead.extruder != '' else 0%}\n{% set restore = False if printer.toolhead.extruder == ''\nelse True  if params.RESTORE|default(1)|int == 1 else False %}\n\nSET_GCODE_VARIABLE MACRO=RESUME VARIABLE=last_extruder_temp VALUE=\"{{'restore': restore, 'temp': temp}}\"\n\n{% if idle_timeout > 0 %}\nSET_GCODE_VARIABLE MACRO=PAUSE VARIABLE=restore_idle_timeout VALUE={printer.configfile.settings.idle_timeout.timeout}\nSET_IDLE_TIMEOUT TIMEOUT={idle_timeout}\n{% endif %}\nPAUSE_BASE\n_TOOLHEAD_PARK_PAUSE_CANCEL {rawparams}"}, "gcode_macro RESUME": {"description": "Resume the actual running print", "rename_existing": "RESUME_BASE", "variable_last_extruder_temp": "{'restore': False, 'temp': 0}", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set sp_move = client.speed_move|default(velocity) %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if printer.idle_timeout.state|upper == \"IDLE\" %}\n{% if last_extruder_temp.restore %} M109 S{last_extruder_temp.temp} {% endif %}\n{% endif %}\n_CLIENT_EXTRUDE\nRESUME_BASE VELOCITY={params.VELOCITY|default(sp_move)}"}, "gcode_macro SET_PAUSE_NEXT_LAYER": {"description": "Enable a pause if the next layer is reached", "gcode": "\n{% set pause_next_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_next_layer %}\n{% set ENABLE = params.ENABLE|default(1)|int != 0 %}\n{% set MACRO = params.MACRO|default(pause_next_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_next_layer VALUE=\"{{ 'enable': ENABLE, 'call': MACRO }}\""}, "gcode_macro SET_PAUSE_AT_LAYER": {"description": "Enable/disable a pause if a given layer number is reached", "gcode": "\n{% set pause_at_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_at_layer %}\n{% set ENABLE = params.ENABLE|int != 0 if params.ENABLE is defined\nelse params.LAYER is defined %}\n{% set LAYER = params.LAYER|default(pause_at_layer.layer)|int %}\n{% set MACRO = params.MACRO|default(pause_at_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_at_layer VALUE=\"{{ 'enable': ENABLE, 'layer': LAYER, 'call': MACRO }}\""}, "gcode_macro SET_PRINT_STATS_INFO": {"rename_existing": "SET_PRINT_STATS_INFO_BASE", "description": "Overwrite, to get pause_next_layer and pause_at_layer feature", "variable_pause_next_layer": "{ 'enable': False, 'call': \"PAUSE\" }", "variable_pause_at_layer": "{ 'enable': False, 'layer': 0, 'call': \"PAUSE\" }", "gcode": "\n{% if pause_next_layer.enable %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_next_layer\" % pause_next_layer.call}'\n{pause_next_layer.call}\nSET_PAUSE_NEXT_LAYER ENABLE=0\n{% elif pause_at_layer.enable and params.CURRENT_LAYER is defined and params.CURRENT_LAYER|int == pause_at_layer.layer %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_at_layer [%d]\" % (pause_at_layer.call, pause_at_layer.layer)}'\n{pause_at_layer.call}\nSET_PAUSE_AT_LAYER ENABLE=0\n{% endif %}\nSET_PRINT_STATS_INFO_BASE {rawparams}"}, "gcode_macro _TOOLHEAD_PARK_PAUSE_CANCEL": {"description": "Helper: park toolhead used in PAUSE and CANCEL_PRINT", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set use_custom     = client.use_custom_pos|default(false)|lower == 'true' %}\n{% set custom_park_x  = client.custom_park_x|default(0.0) %}\n{% set custom_park_y  = client.custom_park_y|default(0.0) %}\n{% set park_dz        = client.custom_park_dz|default(2.0)|abs %}\n{% set sp_hop         = client.speed_hop|default(15) * 60 %}\n{% set sp_move        = client.speed_move|default(velocity) * 60 %}\n\n{% set origin    = printer.gcode_move.homing_origin %}\n{% set act       = printer.gcode_move.gcode_position %}\n{% set max       = printer.toolhead.axis_maximum %}\n{% set cone      = printer.toolhead.cone_start_z|default(max.z) %}\n{% set round_bed = True if printer.configfile.settings.printer.kinematics is in ['delta','polar','rotary_delta','winch']\nelse False %}\n\n{% set z_min = params.Z_MIN|default(0)|float %}\n{% set z_park = [[(act.z + park_dz), z_min]|max, (max.z - origin.z)]|min %}\n{% set x_park = params.X       if params.X is defined\nelse custom_park_x  if use_custom\nelse 0.0            if round_bed\nelse (max.x - 5.0) %}\n{% set y_park = params.Y       if params.Y is defined\nelse custom_park_y  if use_custom\nelse (max.y - 5.0)  if round_bed and z_park < cone\nelse 0.0            if round_bed\nelse (max.y - 5.0) %}\n\n_CLIENT_RETRACT\n{% if \"xyz\" in printer.toolhead.homed_axes %}\nG90\nG1 Z{z_park} F{sp_hop}\nG1 X{x_park} Y{y_park} F{sp_move}\n{% if not printer.gcode_move.absolute_coordinates %} G91 {% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Printer not homed'\n{% endif %}"}, "gcode_macro _CLIENT_EXTRUDE": {"description": "Extrudes, if the extruder is hot enough", "gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set use_fw_retract = (client.use_fw_retract|default(false)|lower == 'true') and (printer.firmware_retraction is defined) %}\n{% set length = params.LENGTH|default(client.unretract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_unretract)|default(35) %}\n{% set absolute_extrude = printer.gcode_move.absolute_extrude %}\n\n{% if printer.toolhead.extruder != '' %}\n{% if printer[printer.toolhead.extruder].can_extrude %}\n{% if use_fw_retract %}\n{% if length < 0 %}\nG10\n{% else %}\nG11\n{% endif %}\n{% else %}\nM83\nG1 E{length} F{(speed|float|abs) * 60}\n{% if absolute_extrude %}\nM82\n{% endif %}\n{% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Extruder not hot enough'\n{% endif %}\n{% endif %}"}, "gcode_macro _CLIENT_RETRACT": {"description": "Retracts, if the extruder is hot enough", "gcode": "\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set length = params.LENGTH|default(client.retract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_retract)|default(35) %}\n\n_CLIENT_EXTRUDE LENGTH=-{length|float|abs} SPEED={speed|float|abs}"}, "mcu": {"serial": "/dev/ttyAMA0", "restart_method": "command"}, "printer": {"kinematics": "cartesian", "max_velocity": "20", "max_accel": "50", "max_z_velocity": "15", "max_z_accel": "15", "square_corner_velocity": "6.0"}, "idle_timeout": {"timeout": "10"}, "stepper_x": {"step_pin": "gpio11", "dir_pin": "gpio10", "enable_pin": "!gpio12", "rotation_distance": "40", "microsteps": "32", "full_steps_per_rotation": "200", "endstop_pin": "!gpio4", "position_endstop": "0", "position_max": "120", "homing_speed": "20", "homing_retract_dist": "2", "homing_positive_dir": "false"}, "tmc2209 stepper_x": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": "0", "interpolate": "False", "run_current": "1.0", "sense_resistor": "0.110", "stealthchop_threshold": "0", "diag_pin": "^gpio4", "driver_sgthrs": "255"}, "stepper_y": {"step_pin": "gpio6", "dir_pin": "!gpio5", "enable_pin": "!gpio7", "rotation_distance": "40", "microsteps": "32", "full_steps_per_rotation": "200", "endstop_pin": "^gpio3", "position_endstop": "0", "position_max": "2000", "homing_speed": "10", "homing_retract_dist": "10", "homing_positive_dir": "false"}, "tmc2209 stepper_y": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": "2", "interpolate": "False", "run_current": "1.2", "sense_resistor": "0.110", "stealthchop_threshold": "0", "diag_pin": "^gpio3", "driver_sgthrs": "10"}, "stepper_z": {"step_pin": "gpio19", "dir_pin": "!gpio28", "enable_pin": "!gpio2", "rotation_distance": "8", "microsteps": "32", "endstop_pin": "^gpio25", "position_endstop": "120", "position_max": "120", "position_min": "-1.5", "homing_speed": "20", "second_homing_speed": "3.0", "homing_retract_dist": "3.0"}, "tmc2209 stepper_z": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": "1", "interpolate": "False", "run_current": "0.56", "sense_resistor": "0.110", "stealthchop_threshold": "0"}}, "settings": {"mcu": {"serial": "/dev/ttyAMA0", "baud": 250000, "restart_method": "command", "max_stepper_error": 2.5e-05}, "virtual_sdcard": {"path": "~/printer_data/gcodes", "on_error_gcode": "CANCEL_PRINT"}, "pause_resume": {"recover_velocity": 50.0}, "respond": {"default_type": "echo", "default_prefix": "echo:"}, "gcode_macro cancel_print": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set allow_park = client.park_at_cancel|default(false)|lower == 'true' %}\n{% set retract = client.cancel_retract|default(5.0)|abs %}\n\n{% set park_x = \"\" if (client.park_at_cancel_x|default(none) is none)\nelse \"X=\" ~ client.park_at_cancel_x %}\n{% set park_y = \"\" if (client.park_at_cancel_y|default(none) is none)\nelse \"Y=\" ~ client.park_at_cancel_y %}\n{% set custom_park = park_x|length > 0 or park_y|length > 0 %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if (custom_park or not printer.pause_resume.is_paused) and allow_park %} _TOOLHEAD_PARK_PAUSE_CANCEL {park_x} {park_y} {% endif %}\n_CLIENT_RETRACT LENGTH={retract}\nTURN_OFF_HEATERS\nM106 S0\n\nSET_PAUSE_NEXT_LAYER ENABLE=0\nSET_PAUSE_AT_LAYER ENABLE=0 LAYER=0\nCANCEL_PRINT_BASE", "rename_existing": "CANCEL_PRINT_BASE", "description": "Cancel the actual running print"}, "gcode_macro pause": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set idle_timeout = client.idle_timeout|default(0) %}\n{% set temp = printer[printer.toolhead.extruder].target if printer.toolhead.extruder != '' else 0%}\n{% set restore = False if printer.toolhead.extruder == ''\nelse True  if params.RESTORE|default(1)|int == 1 else False %}\n\nSET_GCODE_VARIABLE MACRO=RESUME VARIABLE=last_extruder_temp VALUE=\"{{'restore': restore, 'temp': temp}}\"\n\n{% if idle_timeout > 0 %}\nSET_GCODE_VARIABLE MACRO=PAUSE VARIABLE=restore_idle_timeout VALUE={printer.configfile.settings.idle_timeout.timeout}\nSET_IDLE_TIMEOUT TIMEOUT={idle_timeout}\n{% endif %}\nPAUSE_BASE\n_TOOLHEAD_PARK_PAUSE_CANCEL {rawparams}", "rename_existing": "PAUSE_BASE", "description": "Pause the actual running print", "variable_restore_idle_timeout": "0"}, "gcode_macro resume": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set sp_move = client.speed_move|default(velocity) %}\n\n\n{% if printer['gcode_macro PAUSE'].restore_idle_timeout > 0 %}\nSET_IDLE_TIMEOUT TIMEOUT={printer['gcode_macro PAUSE'].restore_idle_timeout}\n{% endif %}\n{% if printer.idle_timeout.state|upper == \"IDLE\" %}\n{% if last_extruder_temp.restore %} M109 S{last_extruder_temp.temp} {% endif %}\n{% endif %}\n_CLIENT_EXTRUDE\nRESUME_BASE VELOCITY={params.VELOCITY|default(sp_move)}", "rename_existing": "RESUME_BASE", "description": "Resume the actual running print", "variable_last_extruder_temp": "{'restore': False, 'temp': 0}"}, "gcode_macro set_pause_next_layer": {"gcode": "\n{% set pause_next_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_next_layer %}\n{% set ENABLE = params.ENABLE|default(1)|int != 0 %}\n{% set MACRO = params.MACRO|default(pause_next_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_next_layer VALUE=\"{{ 'enable': ENABLE, 'call': MACRO }}\"", "description": "Enable a pause if the next layer is reached"}, "gcode_macro set_pause_at_layer": {"gcode": "\n{% set pause_at_layer = printer['gcode_macro SET_PRINT_STATS_INFO'].pause_at_layer %}\n{% set ENABLE = params.ENABLE|int != 0 if params.ENABLE is defined\nelse params.LAYER is defined %}\n{% set LAYER = params.LAYER|default(pause_at_layer.layer)|int %}\n{% set MACRO = params.MACRO|default(pause_at_layer.call, True) %}\nSET_GCODE_VARIABLE MACRO=SET_PRINT_STATS_INFO VARIABLE=pause_at_layer VALUE=\"{{ 'enable': ENABLE, 'layer': LAYER, 'call': MACRO }}\"", "description": "Enable/disable a pause if a given layer number is reached"}, "gcode_macro set_print_stats_info": {"gcode": "\n{% if pause_next_layer.enable %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_next_layer\" % pause_next_layer.call}'\n{pause_next_layer.call}\nSET_PAUSE_NEXT_LAYER ENABLE=0\n{% elif pause_at_layer.enable and params.CURRENT_LAYER is defined and params.CURRENT_LAYER|int == pause_at_layer.layer %}\nRESPOND TYPE=echo MSG='{\"%s, forced by pause_at_layer [%d]\" % (pause_at_layer.call, pause_at_layer.layer)}'\n{pause_at_layer.call}\nSET_PAUSE_AT_LAYER ENABLE=0\n{% endif %}\nSET_PRINT_STATS_INFO_BASE {rawparams}", "rename_existing": "SET_PRINT_STATS_INFO_BASE", "description": "Overwrite, to get pause_next_layer and pause_at_layer feature", "variable_pause_next_layer": "{ 'enable': False, 'call': \"PAUSE\" }", "variable_pause_at_layer": "{ 'enable': False, 'layer': 0, 'call': \"PAUSE\" }"}, "gcode_macro _toolhead_park_pause_cancel": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set velocity = printer.configfile.settings.pause_resume.recover_velocity %}\n{% set use_custom     = client.use_custom_pos|default(false)|lower == 'true' %}\n{% set custom_park_x  = client.custom_park_x|default(0.0) %}\n{% set custom_park_y  = client.custom_park_y|default(0.0) %}\n{% set park_dz        = client.custom_park_dz|default(2.0)|abs %}\n{% set sp_hop         = client.speed_hop|default(15) * 60 %}\n{% set sp_move        = client.speed_move|default(velocity) * 60 %}\n\n{% set origin    = printer.gcode_move.homing_origin %}\n{% set act       = printer.gcode_move.gcode_position %}\n{% set max       = printer.toolhead.axis_maximum %}\n{% set cone      = printer.toolhead.cone_start_z|default(max.z) %}\n{% set round_bed = True if printer.configfile.settings.printer.kinematics is in ['delta','polar','rotary_delta','winch']\nelse False %}\n\n{% set z_min = params.Z_MIN|default(0)|float %}\n{% set z_park = [[(act.z + park_dz), z_min]|max, (max.z - origin.z)]|min %}\n{% set x_park = params.X       if params.X is defined\nelse custom_park_x  if use_custom\nelse 0.0            if round_bed\nelse (max.x - 5.0) %}\n{% set y_park = params.Y       if params.Y is defined\nelse custom_park_y  if use_custom\nelse (max.y - 5.0)  if round_bed and z_park < cone\nelse 0.0            if round_bed\nelse (max.y - 5.0) %}\n\n_CLIENT_RETRACT\n{% if \"xyz\" in printer.toolhead.homed_axes %}\nG90\nG1 Z{z_park} F{sp_hop}\nG1 X{x_park} Y{y_park} F{sp_move}\n{% if not printer.gcode_move.absolute_coordinates %} G91 {% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Printer not homed'\n{% endif %}", "description": "Helper: park toolhead used in PAUSE and CANCEL_PRINT"}, "gcode_macro _client_extrude": {"gcode": "\n\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set use_fw_retract = (client.use_fw_retract|default(false)|lower == 'true') and (printer.firmware_retraction is defined) %}\n{% set length = params.LENGTH|default(client.unretract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_unretract)|default(35) %}\n{% set absolute_extrude = printer.gcode_move.absolute_extrude %}\n\n{% if printer.toolhead.extruder != '' %}\n{% if printer[printer.toolhead.extruder].can_extrude %}\n{% if use_fw_retract %}\n{% if length < 0 %}\nG10\n{% else %}\nG11\n{% endif %}\n{% else %}\nM83\nG1 E{length} F{(speed|float|abs) * 60}\n{% if absolute_extrude %}\nM82\n{% endif %}\n{% endif %}\n{% else %}\nRESPOND TYPE=echo MSG='Extruder not hot enough'\n{% endif %}\n{% endif %}", "description": "Extrudes, if the extruder is hot enough"}, "gcode_macro _client_retract": {"gcode": "\n{% set client = printer['gcode_macro _CLIENT_VARIABLE']|default({}) %}\n{% set length = params.LENGTH|default(client.retract)|default(1.0)|float %}\n{% set speed = params.SPEED|default(client.speed_retract)|default(35) %}\n\n_CLIENT_EXTRUDE LENGTH=-{length|float|abs} SPEED={speed|float|abs}", "description": "Retracts, if the extruder is hot enough"}, "idle_timeout": {"timeout": 10.0, "gcode": "\n{% if 'heaters' in printer %}\n   TURN_OFF_HEATERS\n{% endif %}\nM84\n"}, "tmc2209 stepper_x": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": 0, "diag_pin": "^gpio4", "run_current": 1.0, "hold_current": 2.0, "sense_resistor": 0.11, "interpolate": False, "stealthchop_threshold": 0.0, "driver_multistep_filt": True, "driver_toff": 3, "driver_hstrt": 5, "driver_hend": 0, "driver_tbl": 2, "driver_iholddelay": 8, "driver_pwm_ofs": 36, "driver_pwm_grad": 14, "driver_pwm_freq": 1, "driver_pwm_autoscale": True, "driver_pwm_autograd": True, "driver_pwm_reg": 8, "driver_pwm_lim": 12, "driver_tpowerdown": 20, "driver_sgthrs": 255}, "stepper_x": {"microsteps": 32, "step_pin": "gpio11", "dir_pin": "gpio10", "rotation_distance": 40.0, "full_steps_per_rotation": 200, "gear_ratio": [], "enable_pin": "!gpio12", "endstop_pin": "!gpio4", "position_endstop": 0.0, "position_min": 0.0, "position_max": 120.0, "homing_speed": 20.0, "second_homing_speed": 10.0, "homing_retract_speed": 20.0, "homing_retract_dist": 2.0, "homing_positive_dir": False}, "tmc2209 stepper_y": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": 2, "diag_pin": "^gpio3", "run_current": 1.2, "hold_current": 2.0, "sense_resistor": 0.11, "interpolate": False, "stealthchop_threshold": 0.0, "driver_multistep_filt": True, "driver_toff": 3, "driver_hstrt": 5, "driver_hend": 0, "driver_tbl": 2, "driver_iholddelay": 8, "driver_pwm_ofs": 36, "driver_pwm_grad": 14, "driver_pwm_freq": 1, "driver_pwm_autoscale": True, "driver_pwm_autograd": True, "driver_pwm_reg": 8, "driver_pwm_lim": 12, "driver_tpowerdown": 20, "driver_sgthrs": 10}, "stepper_y": {"microsteps": 32, "step_pin": "gpio6", "dir_pin": "!gpio5", "rotation_distance": 40.0, "full_steps_per_rotation": 200, "gear_ratio": [], "enable_pin": "!gpio7", "endstop_pin": "^gpio3", "position_endstop": 0.0, "position_min": 0.0, "position_max": 2000.0, "homing_speed": 10.0, "second_homing_speed": 5.0, "homing_retract_speed": 10.0, "homing_retract_dist": 10.0, "homing_positive_dir": False}, "tmc2209 stepper_z": {"uart_pin": "gpio9", "tx_pin": "gpio8", "uart_address": 1, "run_current": 0.56, "hold_current": 2.0, "sense_resistor": 0.11, "interpolate": False, "stealthchop_threshold": 0.0, "driver_multistep_filt": True, "driver_toff": 3, "driver_hstrt": 5, "driver_hend": 0, "driver_tbl": 2, "driver_iholddelay": 8, "driver_pwm_ofs": 36, "driver_pwm_grad": 14, "driver_pwm_freq": 1, "driver_pwm_autoscale": True, "driver_pwm_autograd": True, "driver_pwm_reg": 8, "driver_pwm_lim": 12, "driver_tpowerdown": 20, "driver_sgthrs": 0}, "stepper_z": {"microsteps": 32, "step_pin": "gpio19", "dir_pin": "!gpio28", "rotation_distance": 8.0, "full_steps_per_rotation": 200, "gear_ratio": [], "enable_pin": "!gpio2", "endstop_pin": "^gpio25", "position_endstop": 120.0, "position_min": -1.5, "position_max": 120.0, "homing_speed": 20.0, "second_homing_speed": 3.0, "homing_retract_speed": 20.0, "homing_retract_dist": 3.0, "homing_positive_dir": True}, "printer": {"max_velocity": 20.0, "max_accel": 50.0, "max_accel_to_decel": 25.0, "square_corner_velocity": 6.0, "buffer_time_low": 1.0, "buffer_time_high": 2.0, "buffer_time_start": 0.25, "move_flush_time": 0.05, "kinematics": "cartesian", "max_z_velocity": 15.0, "max_z_accel": 15.0}, "force_move": {"enable_force_move": False}}, "warnings": [], "save_config_pending": False, "save_config_pending_items": {}}}}}
    settings: dict = {}
    config: dict = {}
    addr: str = "http://127.0.0.1"
    connected: bool = False
    current_port: MRPHalSerialPortInformation.MRPHalSerialPortInformation = None

    def __init__(self, _selected_port: MRPHalSerialPortInformation, _type: MRPHalSerialPortInformation.MRPRemoteSensorType = MRPHalSerialPortInformation.MRPRemoteSensorType.Unknown):
        self.set_serial_port_information(_selected_port)

    def __del__(self):
        pass

    def set_serial_port_information(self, _port: MRPHalSerialPortInformation):
        self.current_port = _port
        self.addr = self.current_port.device_path.replace("klipper://", "http://").replace("klippers://", "https://")

    def get_serial_port_information(self) -> MRPHalSerialPortInformation:
        return self.current_port

    def connect(self) -> bool:

        self.configfile = self.get('/printer/objects/query?configfile')
        self.settings = self.configfile['result']['status']['configfile']['settings']
        self.config = self.configfile['result']['status']['configfile']['config']

        r, _ = self.request_firmware()
        return r

    def is_connected(self) -> bool:
        r, _ = self.request_firmware()
        return r

    def disconnect(self):
        self.send_gcode("M84")
        self.connected = False

    def read_value(self):
        pass

    def send_command(self, _cmd: str) -> [str]:
        if not _cmd:
            raise MMRPHalKlipperException(
                "command is empty {}".format(_cmd))

        # TO AVOID ERRORS APPEND gcode COMMANd IDENTIFIER AT THE BEGINNING
        if not _cmd.startswith("gcode "):
            _cmd = "gcode " + _cmd

        # REPLACE MAY OCCUrING DOUBLE BLANK SPACES
        _cmd = _cmd.replace("  ", " ")
        # REMOVE CMD PARAMETERS
        cmd_wo_parameters: str = _cmd
        if ' ' in _cmd:
            _cmd_sp = _cmd.split(' ')
            cmd_wo_parameters = _cmd_sp[0]
        else:
            _cmd_sp = [_cmd]

        if cmd_wo_parameters not in self.get_sensor_commandlist():
            raise MMRPHalKlipperException("command not supported by this hal instance {}".format(_cmd))


        # CONSTRUCT FINAL GCODE BACK
        gcode_to_send: str = " ".join(_cmd_sp[1:])
        # SEND GCODE TO KLIPPER
        if self.send_gcode(gcode_to_send):
            return self.get_gcode(count=1, simplify=True)
        else:
            raise MMRPHalKlipperException("command sending failed  {}".format(_cmd))

    def query_command_str(self, _cmd: str) -> str:
        res: [str] = self.send_command(_cmd)

        if len(res) <= 0:
            return ""

        # CATCH SOME MOST COMMON KLIPPER ERRORS
        complete_response: str = "".join(str(e) for e in res)
        if 'Unknown command' in complete_response or 'triggered after retract' in complete_response or 'Must home axis first' in complete_response or 'Move out of range' in complete_response:
            raise MMRPHalKlipperException("sensor returned invalid command or command not implemented for {}".format(_cmd))

        return complete_response

    def query_command_int(self, _cmd: str) -> int:
        return int(self.query_command_str(_cmd))

    def query_command_float(self, _cmd: str) -> float:
        return float(self.query_command_str(_cmd))

    def get_sensor_id(self) -> str:
        return self.current_port.device_path.replace(".", "").replace(":", "").replace("/", "")

    def get_sensor_count(self) -> int:
        return 0

    def get_sensor_capabilities(self) -> [str]:
        return ["dynamic", "fullsphere"]
    def get_sensor_commandlist(self) -> [str]:
        return ["gcode"]
    def request_firmware(self) -> (bool, dict):
        self.send_gcode('M115')

        got_response: bool = False
        search: dict = {
            'FIRMWARE_NAME': '',
            'FIRMWARE_VERSION': ''
        }

        for msg in self.get_gcode(count=20):
            print(msg)
            msg = str(msg).strip('/\n')
            msgs = msg.split(' ')
            for so in search.keys():
                for e in msgs:
                    if so in e:
                        got_response = True
                        try:
                            sp = e.split(':')
                            sp.reverse()
                            search[so] = sp[0]
                        except Exception as e:
                            pass


        print(search)
        return (got_response, search)
    def send_gcode(self, cmd: str):
        resp = self.post('/printer/gcode/script?script=%s' % cmd)
        if 'result' in resp:
            return True
        return False
    def get_gcode(self, count: int = 1, simplify: bool = True, msg_type: str = 'response'):
        '''
        Query the gcode store.

        Args
        ----------
        count : int, default=1
            Numbers of cached items to retrieve from the gcode store
        simplify : bool, default=True
            Return only the message portion of each item, as a list
        msg_type : str, default='response'
            One of 'response', 'command', or 'both' to return

        Returns
        -------
        list - cached gcode strings if simplified, dict of each item if not
        '''
        resp = self.get('/server/gcode_store?count=%i' % count)
        store = resp['result']['gcode_store']
        responses = []
        for obj in store:
            if msg_type == 'both':
                responses.append(obj)
            else:
                if obj['type'] == msg_type:
                    responses.append(obj)
        if simplify:
            return [obj['message'] for obj in responses]
        return responses

    def query_status(self, object: str = ''):
        '''
        Query a single printer object.

        Args
        ----
        object : str
            Printer status object

        Returns
        -------
        dict, printer object status
        '''
        query = '/printer/objects/query?%s' % object
        return self.get(query)['result']['status'][object]






    def get(self, url: str):
        '''`response.get` wrapper. `url` concatenated to printer base address
        Returns .json response dict.'''
        return get(self.addr + url).json()

    def post(self, url: str, *args, **kwargs):
        '''`response.set` wrapper. `url` is concatenated to printer base address.
        Returns .json response dict.'''
        return post(self.addr + url, *args, **kwargs).json()
