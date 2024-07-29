#ifndef __main_h__
#define __main_h__

// VERSION INFORMATION
#include "version.h"
// PLATTFORM INFORMATION
#include "usf_plattform.h"


#ifdef USING_PLATFORMIO
    #include <Arduino.h>
#endif

// PRIVATE LIBS
#include <CommandParser.h>
#include "ArduinoUniqueID.h"



#ifdef ENABLE_HARDWARE_AVERAGING
#include <RingBuf.h>
#endif



#define READOUT_SPEED_IN_SINGLEMODE_DELAY (1000/READOUT_SPEED_IN_SINGLEMODE_HZ)



// PRIVATE CLASSES
//#include "baseSensor.h"
#include "sensor_info.h"
//#include "sensor_result.h"
#include "sync_timer.h"
#include "helper.h"
#include "TCA9458A.h"




#define MAX_TLV_SENSORS (TCA9548A_Channels * 2) // each TLV493d can have two possible addresses and the i2c multiplexer has 8 channels


typedef CommandParser<> DBGCommandParser;
typedef CommandParser<> HostCommandParser;
typedef enum System_Error_Code{
    System_Error_Code_TCA_SCAN_FAILED = 0,
    System_Error_Code_TLV_NO_SENSORS_FOUND = 1,
    System_Error_Code_UNKNWON = 2
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








#endif