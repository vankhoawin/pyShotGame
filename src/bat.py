# bat.py

from monster import Monster
import pygame
from initialVariables import *
from random import choice


class Bat(Monster):
    def __init__(self,x,y):
        Monster.__init__(self,x,y,0,BAT_RADIUS,BAT_MOVE_SPEED)

        self._color = BAT_COLOR
        self._hp    = BAT_HP
        self._timer = BAT_TIMER
        self._base_speed = self._speed
        self._boost = self._speed * BAT_BOOST_SPEED
        self._randangle = choice([1,-1])

    def change_angle(self, angle):
        
        if (pygame.time.get_ticks()/1000 % self._timer) == 0.0:
            self._speed = self._boost
            self._angle = angle + (0.8*self._randangle)
        else:
            self._speed = self._base_speed
            self._angle = angle        
