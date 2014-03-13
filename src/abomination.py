# abomination.py

from monster import Monster
from initialVariables import *



class Abomination(Monster):
    def __init__(self,x,y):
        Monster.__init__(self,x,y,0,ABOM_RADIUS,ABOM_MOVE_SPEED)

        self._color = ABOM_COLOR
        self._hp = ABOM_HP
