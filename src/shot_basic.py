# shot_basic.py

from shot import Shot
import pygame
from initialVariables import *



class Shot_Basic(Shot):
    def __init__(self,x,y,angle,time):
        Shot.__init__(self,x,y,angle)

        self._start = time
        self._speed  = SHOT_BASIC_MOVE_SPEED
        self._radius = SHOT_BASIC_RADIUS
        self._color  = SHOT_BASIC_COLOR
