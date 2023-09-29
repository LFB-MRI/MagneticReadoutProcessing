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
#include "helper.h"
#include "usf_plattform.h"

typedef enum ImplementedSensors{
    SIMULATED = 0,
    TLV493D = Tlv493d_Address::TLV493D_ADDRESS1,
    TLV493D_ALT = Tlv493d_Address::TLV493D_ADDRESS2,
    MMC56X3 = MMC56X3_DEFAULT_ADDRESS
}ImplementedSensors_t;



struct sensor_result{
    float x;
    float y;
    float z;
    float b;
    float t;
    long ts;

    sensor_result(){

    };

    void set(sensor_result _other){
        this->x = _other.x;
        this->y = _other.y;
        this->z = _other.z;
        this->b = _other.b;
        this->t = _other.t;
        this->ts = _other.ts;
    };
}sensor_result_t;


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


struct sensor_info{

    
    int index = -1;
    int tca_channel = 0;
    bool valid = false;
    baseSensor sensor_instance = baseSensor();

    sensor_info(){
        valid = false;
    };
} sensor_info_t;

#endif