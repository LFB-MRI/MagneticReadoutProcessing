#ifndef __baseSensor_h__
#define __baseSensor_h__


#ifdef USING_PLATFORMIO
    #include "Arduino.h"
#endif

#include "Wire.h"


// PRIVATE LIBS
#include <Tlv493d.h>
#include <Adafruit_MMC56x3.h>


//CUSTOM CLASSES
//
#include "usf_plattform.h"
#include "sensor_result.h"
#include "implemented_sensors.h"



class baseSensor
{
public:
        

    baseSensor();
    bool begin(TwoWire &_wire_instance);
    bool is_valid();
    String capabilities();
    String get_sensor_name();
    bool query_sensor();
    sensor_result get_result();

    

    private:
        TwoWire* i2c_inst;
        ImplementedSensors found_sensor = ImplementedSensors::SIMULATED;
        sensor_result last_query_result;
        //POSSIBLE FOUND SENSOR INSTANCES HERE
        Tlv493d_Address_t addr = Tlv493d_Address::TLV493D_ADDRESS1;
        Adafruit_MMC5603* mmc = nullptr; //Adafruit_MMC5603(12345);
        
        Tlv493d* tlv493d_instance = nullptr;
        
};


#endif