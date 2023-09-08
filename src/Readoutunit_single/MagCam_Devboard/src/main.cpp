#ifdef USING_PLATFORMIO
#include <Arduino.h>
#endif

#include <Wire.h>

// CUSTOM INCLUDES
#include "main.h"

// CLASSES
TCA9548A tca9584a(SENSOR_WIRE);

DBGCommandParser debug_command_parser;

HardwareSerial Serial1(PA3, PA2); // RX TX  // FOR SERIAL ANC
sync_timer readout_timer(READOUT_SPEED_IN_SINGLEMODE, false);

long readout_index = 0;
int sensor_number = 0;
sensor_info sensors_found[MAX_TLV_SENSORS] = {sensor_info()}; // TWO POSSIBLE SENSORS PER TCA CHANNEL S0 16 SENSORS PER SLICE
sensor_result sensor_results[MAX_TLV_SENSORS] = {sensor_result()};
System_State system_state = System_State_Error;

bool i2c_scan(TwoWire &_wire_instance, const int _check_for_addr = -1, const bool _log = true)
{
  byte error, address;
  int nDevices;

  if (_log)
  {
    LOGGING_SERIAL.println("Scanning...");
  }

  bool addr_found = false;
  nDevices = 0;
  for (address = 1; address < 127; address++)
  {
    // The i2c_scanner uses the return value of
    // the Write.endTransmisstion to see if
    // a device did acknowledge to the address.
    _wire_instance.beginTransmission(address);
    error = _wire_instance.endTransmission();
    if (_log)
    {
      if (error == 0)
      {
        LOGGING_SERIAL.print("I2C device found at address 0x");
        if (address < 16)
        {
          LOGGING_SERIAL.print("0");
        }
        LOGGING_SERIAL.print(address, HEX);
        LOGGING_SERIAL.println("  !");

        nDevices++;
      }
      else if (error == 4)
      {
        LOGGING_SERIAL.print("Unknown error at address 0x");
        if (address < 16)
        {
          LOGGING_SERIAL.print("0");
        }
        LOGGING_SERIAL.println(address, HEX);
      }
    }

    if (_check_for_addr >= 0 && _check_for_addr == address && error == 0)
    {
      addr_found = true;
    }
  }
  if (_log)
  {
    if (nDevices == 0)
    {
      LOGGING_SERIAL.println("No I2C devices found\n");
    }
    else
    {
      LOGGING_SERIAL.println("done\n");
    }
  }

  return addr_found;
}

void error(const bool _critical, const int _code)
{
  pinMode(ERROR_LED_PIN, OUTPUT);
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

    LOGGING_SERIAL.println("error:" + System_Error_Code_STR[_code]);
  }
}

bool is_i2c_device_present(TwoWire &_i2c_interface, const byte _addr)
{
  return i2c_scan(_i2c_interface, _addr, false);
}


// RETURNS THE SYSTE; TEMP HERE WE ARE USING THE SENSORS BUILD IN TEMPERATURE SENSOR
void temp_debug(DBGCommandParser::Argument *args, char *response)
{
  float temp = 0.0f;
  int c = 0;
  for (int i = 0; i < sensor_number; i++)
  {
    sensor_info *sensor = &sensors_found[i];
    if(sensor->valid){
      sensor_result *result = &sensor_results[i];
      temp += result->t;
      c++;
    }
  }
  LOGGING_SERIAL.println(temp / c*1.0);
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
    LOGGING_SERIAL.println(result->x);
    break;
  case 'y':
    LOGGING_SERIAL.println(result->y);
    break;
  case 'z':
    LOGGING_SERIAL.println(result->z);
    break;
  case 'b':
    LOGGING_SERIAL.println(result->b);
    break;
  default:
    break;
  }

  digitalWrite(STATUS_LED_PIN, LOW);

  strlcpy(response, "success", DBGCommandParser::MAX_RESPONSE_SIZE);
}

