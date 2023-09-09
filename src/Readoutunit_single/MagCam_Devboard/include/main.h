#ifndef __main_h__
#define __main_h__

#include "plattform.h"
#include "version.h"

#ifdef USING_PLATFORMIO
    #include <Arduino.h>
#endif

// PRIVATE LIBS
#include <Tlv493d.h>
#include <CommandParser.h>
#include "ArduinoUniqueID.h"



// PRIVATE CLASSES
#include "TCA9458A.h"
#include "sync_timer.h"



#define READOUT_SPEED_IN_SINGLEMODE_HZ 100 // Hz
#define READOUT_SPEED_IN_SINGLEMODE_DELAY (1000/READOUT_SPEED_IN_SINGLEMODE_HZ)


#define MAX_TLV_SENSORS (TCA9548A_Channels * 2) // each TLV493d can have two possible addresses and the i2c multiplexer has 8 channels


typedef CommandParser<> DBGCommandParser;
typedef CommandParser<> HostCommandParser;
typedef enum System_Error_Code{
    System_Error_Code_TCA_SCAN_FAILED = 1,
    System_Error_Code_TLV_NO_SENSORS_FOUND = 2,
    System_Error_Code_UNKNWON = 3,
}System_Error_Code_t;

const String System_Error_Code_STR[3] = {
    "System_Error_Code_TCA_SCAN_FAILED",
    "System_Error_Code_TLV_NO_SENSORS_FOUND",
    "System_Error_Code_UNKNWON"
};


typedef enum System_State{
    System_State_Error = 0,
    System_State_SETUP = 1,
    System_State_WAIT_FOR_ANC = 2,
    System_State_ANC_GOT_SYNC_PACKET = 3,
    System_State_READOUT_LOOP = 4,
}System_State_t;

const String System_State_STR[5] = {
    "System_State_Error",
    "System_State_SETUP",
    "System_State_WAIT_FOR_ANC",
    "System_State_ANC_GOT_SYNC_PACKET",
    "System_State_READOUT_LOOP"
};


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
    float t;
    long ts;

    sensor_result(){

    };
}sensor_result_t;




#endif