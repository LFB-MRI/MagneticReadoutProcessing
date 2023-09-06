#include "sync_timer.h"

sync_timer::sync_timer(const unsigned long _interval_ms, const bool _one_shot)
{
    one_shot = _one_shot;
    interval_ms = _interval_ms;
    start_timestamp = 0;
    started = false;
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
    if (!started)
    {
        return false;
    }
    else if (current_time - start_timestamp > interval_ms)
    {
        if (!one_shot)
        {
            started = false;
        }
        else
        {
            start_timestamp = current_time;
        }
        return true;
    }
    return false;
}

bool sync_timer::operator()()
{
    return expired();
}
