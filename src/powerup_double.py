# powerup_double.py

from powerup import Powerup
import pygame
from initialVariables import *
import math



class Powerup_Double(Powerup):
    def __init__(self,x,y,time):
        Powerup.__init__(self,x,y)
        self._color = POWERUP_DOUBLE_COLOR
        self._timer = POWERUP_DOUBLE_EXPIRE_TIMER
        self._start = time
        self._type = 'DOUBLE'
