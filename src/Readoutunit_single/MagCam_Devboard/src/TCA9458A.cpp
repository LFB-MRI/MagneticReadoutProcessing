#include "TCA9458A.h"


TCA9548A::TCA9548A(TwoWire& _wire_instance) 
{
    i2c_inst = &_wire_instance;
}

bool TCA9548A::begin(const TCA9548A_Address_t _addr)
{
    //... toggle reset pin ? 
    i2c_addr = _addr;
    return isReady();
}

bool TCA9548A::isReady()
{
    i2c_inst->beginTransmission(i2c_addr);
    if (i2c_inst->endTransmission()== 0){ 
        return true;
    }else{
        return false;
    }
}



bool TCA9548A::setChannel(const byte _channel,const bool _state)
{

    activated_channels[_channel] = _state;
   


    if (_channel < TCA9548A_Channels)
    {
    i2c_inst->beginTransmission(i2c_addr);
    i2c_inst->write(1 << _channel);
    i2c_inst->endTransmission();
    return true;
    }
    else return false;
}

void TCA9548A::resetChannels()
{
    for (int i = 0; i < TCA9548A_Channels; i++)
    {
       setChannel(i, false);
    }
    
    //TODO REMOVE
    i2c_inst->beginTransmission(i2c_addr);
    i2c_inst->write(0x00);
    i2c_inst->endTransmission();
}


byte TCA9548A::getChannel()
{
    byte inByte;
    byte z = 0;

    i2c_inst->requestFrom(int(i2c_addr), 1);
    while (i2c_inst->available() == 0);
    inByte = (i2c_inst->read());
    if (inByte == 0) return 255;
    else
    {
    while (inByte > 1)
    {
        inByte = (inByte >> 1);
        z++;
    }
    }
    return z;
}





