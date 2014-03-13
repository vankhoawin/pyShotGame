# zombie.py

from monster import Monster
from initialVariables import *



class Zombie(Monster):
    def __init__(self,x,y):
        Monster.__init__(self,x,y,0,ZOMBIE_RADIUS,ZOMBIE_MOVE_SPEED)

        self._color = ZOMBIE_COLOR
        self._hp    = ZOMBIE_HP

