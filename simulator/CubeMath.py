from Cell import *
from Tuple3d import *
import math

''' For the following math, please take a look
 at the rotation matrix mentioned here:
 https://en.m.wikipedia.org/wiki/Transformation_matrix#Rotation_2
 It should clear up, where the formulars come from
'''


def rotateZAxis(v: Tuple3d, radians: float) -> Tuple3d:
    # x' = x*cosθ - y*sinθ
    x = int(round(v.x * math.cos(radians) - v.y * math.sin(radians)))
    # y' = x*sinθ + y*cosθ
    y = int(round(v.x * math.sin(radians) + v.y * math.cos(radians)))
    # z' = z
    z = int(v.z)
    return Tuple3d(x, y, z)


def rotateYAxis(v: Tuple3d, radians: float) -> Tuple3d:
    # x' = x*cosθ + z*sinθ
    x = int(round(v.x * math.cos(radians) + v.z * math.sin(radians)))
    # y' = y
    y = int(v.y)
    # z' = -x*sinθ + z*cosθ
    z = int(round(-v.x * math.sin(radians) + v.z * math.cos(radians)))
    return Tuple3d(x, y, z)


def rotateXAxis(v: Tuple3d, radians: float) -> Tuple3d:
    # x' = x
    x = int(v.x)
    # y' = y*cosθ - z*sinθ
    y = int(round(v.y * math.cos(radians) - v.z * math.sin(radians)))
    # z' = y*sinθ + z*cosθ
    z = int(round(v.y * math.sin(radians) + v.z * math.cos(radians)))
    return Tuple3d(x, y, z)


def rotateNode(c: Cell, rotator: "Rotation function", radians: float):
    c.setLocation(rotator(c.getLocation(), radians))
    c.setNormal(rotator(c.getNormal(), radians))
