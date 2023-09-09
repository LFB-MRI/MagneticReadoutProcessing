#ifndef __plattform_h__
#define __plattform_h__


    #ifdef IS_STM32F4_BOARD
        #define GENERAL_SERIAL_SPEED 115200

        #define ERROR_LED_PIN PD15
        #define STATUS_LED_PIN PD14
        #define SINGLE_MODE_PIN PC1
        #define SYNC_PIN
        
        //I2C INTERFACE TO COMMUNICATE WITH ATTACHED SENSORS
        #define SENSOR_WIRE_SCL_PIN PB6
        #define SENSOR_WIRE_SDA_PIN PB9
        #define SENSOR_WIRE Wire

        // SERIAL PORT FOR DEBUGGING
        #define DEBUG_SERIAL Serial  //ON STM32F4 WITH USB SUPPORT => Serial = USB CDC SERIAL
        //SERIAL PINS FOR COMMUNICATING WITH HOST FOR ANC NUMBERING
        #define HOST_SERIAL_RX PA3
        #define HOST_SERIAL_TX PA2
        #define HOST_SERIAL Serial1
    #endif

#endif