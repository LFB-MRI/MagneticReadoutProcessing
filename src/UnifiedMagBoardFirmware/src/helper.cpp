#include "helper.h"

bool i2c_scan(TwoWire &_wire_instance, const int _check_for_addr = -1, const bool _log = true)
{
  byte error, address;
  int nDevices;

  if (_log)
  {
    DEBUG_SERIAL.println("Scanning...");
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
        DEBUG_SERIAL.print("I2C device found at address 0x");
        if (address < 16)
        {
          DEBUG_SERIAL.print("0");
        }
        DEBUG_SERIAL.print(address, HEX);
        DEBUG_SERIAL.println("  !");

        nDevices++;
      }
      else if (error == 4)
      {
        DEBUG_SERIAL.print("Unknown error at address 0x");
        if (address < 16)
        {
          DEBUG_SERIAL.print("0");
        }
        DEBUG_SERIAL.println(address, HEX);
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
      DEBUG_SERIAL.println("No I2C devices found\n");
    }
    else
    {
      DEBUG_SERIAL.println("done\n");
    }
  }

  return addr_found;
}


bool is_i2c_device_present(TwoWire &_i2c_interface, const byte _addr)
{
  return i2c_scan(_i2c_interface, _addr, false);
}
