""" Provides some misc functions like translate and other helper functions"""
import math
import numpy as np
import vector



def normalize_3d_vector(_vector: vector.obj) -> vector.obj:

    vmag = _vector.mag

    if vmag == 0.0:
        return vector.obj(x=0.0, y=0.0, z=0.0)

    return vector.obj(x=_vector.x/vmag, y=_vector.y/vmag, z=_vector.z/vmag)

def is_np_shape_allowed(_arr, _shape:[int]):
  return _arr.shape != (_shape[0], ) and len(_arr.shape) <= _shape[1]


# https://gist.github.com/pghazanfari/8ff2c5c84544bae466191f7f674491b6
def perspective_fov(fov, aspect_ratio, near_plane, far_plane):
    num = 1.0 / np.tan(fov / 2.0)
    num9 = num / aspect_ratio
    return np.array([
        [num9, 0.0, 0.0, 0.0],
        [0.0, num, 0.0, 0.0],
        [0.0, 0.0, far_plane / (near_plane - far_plane), -1.0],
        [0.0, 0.0, (near_plane * far_plane) / (near_plane - far_plane), 0.0]
    ])


def look_at(camera_position, camera_target, up_vector):
    vector = camera_target - camera_position
    vector = vector / np.linalg.norm(vector)

    vector2 = np.cross(up_vector, vector)
    vector2 = vector2 / np.linalg.norm(vector2)

    vector3 = np.cross(vector, vector2)
    return np.array([
        [vector2[0], vector3[0], vector[0], 0.0],
        [vector2[1], vector3[1], vector[1], 0.0],
        [vector2[2], vector3[2], vector[2], 0.0],
        [-np.dot(vector2, camera_position), -np.dot(vector3, camera_position), np.dot(vector, camera_position), 1.0]
    ])


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
    theta = math.degrees(_rthetaphi[1]) * math.pi / 180  # to radian
    phi = math.degrees(_rthetaphi[2]) * math.pi / 180
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)
    return [x, y, z]


def asCartesian_degree(_rthetaphi: (float, float, float) = (None, None, None)) -> [float, float, float]:
    r = _rthetaphi[0]
    theta = _rthetaphi[1] * math.pi / 180  # to radian
    phi = _rthetaphi[2] * math.pi / 180
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)
    return [x, y, z]


def asCartesian_touple(_rthetaphi: (float, float, float) = (None, None, None)) -> (float, float, float):
    ret = asCartesian(_rthetaphi)
    return (ret[0], ret[1], ret[2])
