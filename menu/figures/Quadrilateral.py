from math import cos, sin
from figures.Vertex import Vertex
import pygame

class Quadrilateral:
    def __init__(self, vertex_a, vertex_b, vertex_c, vertex_d, center, screen):
        self._vertex_a = vertex_a
        self._vertex_b = vertex_b
        self._vertex_c = vertex_c
        self._vertex_d = vertex_d
        self._center = center
        self.screen = screen

    def rotate(self):
        grades = 1.5708
        self.vertex_a = self.rotate_vertex(self.vertex_a.x-self.center.x, self.vertex_a.y-self.center.y, grades)
        self.vertex_b = self.rotate_vertex(self.vertex_b.x-self.center.x, self.vertex_b.y-self.center.y, grades)
        self.vertex_c = self.rotate_vertex(self.vertex_c.x-self.center.x, self.vertex_c.y-self.center.y, grades)
        self.vertex_d = self.rotate_vertex(self.vertex_d.x - self.center.x, self.vertex_d.y - self.center.y, grades)

    def rotate_vertex(self, x, y, alpha):
        new_y = x*sin(alpha) + y*cos(alpha)
        new_x = x*cos(alpha) - y*sin(alpha)
        return Vertex([new_x+self.center.x, new_y+self.center.y])

    def draw(self):
        pygame.draw.polygon(self.screen, (0, 255, 0), (self.vertex_a.vertex, self.vertex_b.vertex, self.vertex_c.vertex, self.vertex_d.vertex))

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
