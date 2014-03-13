# shot.py

from mobileObject import mobileObject
import pygame
from initialVariables import *



class Shot(mobileObject):
    def __init__(self,x,y,angle):
        mobileObject.__init__(self,x,y,angle,0,0)
        
        self._color = (255,255,255)
        self._start = 10
        self._timer = 10000

    def timer_expire(self, time):
        return (time - self._start >= self._timer)

        
