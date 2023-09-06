#ifndef __main_h__
#define __main_h__

#ifdef USING_PLATFORMIO
    #include <Arduino.h>
#endif

// PRIVATE LIBS
#include <Tlv493d.h>

// PRIVATE CLASSES
#include "TCA9458A.h"
#include "sync_timer.h"


#define ERROR_LED_PIN PD15

#define SENSOR_WIRE_SCL_PIN PB6
#define SENSOR_WIRE_SDA_PIN PB9
#define SENSOR_WIRE Wire


#define MAX_TLV_SENSORS (TCA9548A_Channels * 2)


typedef enum System_Error_Code{
    System_Error_Code_TCA_SCAN_FAILED = 1,
    System_Error_Code_TLV_NO_SENSORS_FOUND = 2,
    System_Error_Code_UNKNWON = 3,
}System_Error_Code_t;

String System_Error_Code_STR[2] = {
    "System_Error_Code_TCA_SCAN_FAILED",
    "System_Error_Code_TLV_NO_SENSORS_FOUND",
    "System_Error_Code_UNKNWON"
};


typedef enum System_State{
    System_State_Error = 0,
    System_State_SETUP = 1,
    System_State_WAIT_FOR_ANC = 2,
    System_State_READOUT_LOOP = 3,
}System_State_t;



struct sensor_info{
    
    Tlv493d_Address_t addr = Tlv493d_Address::TLV493D_ADDRESS1;
    int index = -1;
    int tca_channel = 0;
    bool valid = false;
    Tlv493d sensor_instance;

    sensor_info(){
        valid = false;
    };
} sensor_info_t;


struct sensor_result{
    float x;
    float y;
    float z;
    float b;
    long ts;

    sensor_result(){

    };
}sensor_result_t;
#endif