#ifndef __sensor_info_h__
#define __sensor_info_h__
#include "baseSensor.h"

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