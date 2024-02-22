// CUSTOM INCLUDES
#include "main.h"

#ifdef ARDUINO_ARCH_MBED
REDIRECT_STDOUT_TO(DEBUG_SERIAL) // MBED  printf(...) to console
#endif

// CLASSES
TCA9548A tca9584a(SENSOR_WIRE);

DBGCommandParser debug_command_parser;
HostCommandParser host_command_parser;

#if defined(HOST_SERIAL_RX) && defined(HOST_SERIAL_TX)
HardwareSerial HOST_SERIAL(HOST_SERIAL_RX, HOST_SERIAL_TX); // RX TX  // FOR SERIAL ANC
#endif

#ifdef SENSOR_WIRE_ALT
arduino::MbedI2C Wire1(SENSOR_WIRE_ALT_SDA_PIN, SENSOR_WIRE_ALT_SCL_PIN);
#endif

sync_timer readout_timer(READOUT_SPEED_IN_SINGLEMODE_DELAY, false);
sensor_info sensors_found[MAX_TLV_SENSORS] = {sensor_info()}; // TWO POSSIBLE SENSORS PER TCA CHANNEL S0 16 SENSORS PER SLICE
sensor_result sensor_results[MAX_TLV_SENSORS] = {sensor_result()};
System_State system_state = System_State_Error;

long readout_index = 0;
int sensor_number = 0;
int anc_base_id = -1;

void error(const bool _critical, const int _code)
{
  pinMode(ERROR_LED_PIN, OUTPUT);
  DEBUG_SERIAL.println("error:" + System_Error_Code_STR[_code]);
  HOST_SERIAL.println("error:" + System_Error_Code_STR[_code]);

  while (_critical)
  {
    for (int i = 0; i < _code; i++)
    {
      digitalWrite(ERROR_LED_PIN, HIGH);
      delay(100);
      digitalWrite(ERROR_LED_PIN, LOW);
      delay(100);
    }
    delay(1000);

    DEBUG_SERIAL.println("error:" + System_Error_Code_STR[_code]);
    HOST_SERIAL.println("error:" + System_Error_Code_STR[_code]);
  }
}

// RETURNS THE SYSTE; TEMP HERE WE ARE USING THE SENSORS BUILD IN TEMPERATURE SENSOR
void list_sensor_capabilities(DBGCommandParser::Argument *args, char *response)
{
  // todo check which sensor Tpes are presnet
  DEBUG_SERIAL.println("static, axis_b, axis_x, axis_y, axis_z, axis_temp, axis_stimestamp");
}

// RETURNS THE SYSTE; TEMP HERE WE ARE USING THE SENSORS BUILD IN TEMPERATURE SENSOR
void list_sensor_commands(DBGCommandParser::Argument *args, char *response)
{
  // todo check which sensor Tpes are presnet
  DEBUG_SERIAL.println("sensorcnt, readsensor, temp, ");
}

// RETURNS THE SYSTE; TEMP HERE WE ARE USING THE SENSORS BUILD IN TEMPERATURE SENSOR
void temp_debug(DBGCommandParser::Argument *args, char *response)
{
  float temp = 0.0f;
  int c = 0;
  for (int i = 0; i < sensor_number; i++)
  {
    sensor_info *sensor = &sensors_found[i];
    if (sensor->valid)
    {
      sensor_result *result = &sensor_results[i];
      temp += result->t;
      c++;
    }
  }
  if (c > 0)
  {
    DEBUG_SERIAL.println(temp / c * 1.0);
  }
  else
  {
    strlcpy(response, "error", DBGCommandParser::MAX_RESPONSE_SIZE);
  }
};

void readsensor_debug(DBGCommandParser::Argument *args, char *response)
{
  const String axis = args[0].asString;
  const int id = (int32_t)args[1].asInt64;

  if (id < 0 && id > sensor_number)
  {
    return;
  }

  sensor_result *result = &sensor_results[id];

  switch (axis.charAt(0))
  {
  case 'x':
    DEBUG_SERIAL.println(result->x);
    break;
  case 'y':
    DEBUG_SERIAL.println(result->y);
    break;
  case 'z':
    DEBUG_SERIAL.println(result->z);
    break;
  case 'b':
    DEBUG_SERIAL.println(result->b);
    break;
  case 't':
    DEBUG_SERIAL.println(result->t);
    break;
  case 's':
    DEBUG_SERIAL.println(result->ts);
    break;
  default:
    strlcpy(response, "error", DBGCommandParser::MAX_RESPONSE_SIZE);
    break;
  }
}

// WILL BE CALLED IF HOST REQUESTS A MEASUREMENT
void sync_irq_function()
{
  // HERE WE MANUALLY EXIPRES THE TIMER FROM THE MAIN LOOP
  readout_timer.trigger_timer_expire();
}

