#ifndef __TCA9548A_h__
#define __TCA9548A_h__

#ifdef USING_PLATFORMIO
    #include "Arduino.h"
#endif


#include "Wire.h"

#define TCA9548A_Channels 8

typedef enum TCA9548A_Address{
    TCA9548A_ADDRESS0	=	0x70,
    TCA9548A_ADDRESS1	=	0x71,
    TCA9548A_ADDRESS2	=	0x72,
    TCA9548A_ADDRESS3	=	0x73,
    TCA9548A_ADDRESS4	=	0x74,
    TCA9548A_ADDRESS5	=	0x75,
    TCA9548A_ADDRESS6	=	0x76,
    TCA9548A_ADDRESS7	=	0x77
}TCA9548A_Address_t;



class TCA9548A
{
    public:
        

        TCA9548A(TwoWire& _wire_instance);
        bool begin(const TCA9548A_Address_t _addr);
        bool isReady(void);
        bool setChannel(const byte _channel, const bool _state);
        void resetChannels(void);
        byte getChannel(void);
  						 
    private:
       TCA9548A_Address_t i2c_addr = TCA9548A_ADDRESS0;
        TwoWire* i2c_inst;
        
       bool activated_channels[TCA9548A_Channels] = { false };
};

#endif