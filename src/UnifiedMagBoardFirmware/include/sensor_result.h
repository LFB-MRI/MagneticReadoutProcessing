#ifndef SENSOR_RESULT_H_INCLUDED
#define SENSOR_RESULT_H_INCLUDED

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
};


#endif