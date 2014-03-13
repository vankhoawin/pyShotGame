# powerup.py

from Object import Object
import pygame
from initialVariables import *
import math



class Powerup(Object):
    def __init__(self,x,y):
        Object.__init__(self,x,y,POWERUP_RADIUS)
        self._color = (0,0,0)
        self._timer = 10
        self._type = 'BASIC'
        
    def get_color(self):
        return self._color

    def get_type(self):
        return self._type

    def timer_expire(self, time):
        return (time - self._start >= self._timer)

    def update(self):
        pass

    def display(self):
        pygame.draw.circle(screen, self.get_color(), self.get_location(),
                           self.get_radius(), int(self.get_radius()*.9))
