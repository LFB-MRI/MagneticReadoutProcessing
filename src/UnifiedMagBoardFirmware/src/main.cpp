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

#ifdef ENABLE_HARDWARE_AVERAGING
RingBuf<sensor_result, MAX_AVERAGING_COUNT> sensor_results[MAX_TLV_SENSORS];
int hw_averaging_samples = MAX_AVERAGING_COUNT;
#else
sensor_result sensor_results[MAX_TLV_SENSORS] = {sensor_result()};
#endif
System_State system_state = System_State_Error;

bool wait_for_readout_ready = false;
bool readout_ready = false;
long readout_index = 0;
int sensor_number = 0;
int anc_base_id = -1;
String readout_triggered_axis;
int readout_triggered_id;

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

void setup_hwavg(DBGCommandParser::Argument *args, char *response)
{
#ifdef ENABLE_HARDWARE_AVERAGING
  const int hvavg = abs((int32_t)args[0].asInt64);
  if (hvavg > MAX_AVERAGING_COUNT)
  {
    hw_averaging_samples = MAX_AVERAGING_COUNT;
  }
  else
  {
    hw_averaging_samples = hvavg;
  }
  DEBUG_SERIAL.println(String(hw_averaging_samples));
#else
  DEBUG_SERIAL.println("1");
#endif
}

void trigger_hwavgcls(DBGCommandParser::Argument *args, char *response)
{
#ifdef ENABLE_HARDWARE_AVERAGING
  for (int i = 0; i < sensor_number; i++)
  {
    sensor_results[i].clear();
  }
#endif
  DEBUG_SERIAL.println("1");
}

// RETURNS THE SYSTE; TEMP HERE WE ARE USING THE SENSORS BUILD IN TEMPERATURE SENSOR
void list_sensor_capabilities(DBGCommandParser::Argument *args, char *response)
{
// todo check which sensor Tpes are presnet
#ifdef ENABLE_HARDWARE_AVERAGING
  DEBUG_SERIAL.println("static, axis_b, axis_x, axis_y, axis_z, axis_temp, axis_stimestamp, hwavg");
#else
  DEBUG_SERIAL.println("static, axis_b, axis_x, axis_y, axis_z, axis_temp, axis_stimestamp");
#endif
}

// RETURNS THE SYSTE; TEMP HERE WE ARE USING THE SENSORS BUILD IN TEMPERATURE SENSOR
void list_sensor_commands(DBGCommandParser::Argument *args, char *response)
{
// todo check which sensor Tpes are presnet
#ifdef ENABLE_HARDWARE_AVERAGING
  DEBUG_SERIAL.println("sensorcnt, readsensor, temp, hwavg, ");
#else
  DEBUG_SERIAL.println("sensorcnt, readsensor, temp, ");
#endif
}

// RETURNS THE SYSTE; TEMP HERE WE ARE USING THE SENSORS BUILD IN TEMPERATURE SENSOR
void temp_debug(DBGCommandParser::Argument *args, char *response)
{
  readout_triggered_axis = "t";
  readout_triggered_id = (int32_t)args[1].asInt64;
  wait_for_readout_ready = true; // SET TO RESPONSE WITH READOUT
};

void readsensor_debug(DBGCommandParser::Argument *args, char *response)
{
  readout_triggered_axis = args[0].asString;
  readout_triggered_id = (int32_t)args[1].asInt64;
  wait_for_readout_ready = true; // SET TO RESPONSE WITH READOUT
  readout_index++;
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


#ifdef USER_BUTTON_TRIGGER_INPUT
  void user_button_trigger_irq(){
    if (system_state == System_State_READOUT_LOOP && !wait_for_readout_ready)
    {
      readout_triggered_axis = "b";
      readout_triggered_id = 0;
      wait_for_readout_ready = true; // SET TO RESPONSE WITH READOUT
      readout_index++;
    }
  }
#endif


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
    found_sensors++;
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

#ifdef IS_RP2040_BOARD
    DEBUG_SERIAL.println("IS_RP2040_BOARD");
#endif
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

#ifdef ENABLE_HARDWARE_AVERAGING
      DEBUG_SERIAL.println(F("> hwavg <avg_samples>          enables hardware averaging"));
      DEBUG_SERIAL.println(F("> hwavgcls                     clears ringbuffer"));
#endif
      DEBUG_SERIAL.println(F("=============================================================================================")); });

  debug_command_parser.registerCommand("version", "", [](DBGCommandParser::Argument *args, char *response)
                                       {
#ifdef VERSION
                                         DEBUG_SERIAL.println(VERSION);
#else
        DEBUG_SERIAL.println("v" + String(VERSION_MAJOR) + "." + String(VERSION_MINOR) + "." + String(VERSION_REVISION));
#endif
                                       });

  debug_command_parser.registerCommand("id", "", [](DBGCommandParser::Argument *args, char *response)
                                       { for (size_t i = 0; i < 8; i++){Serial.print(UniqueID8[i], DEC);}Serial.println(); });

  debug_command_parser.registerCommand("sid", "", [](DBGCommandParser::Argument *args, char *response)
                                       { for (size_t i = 0; i < sensor_number; i++){ Serial.print(sensors_found[i].sensor_instance.get_sensor_name());Serial.print(", "); }; Serial.println("");});

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
  debug_command_parser.registerCommand("hwavg", "i", &setup_hwavg);
  debug_command_parser.registerCommand("hwavgcls", "", &trigger_hwavgcls);

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