void process_anc_information(DBGCommandParser::Argument *args, char *response)
{
  const int base_id = (int32_t)args[0].asInt64;
  if (system_state == System_State_WAIT_FOR_ANC && base_id >= 0)
  {
    anc_base_id = base_id;
    system_state = System_State_ANC_GOT_SYNC_PACKET;
  }
  else
  {
    strlcpy(response, "error not in right system state or invalid base_id", HostCommandParser::MAX_RESPONSE_SIZE);
  }
}

int scan_for_sensors()
{
  // SCAN FOR TLV SENSORS
  // if not tca found only one channel/sensor can be connected
  int max_tca_channels = 1;
  int found_sensors = 0;
  if (tca9584a.isEnabled())
  {
    max_tca_channels = TCA9548A_Channels;
    tca9584a.resetChannels();

    for (int i = 0; i < max_tca_channels; i++)
    {
      // SET TCA CHANNEL
      tca9584a.setChannel(i, true);
      // SCAN FOR SENSORS
      const int arr_index = found_sensors;
      sensors_found[arr_index].index = found_sensors;
      sensors_found[arr_index].tca_channel = i;
      sensors_found[arr_index].valid = sensors_found[arr_index].sensor_instance.begin(SENSOR_WIRE);
      sensor_number++;
      // UNSET TCA CHANNEL
      tca9584a.setChannel(i, false);
    }
  }
  else
  {
    // TCA IS NOT PRESENT JUST TRY TO ADD ONE SENSOR

    // i2c_scan
    delay(1000);
    for (size_t i = 0; i < IMPLEMENTED_SENSOR_COUNT; i++)
    {
      const ImplementedSensors sensor_to_scan = static_cast<ImplementedSensors>(i);
      const int sensor_to_scan_addr = ImplementedSensorsAddressLookup[sensor_to_scan];
      if (sensor_to_scan_addr == I2C_ADDR_INVALID)
      {
        continue;
      }

      HOST_SERIAL.println(ImplementedSensors_STR[sensor_to_scan]);

      sensors_found[found_sensors].index = found_sensors;
      sensors_found[found_sensors].tca_channel = 0;
      sensors_found[found_sensors].valid = sensors_found[found_sensors].sensor_instance.begin(SENSOR_WIRE, sensor_to_scan);

      if (sensors_found[found_sensors].valid)
      {
        found_sensors++;
      }

#ifdef SENSOR_WIRE_ALT
    sensors_found[found_sensors].index = found_sensors;
    sensors_found[found_sensors].tca_channel = 0;
    sensors_found[found_sensors].valid = sensors_found[found_sensors].sensor_instance.begin(Wire1, sensor_to_scan);
    if (sensors_found[found_sensors].valid)
    {
      found_sensors++;
    }
#endif

      if (found_sensors >= MAX_TLV_SENSORS)
      {
        DEBUG_SERIAL.println("MAX_SENSORS_REACHED");
        break;
      }
    }
  }

#ifdef CREATE_VIRTUAL_SENSOR_IF_NOT_HARDWARE_SENSORS_FOUND
  if (found_sensors <= 0)
  {
    sensors_found[0].index = 0;
    sensors_found[0].tca_channel = 0;
    sensors_found[0].valid = sensors_found[found_sensors].sensor_instance.begin(SENSOR_WIRE, ImplementedSensors::SIMULATED_START);
  }
#endif

  return found_sensors;
}

