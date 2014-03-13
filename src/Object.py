# objects.py

import math
from initialVariables import *



class Object:
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def get_radius(self):
        return int(self._radius)
        
    def get_location(self):
        return (int(self._x), int(self._y))
    
    def change_location(self,dx,dy):
        self._x += dx
        self._y += dy
    
    def angle_between_points(p1, p2):
        x = p1[0] - p2[0]
        y = p1[1] - p2[1]
        return math.atan2(y,x) - math.pi

    def contains(self, s):
        distance = math.sqrt((self._x-s._x)**2 + (self._y-s._y)**2)
        return distance <= (self._radius+s._radius)

    def update(self):
        self.change_location(self.get_speed()*math.cos(self._angle),
                             self.get_speed()*math.sin(self._angle))

    def display(self):
        pygame.draw.circle(screen, self.get_color(),
                           self.get_location(), self.get_radius())

    
