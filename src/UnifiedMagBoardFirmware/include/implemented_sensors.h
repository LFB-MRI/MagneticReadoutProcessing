#ifndef __ImplementedSensors_h__
#define __ImplementedSensors_h__

#include <Tlv493d.h>
#include <Adafruit_MMC56x3.h>

typedef enum ImplementedSensors{
    SIMULATED = 0,
    TLV493D = Tlv493d_Address::TLV493D_ADDRESS1,
    TLV493D_ALT = Tlv493d_Address::TLV493D_ADDRESS2,
    MMC56X3 = MMC56X3_DEFAULT_ADDRESS
}ImplementedSensors_t;

#endif