void setup()
{
  DEBUG_SERIAL.begin(GENERAL_SERIAL_SPEED);
  DEBUG_SERIAL.println("setup");

  // SETUP HOST SERIAL ANC
  HOST_SERIAL.begin(GENERAL_SERIAL_SPEED);
  delay(2000);
  system_state = System_State_SETUP;
  DEBUG_SERIAL.println("sysstate_" + System_State_STR[system_state]);

  // SETUP DEBUG COMMAND PARSER TO ALLOW SOME DEBUGGING
  debug_command_parser.registerCommand("help", "", [](DBGCommandParser::Argument *args, char *response)
                                       {
      DEBUG_SERIAL.println(F("============================================================================================="));
      DEBUG_SERIAL.println(F("> help                         shows this message"));
      DEBUG_SERIAL.println(F("> version                      prints version information"));
      DEBUG_SERIAL.println(F("> id                           sensor serial number for identification purposes"));
      DEBUG_SERIAL.println(F("> sysstate                     returns current system state machine state"));
      DEBUG_SERIAL.println(F("> opmode                       returns 1 if in single mode"));
     // DEBUG_SERIAL.println(F("> sensorscn                   scans i2c bus for sensors"));
      DEBUG_SERIAL.println(F("> sensorcnt                   returns found sensorcount"));
      DEBUG_SERIAL.println(F("> readsensor x <0-senorcount>  returns the readout result for a given sensor index for X axis"));
      DEBUG_SERIAL.println(F("> readsensor y <0-senorcount>  returns the readout result for a given sensor index for Y axis"));
      DEBUG_SERIAL.println(F("> readsensor z <0-senorcount>  returns the readout result for a given sensor index for Z axis"));
      DEBUG_SERIAL.println(F("> readsensor b <0-senorcount>  returns the readout result for a given sensor index for B axis"));
      DEBUG_SERIAL.println(F("> temp                         returns the system temperature"));
      DEBUG_SERIAL.println(F("> anc <base_id>                perform a autonumbering sequence manually"));
      DEBUG_SERIAL.println(F("> ancid                        returns the current set autonumbering base id (-1 in singlemode)"));
      DEBUG_SERIAL.println(F("> reset                        performs reset of the system"));
      DEBUG_SERIAL.println(F("> info                         logs sensor capabilities"));
      DEBUG_SERIAL.println(F("> commands                     lists sensor implemented commamnds which can be used by hal"));
      DEBUG_SERIAL.println(F("> sid                          lists detected sensor types"));
      DEBUG_SERIAL.println(F("=============================================================================================")); });

  debug_command_parser.registerCommand("version", "", [](DBGCommandParser::Argument *args, char *response)
                                       {
                                        #ifdef VERSION
                                        DEBUG_SERIAL.println(VERSION);
                                        #else
                                        DEBUG_SERIAL.println("v" + String(VERSION_MAJOR) + "." + String(VERSION_MINOR) + "." + String(VERSION_REVISION));
                                        #endif
                                        });

  debug_command_parser.registerCommand("id", "", [](DBGCommandParser::Argument *args, char *response){ for (size_t i = 0; i < 8; i++){Serial.print(UniqueID8[i], DEC);}Serial.println(); });

  debug_command_parser.registerCommand("sid", "", [](DBGCommandParser::Argument *args, char *response){ for (size_t i = 0; i < sensor_number; i++){ Serial.print(i);Serial.print(":");Serial.println(sensors_found[i].sensor_instance.get_sensor_name()); }});

  debug_command_parser.registerCommand("sysstate", "", [](DBGCommandParser::Argument *args, char *response)
                                       { DEBUG_SERIAL.println(System_State_STR[system_state]); });

  debug_command_parser.registerCommand("opmode", "", [](DBGCommandParser::Argument *args, char *response)
                                       {
    if (!digitalRead(SINGLE_MODE_PIN))
  {
    DEBUG_SERIAL.println("SingleModeEnabled");
  }else{
    DEBUG_SERIAL.println("SingleModeDisabled");
  } });

  debug_command_parser.registerCommand("sensorcnt", "", [](DBGCommandParser::Argument *args, char *response)
                                       { DEBUG_SERIAL.println(sensor_number); });

  // readsensor command accepts an int as argument for the given sensor id and x/y/z/b for the axis
  debug_command_parser.registerCommand("readsensor", "si", &readsensor_debug);

  debug_command_parser.registerCommand("temp", "", &temp_debug);

  debug_command_parser.registerCommand("anc", "i", &process_anc_information);

  debug_command_parser.registerCommand("ancid", "", [](DBGCommandParser::Argument *args, char *response)
                                       { DEBUG_SERIAL.println(anc_base_id); });

  debug_command_parser.registerCommand("reset", "", [](DBGCommandParser::Argument *args, char *response)
                                       { DEBUG_SERIAL.println("performing_reset"); RESET_SYSTEM_FUNCTION(); });

  // REGISTER HOST COMMANDS
  host_command_parser.registerCommand("anc", "i", &process_anc_information);

  debug_command_parser.registerCommand("reset", "", [](DBGCommandParser::Argument *args, char *response)
                                       { HOST_SERIAL.println("reset"); RESET_SYSTEM_FUNCTION(); });

  debug_command_parser.registerCommand("info", "", &list_sensor_capabilities);
  debug_command_parser.registerCommand("commands", "", &list_sensor_commands);

  // GPIO SETUP
  pinMode(SINGLE_MODE_PIN, INPUT_PULLUP);
  pinMode(STATUS_LED_PIN, OUTPUT);
  digitalWrite(STATUS_LED_PIN, LOW);

  pinMode(SYNC_PIN_STATUS_LED, OUTPUT);
  digitalWrite(SYNC_PIN_STATUS_LED, LOW);

  // I2C SENSOR INTERFACE SETUP
#if defined(SENSOR_WIRE_SCL_PIN) && defined(SENSOR_WIRE_SDA_PIN)
  SENSOR_WIRE.setSCL(SENSOR_WIRE_SCL_PIN);
  SENSOR_WIRE.setSDA(SENSOR_WIRE_SDA_PIN);
#endif

  SENSOR_WIRE.begin();

#ifdef SENSOR_WIRE_ALT
  Wire1.begin();
#endif

  if (!digitalRead(SINGLE_MODE_PIN))
  {
    DEBUG_SERIAL.println("log_singlemodeenabled");
  }
  else
  {
    DEBUG_SERIAL.println("log_singlemodedisabled");
    pinMode(SYNC_PIN_IRQ_INPUT, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(SYNC_PIN_IRQ_INPUT), sync_irq_function, CHANGE);
  }

  // i2c_scan(SENSOR_WIRE);
  //  CHECK IF TCA9584A IS PRESENT
  if (is_i2c_device_present(SENSOR_WIRE, TCA9548A_ADDRESS0))
  {
    tca9584a.begin(TCA9548A_ADDRESS0, true);
  }
  else
  {
    tca9584a.begin(TCA9548A_ADDRESS0, false);
  }

  delay(1000);
  sensor_number = scan_for_sensors();
  if (sensor_number <= 0)
  {

    error(false, System_Error_Code_TLV_NO_SENSORS_FOUND);
    while (sensor_number <= 0)
    {
      sensor_number = scan_for_sensors();
    }
  }

  // INIT SENSORS
  tca9584a.resetChannels();

  for (int i = 0; i < sensor_number; i++)
  {
    // SET TCA TO THE CORRECT CHANNEL
    tca9584a.setChannel(sensors_found[i].tca_channel, true);
    // QUERY SENSOR
    sensors_found[i].sensor_instance.query_sensor();
    // RESET TCA CHANNEL
    tca9584a.setChannel(sensors_found[i].tca_channel, false);
  }

  // SETUP ANC SERIAL
  system_state = System_State_WAIT_FOR_ANC;
  anc_base_id = -1;
}

