# shot_cone.py

from shot import Shot
import pygame
from initialVariables import *
import math



class Shot_Cone(Shot):
    def __init__(self,x,y,angle,time):
        Shot.__init__(self,x,y,angle)

        self._speed  = SHOT_CONE_MOVE_SPEED
        self._radius = SHOT_CONE_RADIUS
        self._color  = SHOT_CONE_COLOR
        self._start = time
        self._timer  = 0.20

    def update(self):
        self._radius += 0.5
        
        self.change_location(self.get_speed()*math.cos(self._angle),
                             self.get_speed()*math.sin(self._angle))
        
