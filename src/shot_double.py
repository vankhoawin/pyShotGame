# shot_double.py

from shot import Shot
import pygame
from initialVariables import *



class Shot_Double(Shot):
    def __init__(self,x,y,angle,time):
        Shot.__init__(self,x,y,angle)

        self._start = time
        self._speed  = SHOT_DOUBLE_MOVE_SPEED
        self._radius = SHOT_DOUBLE_RADIUS
        self._color  = SHOT_DOUBLE_COLOR
        
