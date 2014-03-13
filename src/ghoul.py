# ghoul.py

from monster import Monster
import pygame
from initialVariables import *
import math
from random import randint



class Ghoul(Monster):
    def __init__(self,x,y):
        Monster.__init__(self,x,y,0,GHOUL_RADIUS,GHOUL_MOVE_SPEED)
        
        self._color = GHOUL_COLOR
        self._hp    = GHOUL_HP

    def change_angle(self, angle):
        if randint(1,5) > 2:
            self._angle = angle + 1/randint(1,3)
        else:
            self._angle = angle
        
    def update(self):
        self._speed += 1/randint(1,GHOUL_ACCELERATE)
        
        self.change_location(self.get_speed()*math.cos(self._angle),
                             self.get_speed()*math.sin(self._angle))
    
