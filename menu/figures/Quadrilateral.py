from math import cos, sin
from figures.Vertex import Vertex
import pygame
import random as rm
import math
from copy import deepcopy

class Quadrilateral:
    def __init__(self, vertex_a, vertex_b, vertex_c, vertex_d, center, screen, color, name):
        self.name = name
        self.origin_a = deepcopy(vertex_a)
        self.origin_b = deepcopy(vertex_b)
        self.origin_c = deepcopy(vertex_c)
        self.origin_d = deepcopy(vertex_d)
        self.origin_center = deepcopy(center)
        self._vertex_a = vertex_a
        self._vertex_b = vertex_b
        self._vertex_c = vertex_c
        self._vertex_d = vertex_d
        self._center = center
        self.screen = screen
        self.delta = 10
        self.range =5
        self.color = color
        self.pos_random()
        self.control= False

    def toOrigin(self):
        self._vertex_a.x = self.origin_a.x
        self._vertex_a.y = self.origin_a.y
        self._vertex_b.x = self.origin_b.x
        self._vertex_b.y = self.origin_b.y
        self._vertex_c.x = self.origin_c.x
        self._vertex_c.y = self.origin_c.y
        self._vertex_d.x = self.origin_d.x
        self._vertex_d.y = self.origin_d.y
        self._center.x = self.origin_center.x
        self._center.y = self.origin_center.y
    
    def draw(self):
        pygame.draw.polygon(self.screen, self.color, (self.vertex_a.vertex, self.vertex_b.vertex, self.vertex_c.vertex, self.vertex_d.vertex))

    def rotate(self):
        grades = 1.5708
        self.vertex_a = self.rotate_vertex(self.vertex_a.x-self.center.x, self.vertex_a.y-self.center.y, grades)
        self.vertex_b = self.rotate_vertex(self.vertex_b.x-self.center.x, self.vertex_b.y-self.center.y, grades)
        self.vertex_c = self.rotate_vertex(self.vertex_c.x-self.center.x, self.vertex_c.y-self.center.y, grades)
        self.vertex_d = self.rotate_vertex(self.vertex_d.x - self.center.x, self.vertex_d.y - self.center.y, grades)
    
    def toString(self):
        return str(self.vertex_a.x)+","+str(self.vertex_a.y)+"|"+str(self.vertex_b.x)+","+str(self.vertex_b.y)+"|"+str(self.vertex_c.x)+","+str(self.vertex_c.y)+"|"+str(self.vertex_d.x)+","+str(self.vertex_d.y)
            

    def rotate_vertex(self, x, y, alpha):
        new_y = x*sin(alpha) + y*cos(alpha)
        new_x = x*cos(alpha) - y*sin(alpha)
        return Vertex([new_x+self.center.x, new_y+self.center.y])

    def pos_random(self):
        rx = rm.randint(self.range*(-1), self.range) * self.delta
        ry = rm.randint(self.range*(-1), self.range) * self.delta
        #print(' '+str(rx)+'--'+str(ry))
        self._vertex_a.x = self.vertex_a.x + rx
        self._vertex_b.x = self.vertex_b.x + rx
        self._vertex_c.x = self.vertex_c.x + rx
        self._vertex_d.x = self.vertex_d.x + rx
        
        self._vertex_a.y = self.vertex_a.y + ry
        self._vertex_b.y = self.vertex_b.y + ry
        self._vertex_c.y = self.vertex_c.y + ry
        self._vertex_d.y = self.vertex_d.y + ry
        self.center = self.vertex_a
    @property
    def move_l(self):
        if self.vertex_a.x - self.delta>=0:
            self.vertex_a.x = self.vertex_a.x - self.delta
            self.vertex_b.x = self.vertex_b.x - self.delta
            self.vertex_c.x = self.vertex_c.x - self.delta
            self.vertex_d.x = self.vertex_d.x - self.delta

    @property
    def move_r(self):
        self.vertex_a.x = self.vertex_a.x + self.delta
        self.vertex_b.x = self.vertex_b.x + self.delta
        self.vertex_c.x = self.vertex_c.x + self.delta
        self.vertex_d.x = self.vertex_d.x + self.delta

    @property
    def move_u(self):
        self.vertex_a.y = self.vertex_a.y - self.delta
        self.vertex_b.y = self.vertex_b.y - self.delta
        self.vertex_c.y = self.vertex_c.y - self.delta
        self.vertex_d.y = self.vertex_d.y - self.delta

    @property
    def move_d(self):
        self.vertex_a.y = self.vertex_a.y + self.delta
        self.vertex_b.y = self.vertex_b.y + self.delta
        self.vertex_c.y = self.vertex_c.y + self.delta
        self.vertex_d.y = self.vertex_d.y + self.delta

    @property
    def vertex_a(self):
        return self._vertex_a

    @property
    def vertex_b(self):
        return self._vertex_b

    @property
    def vertex_c(self):
        return self._vertex_c

    @property
    def vertex_d(self):
        return self._vertex_d

    @property
    def center(self):
        return self._center
    
    @property
    def origincenter(self):
        return self.origin_center

    @vertex_a.setter
    def vertex_a(self, value):
        self._vertex_a = value

    @vertex_b.setter
    def vertex_b(self, value):
        self._vertex_b = value

    @vertex_c.setter
    def vertex_c(self, value):
        self._vertex_c = value

    @center.setter
    def center(self, value):
        self._center = value

    @vertex_d.setter
    def vertex_d(self, value):
        self._vertex_d = value
    
    def point_distance(self, point2):
        d = math.pow(math.pow((self.vertex_a[0]-point2[0]),2)+math.pow((self.vertex_a[0]-point2[0]),2))
        return d

