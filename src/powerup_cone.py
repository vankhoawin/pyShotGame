# powerup_cone.py

from powerup import Powerup
import pygame
from initialVariables import *
import math



class Powerup_Cone(Powerup):
    def __init__(self,x,y,time):
        Powerup.__init__(self,x,y)
        self._color = POWERUP_CONE_COLOR
        self._timer = POWERUP_CONE_EXPIRE_TIMER
        self._start = time
        self._type = 'CONE'
