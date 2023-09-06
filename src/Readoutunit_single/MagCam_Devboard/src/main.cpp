#ifdef USING_PLATFORMIO
#include <Arduino.h>
#endif

#include <Wire.h>

// CUSTOM INCLUDES
#include "main.h"

// CLASSES
TCA9548A tca9584a(SENSOR_WIRE);


HardwareSerial Serial1(PA3, PA2); // RX TX  // FOR SERIAL ANC
sync_timer readout_timer(1000, false);


long readout_index = 0;
int sensor_number = 0;
sensor_info sensors_found[MAX_TLV_SENSORS] = {sensor_info()}; // TWO POSSIBLE SENSORS PER TCA CHANNEL S0 16 SENSORS PER SLICE
sensor_result sensor_results[MAX_TLV_SENSORS] = {sensor_result()};
System_State system_state = System_State_Error;


bool i2c_scan(TwoWire &_wire_instance, int _check_for_addr = -1, bool _log = true)
{
  byte error, address;
  int nDevices;

  if (_log)
  {
    Serial.println("Scanning...");
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
        Serial.print("I2C device found at address 0x");
        if (address < 16)
          Serial.print("0");
        Serial.print(address, HEX);
        Serial.println("  !");

        nDevices++;
      }
      else if (error == 4)
      {
        Serial.print("Unknown error at address 0x");
        if (address < 16)
          Serial.print("0");
        Serial.println(address, HEX);
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
      Serial.println("No I2C devices found\n");
    }
    else
    {
      Serial.println("done\n");
    }
  }

  return addr_found;
}

void error(const bool _critical, const int _code)
{
  pinMode(error_led, OUTPUT);
  while (_critical)
  {
    for (int i = 0; i < _code; i++)
    {
      digitalWrite(error_led, 1);
      delay(100);
      digitalWrite(error_led, 0);
      delay(100);
    }
    delay(1000);

    Serial.println("error:" + System_Error_Code_STR[_code]);
  }
}

bool is_i2c_device_present(TwoWire &_i2c_interface, byte _addr)
{
  return i2c_scan(_i2c_interface, _addr, false);
}

void setup()
{
  system_state = System_State_SETUP;

  Serial.begin(115200);
  Serial.println("setup");

  
  SENSOR_WIRE.setSCL(SENSOR_WIRE_SCL_PIN);
  SENSOR_WIRE.setSDA(SENSOR_WIRE_SDA_PIN);
  SENSOR_WIRE.begin();

  i2c_scan(SENSOR_WIRE);
  // CHECK IF TCA9584A IS PRESENT
  if (!is_i2c_device_present(SENSOR_WIRE, TCA9548A_ADDRESS0))
  {
    error(true, System_Error_Code_TCA_SCAN_FAILED);
  }
  tca9584a.begin(TCA9548A_ADDRESS0);

  // SCAN FOR TLV SENSORS
  bool found = false;

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
  volatile int ii = 0;

  
  system_state = System_State_READOUT_LOOP;
}

void loop()
{
  // HANDLE SYSTEM STATE
  // IMPLEMENT IRQ

  // TRIGGER READOUT
  if (readout_timer.expired())
  {
    for (int i = 0; i < sensor_number; i++)
    {
      sensor_info *sensor = &sensors_found[i];
      tca9584a.setChannel(sensor->tca_channel, true);
      sensor->sensor_instance.updateData();
      tca9584a.setChannel(sensor->tca_channel, false);
    }
    readout_index++;
  }

  // READ RESULT
  for (int i = 0; i < sensor_number; i++)
  {
    sensor_info *sensor = &sensors_found[i];
    sensor_result *result = &sensor_results[i];

    tca9584a.setChannel(sensor->tca_channel, true);
    result->x = sensor->sensor_instance.getX();
    result->y = sensor->sensor_instance.getY();
    result->z = sensor->sensor_instance.getZ();
    result->b = sensor->sensor_instance.getAmount();
    result->ts = readout_index;
    tca9584a.setChannel(sensor->tca_channel, false);

    Serial.println(result->b);
  }

  delay(10);
}