void setup()
{
  system_state = System_State_SETUP;
  LOGGING_SERIAL.println("sysstate_" + System_State_STR[system_state]);

  LOGGING_SERIAL.begin(115200);
  LOGGING_SERIAL.println("setup");
  // SETUP DEBUG COMMAND PARSER TO ALLOW SOME DEBUGGING
  debug_command_parser.registerCommand("help", "", [](DBGCommandParser::Argument *args, char *response)
                                       {
      LOGGING_SERIAL.println(F("============================================================================================="));
      LOGGING_SERIAL.println(F("> help                       shows this message"));
      LOGGING_SERIAL.println(F("> sysstate                   returns current system state machine state"));
      LOGGING_SERIAL.println(F("> opmode                     returns 1 if in single mode"));
      LOGGING_SERIAL.println(F("> senorcount                 returns found sensorcount"));
      LOGGING_SERIAL.println(F("> readsensor x <0-senorcount>  returns the readout result for a given sensor index for X axis"));
      LOGGING_SERIAL.println(F("> readsensor y <0-senorcount>  returns the readout result for a given sensor index for Y axis"));
      LOGGING_SERIAL.println(F("> readsensor z <0-senorcount>  returns the readout result for a given sensor index for Z axis"));
      LOGGING_SERIAL.println(F("> readsensor b <0-senorcount>  returns the readout result for a given sensor index for B axis"));
      LOGGING_SERIAL.println(F("> temp  returns the system temperature"));
      LOGGING_SERIAL.println(F("=============================================================================================")); });

  debug_command_parser.registerCommand("sysstate", "", [](DBGCommandParser::Argument *args, char *response)
                                       { LOGGING_SERIAL.println(System_State_STR[system_state]); });

  debug_command_parser.registerCommand("opmode", "", [](DBGCommandParser::Argument *args, char *response)
                                       {
    if (!digitalRead(SINGLE_MODE_PIN))
  {
    LOGGING_SERIAL.println("SingleModeEnabled");
  }else{
    LOGGING_SERIAL.println("SingleModeDisabled");
  } });

  debug_command_parser.registerCommand("senorcount", "", [](DBGCommandParser::Argument *args, char *response)
                                       { LOGGING_SERIAL.println(sensor_number); });

  // readsensor command accepts an int as argument for the given sensor id and x/y/z/b for the axis
  debug_command_parser.registerCommand("readsensor", "si", &readsensor_debug);

  debug_command_parser.registerCommand("temp", "", &temp_debug);

  // GPIO SETUP
  pinMode(SINGLE_MODE_PIN, INPUT_PULLUP);
  pinMode(STATUS_LED_PIN, OUTPUT);
  digitalWrite(STATUS_LED_PIN, LOW);

  // I2C SENSOR INTERFACE SETUP
  SENSOR_WIRE.setSCL(SENSOR_WIRE_SCL_PIN);
  SENSOR_WIRE.setSDA(SENSOR_WIRE_SDA_PIN);
  SENSOR_WIRE.begin();

  if (!digitalRead(SINGLE_MODE_PIN))
  {
    LOGGING_SERIAL.println("log_singlemodeenabled");
  }
  else
  {
    LOGGING_SERIAL.println("log_singlemodedisabled");
  }

  // i2c_scan(SENSOR_WIRE);
  //  CHECK IF TCA9584A IS PRESENT
  if (!is_i2c_device_present(SENSOR_WIRE, TCA9548A_ADDRESS0))
  {
    error(true, System_Error_Code_TCA_SCAN_FAILED);
  }
  tca9584a.begin(TCA9548A_ADDRESS0);

  // SCAN FOR TLV SENSORS
  tca9584a.resetChannels();
  for (int i = 0; i < TCA9548A_Channels; i++)
  {
    // SET TCA CHANNEL
    tca9584a.setChannel(i, true);
    volatile byte res = tca9584a.getChannel();

    i2c_scan(SENSOR_WIRE);
    const int arr_index = sensor_number;
    // CHECK IF SENSOR IS PRESENT
    if (is_i2c_device_present(SENSOR_WIRE, Tlv493d_Address::TLV493D_ADDRESS1))
    {
      sensors_found[arr_index].addr = Tlv493d_Address::TLV493D_ADDRESS1;
      sensors_found[arr_index].index = sensor_number;
      sensors_found[arr_index].tca_channel = i;
      sensors_found[arr_index].valid = true;
      sensor_number++;
    }
    else if (is_i2c_device_present(SENSOR_WIRE, Tlv493d_Address::TLV493D_ADDRESS2))
    {
      sensors_found[arr_index].addr = Tlv493d_Address::TLV493D_ADDRESS2;
      sensors_found[arr_index].index = sensor_number;
      sensors_found[arr_index].tca_channel = i;
      sensors_found[arr_index].valid = true;
      sensor_number++;
    }

    tca9584a.setChannel(i, false);
  }

  if (sensor_number <= 0)
  {
    error(true, System_Error_Code_TLV_NO_SENSORS_FOUND);
  }

  // INIT SENSORS
  tca9584a.resetChannels();
  for (int i = 0; i < sensor_number; i++)
  {
    // SET TCA TO THE CORRECT CHANNEL
    tca9584a.setChannel(sensors_found[i].tca_channel, true);
    // INIT SENSOR
    sensors_found[i].sensor_instance.begin(SENSOR_WIRE, sensors_found[i].addr, false);
    sensors_found[i].sensor_instance.updateData();
    // RESET TCA CHANNEL
    tca9584a.setChannel(sensors_found[i].tca_channel, false);
  }

  // SETUP ANC SERIAL
  system_state = System_State_WAIT_FOR_ANC;
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
  }
  else if (system_state == System_State_ANC_GOT_SYNC_PACKET)
  {
    // SETUP SLICE COMMUNICATION SETTINGS

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
        sensor->sensor_instance.updateData();
        tca9584a.setChannel(sensor->tca_channel, false);
      }
      readout_index++;

      // READ RESULT // TODO OPTIMIZE
      for (int i = 0; i < sensor_number; i++)
      {
        sensor_info *sensor = &sensors_found[i];
        sensor_result *result = &sensor_results[i];

        result->x = sensor->sensor_instance.getX();
        result->y = sensor->sensor_instance.getY();
        result->z = sensor->sensor_instance.getZ();
        result->b = sensor->sensor_instance.getAmount();
        result->t = sensor->sensor_instance.getTemp();
        result->ts = readout_index;

        digitalWrite(STATUS_LED_PIN, LOW);
      }
    }
  }

  if (Serial.available())
  {
    char line[128];
    size_t lineLength = Serial.readBytesUntil('\n', line, 127);
    line[lineLength] = '\0';

    char response[DBGCommandParser::MAX_RESPONSE_SIZE];
    debug_command_parser.processCommand(line, response);
    Serial.println(response);
  }



}