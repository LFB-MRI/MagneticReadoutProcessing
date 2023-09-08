#ifndef __sync_timer_h__
#define __sync_timer_h__

#ifdef USING_PLATFORMIO
    #include <Arduino.h>
#endif

class sync_timer
{
public:
    sync_timer(const unsigned long _interval_ms, const bool _one_shot);

    void start(void);
    void stop(void);

    bool operator()();
    bool expired();
    void trigger_timer_expire();
    
private:
    unsigned long interval_ms;
    unsigned long start_timestamp;
    bool started;
    bool manual_expire;
    bool one_shot;
};

#endif