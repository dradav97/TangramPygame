from math import cos, sin
from figures.Vertex import Vertex

class Triangle:

    def __init__(self, height, base, side_ab, side_ac, side_bc, vertex_a, vertex_b, vertex_c, center):
        self._height = height
        self._base = base
        self._vertex_a = vertex_a
        self._vertex_b = vertex_b
        self._vertex_c = vertex_c
        self._side_ab = side_ab
        self._side_ac = side_ac
        self._side_bc = side_bc
        self._center = center

    def rotate(self, grades):
        self.vertex_a = self.rotate_vertex(self.vertex_a.x-self.center.x, self.vertex_a.y-self.center.y, grades)
        self.vertex_b = self.rotate_vertex(self.vertex_b.x-self.center.x, self.vertex_b.y-self.center.y, grades)
        self.vertex_c = self.rotate_vertex(self.vertex_c.x-self.center.x, self.vertex_c.y-self.center.y, grades)

    def rotate_vertex(self, x, y, alpha):
        new_y = x*sin(alpha) + y*cos(alpha)
        new_x = x*cos(alpha) - y*sin(alpha)
        return Vertex([new_x+self.center.x, new_y+self.center.y])

    @property
    def height(self):
        return self._height

    @property
    def base(self):
        return self._base

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
    def side_ab(self):
        return self._side_ab

    @property
    def side_ac(self):
        return self._side_ac

    @property
    def side_bc(self):
        return self._side_bc

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        self._center = value

    @height.setter
    def height(self, value):
        self._height = value

    @base.setter
    def base(self, value):
        self._base = value

    @vertex_a.setter
    def vertex_a(self, value):
        self._vertex_a = value

    @side_ab.setter
    def side_ab(self, value):
        self._side_ab = value

    @side_ac.setter
    def side_ac(self, value):
        self._side_ac = value

    @side_bc.setter
    def side_bc(self, value):
        self._side_bc = value

    @vertex_b.setter
    def vertex_b(self, value):
        self._vertex_b = value

    @vertex_c.setter
    def vertex_c(self, value):
        self._vertex_c = value
