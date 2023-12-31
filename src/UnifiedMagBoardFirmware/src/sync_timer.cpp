#include "sync_timer.h"

sync_timer::sync_timer(const unsigned long _interval_ms, const bool _one_shot)
{
    one_shot = _one_shot;
    interval_ms = _interval_ms;
    start_timestamp = 0;
    started = false;
    manual_expire = false;
}

void sync_timer::trigger_timer_expire()
{
}

void sync_timer::start()
{
    start_timestamp = millis();
    started = true;
}

void sync_timer::stop()
{
    start_timestamp = 0;
    started = false;
}

bool sync_timer::expired()
{
    const unsigned long current_time = millis();
    if (!started && !manual_expire)
    {
        return false;
    }
    else if (current_time - start_timestamp > interval_ms || manual_expire)
    {
        if (one_shot)
        {
            started = false;
        }
        else
        {
            start_timestamp = current_time;
        }


        if (manual_expire)
        {
            manual_expire = false;
        }
        return true;
    }
    return false;
}

bool sync_timer::operator()()
{
    return expired();
}
