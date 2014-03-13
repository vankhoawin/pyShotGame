# monster.py

from mobileObject import mobileObject
import pygame
from initialVariables import *
import math

class Monster(mobileObject):
    def __init__(self,x,y,angle,radius,speed):
        mobileObject.__init__(self,x,y,angle,radius,speed)
        self._color = (0,0,0)
        self._hp = 1

    def change_angle(self, angle):
        self._angle = angle
    
    def get_hp(self):
        return self._hp

    def damage_hp(self):
        self._hp -= 1
