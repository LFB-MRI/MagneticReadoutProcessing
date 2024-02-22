#ifndef __ImplementedSensors_h__
#define __ImplementedSensors_h__

#include <Tlv493d.h>
#include <Adafruit_MMC56x3.h>

#define I2C_ADDR_INVALID -1
typedef enum ImplementedSensors{
    SIMULATED_START = 0,
    TLV493D,
    TLV493D_ALT,
    MMC56X3,
    SIMULATED_END

}ImplementedSensors_t;

const int IMPLEMENTED_SENSOR_COUNT = ImplementedSensors::SIMULATED_END+1;
const int ImplementedSensorsAddressLookup[IMPLEMENTED_SENSOR_COUNT] = {I2C_ADDR_INVALID,Tlv493d_Address::TLV493D_ADDRESS1, Tlv493d_Address::TLV493D_ADDRESS2, MMC56X3_DEFAULT_ADDRESS, I2C_ADDR_INVALID};
const String ImplementedSensors_STR[IMPLEMENTED_SENSOR_COUNT] = {"SIMULATED +","TLV493D_ADDRESS1", "TLV493D_ADDRESS2", "MMC56X3_DEFAULT_ADDRESS", "SIMULATED -"};

#endif