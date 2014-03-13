# shot.py

import pygame
from Object import Object
import math
from initialVariables import *


class mobileObject(Object):
    def __init__(self,x,y,angle,radius,speed):
        Object.__init__(self,x,y,radius)
        self._angle = angle
        self._speed = speed
        self._color = (0,0,0)

    def get_color(self):
        return self._color

    def get_angle(self):
        return self._angle

    def get_speed(self):
        return self._speed

    