void loop()
{
  // HANDLE SYSTEM STATE
  // WAIt FOR THE ANC PACKET
  if (system_state == System_State_WAIT_FOR_ANC)
  {
    if (!digitalRead(SINGLE_MODE_PIN))
    {
      system_state = System_State_ANC_GOT_SYNC_PACKET;
    }
    else if (anc_base_id >= 0)
    {
      // TODO SETUP CAN
    }
  }
  else if (system_state == System_State_ANC_GOT_SYNC_PACKET)
  {
    // IF GOT ANC INFORMATION ARE INVALID WAIT FOR NEXT CYCLE
    if (anc_base_id < 0)
    {
      system_state = System_State_WAIT_FOR_ANC;
      anc_base_id = -1;
    }
    // SETUP SLICE COMMUNICATION SETTINGS
    const int next_slice_id = anc_base_id + sensor_number + 1;

    // FORWARD NEXT ID TO NEXT SENSOR SLICE
    HOST_SERIAL.println("anc " + String(anc_base_id));
    // FINALLY SWITCH TO SENSOR READOUT
    system_state = System_State_READOUT_LOOP;
    // START READOUT TIMER
    // IF IN SINGLEMODE WE WARE USING A SECOND TIMER TO READOUT THE SENSORS
    if (!digitalRead(SINGLE_MODE_PIN))
    {
      readout_timer.start();
    }
  }
  else if (system_state == System_State_READOUT_LOOP)
  {
    // TRIGGER READOUT
    if (readout_timer.expired())
    {
      digitalWrite(STATUS_LED_PIN, HIGH);
      for (int i = 0; i < sensor_number; i++)
      {
        sensor_info *sensor = &sensors_found[i];
        tca9584a.setChannel(sensor->tca_channel, true);
        sensor->sensor_instance.query_sensor();
        tca9584a.setChannel(sensor->tca_channel, false);
      }
      readout_index++;

      // READ RESULT // TODO OPTIMIZE
      for (int i = 0; i < sensor_number; i++)
      {
        sensor_info *sensor = &sensors_found[i];
        sensor_result *result = &sensor_results[i];
        // UPDATE DATA
        result->set(sensor->sensor_instance.get_result());
        result->ts = readout_index;

        digitalWrite(STATUS_LED_PIN, LOW);
      }
    }
  }

  if (DEBUG_SERIAL.available())
  {
    char line[128];
    size_t lineLength = DEBUG_SERIAL.readBytesUntil('\n', line, 127);
    line[lineLength] = '\0';

    char response[DBGCommandParser::MAX_RESPONSE_SIZE];
    debug_command_parser.processCommand(line, response);
    DEBUG_SERIAL.println(response);
  }

  if (HOST_SERIAL.available())
  {
    char line[128];
    size_t lineLength = HOST_SERIAL.readBytesUntil('\n', line, 127);
    line[lineLength] = '\0';

    char response[HostCommandParser::MAX_RESPONSE_SIZE];
    host_command_parser.processCommand(line, response);
    HOST_SERIAL.println(response);
  }
}
