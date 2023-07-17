""" Provides some misc functions like translate and other helper functions"""
import math


# https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)



def asCartesian(_rthetaphi: (float, float, float) = (None, None, None)) -> [float, float, float]:
    r = _rthetaphi[0]
    theta = _rthetaphi[1] #* math.pi / 180  # to radian
    phi = _rthetaphi[2] #* math.pi / 180
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)
    return [x, y, z]

def asCartesian_touple(_rthetaphi: (float, float, float) = (None, None, None)) -> (float, float, float):
    ret = asCartesian(_rthetaphi)
    return (ret[0], ret[1], ret[2])