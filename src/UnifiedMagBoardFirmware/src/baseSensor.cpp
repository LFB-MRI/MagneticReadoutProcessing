#include "baseSensor.h"
#include "helper.h"
baseSensor::baseSensor()
{
}


bool baseSensor::begin(TwoWire &_wire_instance, ImplementedSensors _sensor){
    this->i2c_inst = &_wire_instance;
    //AVOID ERRORS DUE TO CALL BEGIN AGAIN
    if(tlv493d_instance){
        delete tlv493d_instance;
    }

    if(this->mmc){
        delete this->mmc;
    }

    found_sensor = _sensor;
    const int sensor_i2c_addr = ImplementedSensorsAddressLookup[_sensor];


    // scan for sensors
    if (_sensor == ImplementedSensors::TLV493D && is_i2c_device_present(_wire_instance, sensor_i2c_addr))
    {
        addr = Tlv493d_Address::TLV493D_ADDRESS1;
        tlv493d_instance = new Tlv493d();
        tlv493d_instance->begin(_wire_instance);
        return true;
    }
    else if (_sensor == ImplementedSensors::TLV493D_ALT && is_i2c_device_present(_wire_instance, sensor_i2c_addr))
    {
        addr = Tlv493d_Address::TLV493D_ADDRESS2;
        const bool reset = false;
        tlv493d_instance = new Tlv493d();
        tlv493d_instance->begin(_wire_instance, addr, reset);
        return true;
    }
    else if (_sensor == ImplementedSensors::MMC56X3 && is_i2c_device_present(_wire_instance, sensor_i2c_addr))
    {
        this->mmc = new Adafruit_MMC5603();
        this->mmc->begin(sensor_i2c_addr, i2c_inst);
        this->mmc->setDataRate(100);
        return true;
    }else if (_sensor == ImplementedSensors::SIMULATED_START || _sensor == ImplementedSensors::SIMULATED_END){
        return true;
    }else{
        return false;
    }
}


bool baseSensor::begin(TwoWire& _wire_instance)
{   
    this->i2c_inst = &_wire_instance;
    //AVOID ERRORS DUE TO CALL BEGIN AGAIN
    if(tlv493d_instance){
        delete tlv493d_instance;
    }

    if(this->mmc){
        delete this->mmc;
    }

    // scan for sensors
    if (is_i2c_device_present(_wire_instance, ImplementedSensorsAddressLookup[ImplementedSensors::TLV493D]))
    {
        found_sensor = ImplementedSensors::TLV493D;
        addr = Tlv493d_Address::TLV493D_ADDRESS1;
        tlv493d_instance = new Tlv493d();
        tlv493d_instance->begin(_wire_instance);
        return true;
    }
    //else if (is_i2c_device_present(_wire_instance, ImplementedSensors::TLV493D_ALT))
    //{
    //    found_sensor = ImplementedSensors::TLV493D;
    //    addr = Tlv493d_Address::TLV493D_ADDRESS2;
    //    const bool reset = false;
    //    tlv493d_instance = new Tlv493d();
    //    tlv493d_instance->begin(_wire_instance, addr, reset);
    //return true;
    //}
    else if (is_i2c_device_present(_wire_instance, ImplementedSensorsAddressLookup[ImplementedSensors::MMC56X3]))
    {
        found_sensor = ImplementedSensors::MMC56X3;
        this->mmc = new Adafruit_MMC5603();
        this->mmc->begin(ImplementedSensors::MMC56X3, i2c_inst);
        this->mmc->setDataRate(100);
        return true;
    }
    else
    {
        return false;
    }

    // init sensor instances
}

String baseSensor::capabilities()
{
}


String baseSensor::get_sensor_name()
{
    switch (found_sensor)
    {
    case ImplementedSensors::SIMULATED_START:
        return "SIMULATED [+uT]";
    case ImplementedSensors::SIMULATED_END:
        return "SIMULATED [-uT]";
    case ImplementedSensors::TLV493D:
        return "TLV493D [uT]";
    case ImplementedSensors::MMC56X3:
        return "MMC56X3 [uT]";
    default:
        return "UNKNOWN";
    }
}

bool baseSensor::query_sensor()
{
    bool succ = false;
    switch (found_sensor)
    {
    case ImplementedSensors::SIMULATED_START:
        last_query_result.x = random(0, 10000) / 10.0;
        last_query_result.y = random(0, 10000) / 10.0;
        last_query_result.z = random(0, 10000) / 10.0;
        last_query_result.b = 1.0 * sqrt(pow(static_cast<float>(last_query_result.x), 2) + pow(static_cast<float>(last_query_result.y), 2) + pow(static_cast<float>(last_query_result.z), 2));
        last_query_result.t = 25.0;
        succ = true;
        break;
    case ImplementedSensors::SIMULATED_END:
        last_query_result.x = random(0, 10000) / 10.0;
        last_query_result.y = random(0, 10000) / 10.0;
        last_query_result.z = random(0, 10000) / 10.0;
        last_query_result.b = -1.0 * sqrt(pow(static_cast<float>(last_query_result.x), 2) + pow(static_cast<float>(last_query_result.y), 2) + pow(static_cast<float>(last_query_result.z), 2));
        last_query_result.t = 25.0;
        succ = true;
        break;
    case ImplementedSensors::TLV493D:
        succ = (tlv493d_instance->updateData() & Tlv493d_Error_t::TLV493D_NO_ERROR);
        this->last_query_result.x = tlv493d_instance->getX() * 1000.0;
        this->last_query_result.y = tlv493d_instance->getY() * 1000.0;
        this->last_query_result.z = tlv493d_instance->getZ() * 1000.0;
        this->last_query_result.b = tlv493d_instance->getAmount() * 1000.0;
        this->last_query_result.t = tlv493d_instance->getTemp();
        break;
    case ImplementedSensors::MMC56X3:
        sensors_event_t event;
        succ = mmc->getEvent(&event);
        this->last_query_result.x =  event.magnetic.x;
        this->last_query_result.y =  event.magnetic.y;
        this->last_query_result.z =  event.magnetic.z;
        this->last_query_result.b = 1.0 * sqrt(pow(static_cast<float>(event.magnetic.x), 2) + pow(static_cast<float>(event.magnetic.y), 2) + pow(static_cast<float>(event.magnetic.z), 2));
        this->last_query_result.t = mmc->readTemperature();
        break;
    default:
        return false;
    }
    return succ;
}

sensor_result baseSensor::get_result()
{
    return this->last_query_result;
}
