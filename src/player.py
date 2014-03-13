# player.py

from Object import Object
import pygame
from initialVariables import *
import math



class Player(Object):
    def __init__(self,x,y):
        Object.__init__(self,x,y,PLAYER_RADIUS)
        self._color = PLAYER_COLOR

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y
        
    def change_x(self,dx):
        self._x += dx

    def change_y(self,dy):
        self._y += dy

    def get_color(self):
        return self._color

    def update(self):
        pass
