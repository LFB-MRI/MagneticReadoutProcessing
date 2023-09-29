#include "baseSensor.h"

baseSensor::baseSensor()
{
}

/*

      Tlv493d_Address_t addr = Tlv493d_Address::TLV493D_ADDRESS1;
        Adafruit_MMC5603* mmc = nullptr; //Adafruit_MMC5603(12345);

        Tlv493d* tlv493d_instance = nullptr;

*/
bool baseSensor::begin(TwoWire &_wire_instance)
{   
    i2c_inst = _wire_instance;
    //AVOID ERRORS DUE TO CALL BEGIN AGAIN
    if(tlv493d_instance){
        delete tlv493d_instance;
    }

    if(mmc){
        delete mmc;
    }
    // scan for sensors
    if (is_i2c_device_present(i2c_inst, ImplementedSensors::TLV493D))
    {
        found_sensor = ImplementedSensors::TLV493D;
        addr = Tlv493d_Address::TLV493D_ADDRESS1;
        tlv493d_instance = new Tlv493d();
    }
    else if (is_i2c_device_present(i2c_inst, ImplementedSensors::TLV493D_ALT))
    {
        found_sensor = ImplementedSensors::TLV493D;
        addr = Tlv493d_Address::TLV493D_ADDRESS2;
        tlv493d_instance = new Tlv493d();
    }
    else if (is_i2c_device_present(i2c_inst, ImplementedSensors::MMC56X3))
    {
        found_sensor = ImplementedSensors::MMC56X3;
        Adafruit_MMC5603 *mmc = new Adafruit_MMC5603(); // Adafruit_MMC5603(12345);
        mmc->begin(ImplementedSensors::MMC56X3, i2c_inst);
        mmc->setDataRate(100);
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
    case ImplementedSensors::SIMULATED:
        return "SIMULATED";
    case ImplementedSensors::TLV493D:
        return "TLV493D";
    case ImplementedSensors::MMC56X3:
        return "MMC56X3";
    default:
        return "UNKNOWN";
    }
}

bool baseSensor::query_sensor()
{
    bool succ = false;
    switch (found_sensor)
    {
    case ImplementedSensors::SIMULATED:
        last_query_result.x = random(0, 100) / 100.0;
        last_query_result.y = random(0, 100) / 100.0;
        last_query_result.z = random(0, 100) / 100.0;
        last_query_result.b = 1.0 * sqrt(pow(static_cast<float>(last_query_result.x), 2) + pow(static_cast<float>(last_query_result.y), 2) + pow(static_cast<float>(last_query_result.z), 2));
        last_query_result.t = 25.0;
        succ = true;
        break;
    case ImplementedSensors::TLV493D:
        succ = (tlv493d_instance->updateData() & Tlv493d_Error_t::TLV493D_NO_ERROR);
        last_query_result.x = tlv493d_instance->getX();
        last_query_result.y = tlv493d_instance->getY();
        last_query_result.z = tlv493d_instance->getZ();
        last_query_result.b = tlv493d_instance->getAmount();
        last_query_result.t = tlv493d_instance->getTemp();
        break;
    case ImplementedSensors::MMC56X3:
        sensors_event_t event;
        succ = mmc->getEvent(&event);
        event.
        last_query_result.x =  event.magnetic.x;
        last_query_result.y =  event.magnetic.y;
        last_query_result.z =  event.magnetic.z;
        last_query_result.z = 1.0 * sqrt(pow(static_cast<float>(event.magnetic.x), 2) + pow(static_cast<float>(event.magnetic.y), 2) + pow(static_cast<float>(event.magnetic.z), 2));
        last_query_result.t = mmc->readTemperature();
        break;
    default:
        return false;
    }
}

sensor_result baseSensor::get_result()
{
}
