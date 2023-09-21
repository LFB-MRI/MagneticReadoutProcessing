#ifdef USING_PLATFORMIO
#include <Arduino.h>
#endif

#include <Wire.h>

#include "usf_plattform.h"

bool is_i2c_device_present(TwoWire &_i2c_interface, const byte _addr);
bool i2c_scan(TwoWire &_wire_instance, const int _check_for_addr, const bool _log);