#if defined(IS_RP2040_BOARD)
    attachInterrupt(SYNC_PIN_IRQ_INPUT, sync_irq_function, RISING);
#elif defined(IS_STM32F4_BOARD)
    attachInterrupt(SYNC_PIN_IRQ_INPUT, sync_irq_function, RISING);
#else
    attachInterrupt(digitalPinToInterrupt(SYNC_PIN_IRQ_INPUT), sync_irq_function, RISING);
#endif
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


  //ATTACH IRQ IF ENABLED
#ifdef USER_BUTTON_TRIGGER_INPUT
  DEBUG_SERIAL.println("USER_BUTTON_TRIGGER_INPUT ENABLED");
  pinMode(USER_BUTTON_TRIGGER_INPUT, INPUT_PULLUP);
  #if defined(IS_RP2040_BOARD)
    attachInterrupt(USER_BUTTON_TRIGGER_INPUT, user_button_trigger_irq, RISING);
  #elif defined(IS_STM32F4_BOARD)
    attachInterrupt(USER_BUTTON_TRIGGER_INPUT, user_button_trigger_irq, RISING);
  #else
    attachInterrupt(digitalPinToInterrupt(USER_BUTTON_TRIGGER_INPUT)), user_button_trigger_irq, RISING);
  #endif
#endif
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

      // READ RESULT // TODO OPTIMIZE
      for (int i = 0; i < sensor_number; i++)
      {
        sensor_info *sensor = &sensors_found[i];
#ifdef ENABLE_HARDWARE_AVERAGING
        sensor_result r = sensor->sensor_instance.get_result();
        r.ts = readout_index;
        sensor_results[i].lockedPush(r);

        if (wait_for_readout_ready)
        {
          if (sensor_results[i].size() >= hw_averaging_samples || sensor_results[i].isFull())
          {
            readout_ready = true;
          }
          else
          {
            readout_ready = false;
          }
        }
#else
        sensor_result *result = &sensor_results[i];
        // UPDATE DATA
        result->set(sensor->sensor_instance.get_result());
        result->ts = readout_index;
        readout_ready = true;
#endif
        digitalWrite(STATUS_LED_PIN, LOW);
      }
    }

    if (wait_for_readout_ready && readout_ready)
    {
      readout_ready = false;

      // REPONSE WITH READING
      if (readout_triggered_id >= 0 && readout_triggered_id < sensor_number)
      {
#ifdef ENABLE_HARDWARE_AVERAGING
        sensor_result result = sensor_result();

        const int avg_samples = sensor_results[readout_triggered_id].size();
        if (avg_samples > 0)
        {
          result.set(sensor_results[readout_triggered_id][0]);
        }
        for (int i = 0; i < avg_samples; i++)
        {
          sensor_result r;
          sensor_results[readout_triggered_id].pop(r);

          result.x = (result.x + r.x) / 2;
          result.y = (result.y + r.y) / 2;
          result.z = (result.z + r.z) / 2;
          result.b = (result.b + r.b) / 2;
          result.t = (result.t + r.t) / 2;
        }

#else
        sensor_result result = sensor_results[readout_triggered_id];
#endif
        switch (readout_triggered_axis.charAt(0))
        {
        case 'x':
          DEBUG_SERIAL.println(result.x);
          break;
        case 'y':
          DEBUG_SERIAL.println(result.y);
          break;
        case 'z':
          DEBUG_SERIAL.println(result.z);
          break;
        case 'b':
          DEBUG_SERIAL.println(result.b);
          break;
        case 't':
          DEBUG_SERIAL.println(result.t);
          break;
        case 's':
          DEBUG_SERIAL.println(result.ts);
          break;
        default:
          DEBUG_SERIAL.println("error");
          break;
        }
        wait_for_readout_ready = false;

        while(DEBUG_SERIAL.available() > 0) {
          char t = Serial.read();
        }

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
    if(response && response[0] != '\0'){
     // DEBUG_SERIAL.println(response);
    }
   
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
