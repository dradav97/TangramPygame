
class Triangle:

    def __init__(self, height, base, side_ab, side_ac, side_bc, vertex_a, vertex_b, vertex_c):
        self.height = height
        self.base = base
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.vertex_c = vertex_c
        self.side_ab = side_ab
        self.side_ac = side_ac
        self.side_bc = side_bc

    def rotate(self, grades):
        pass

    @property
    def height(self):
        return self.height

    @property
    def base(self):
        return self.base

    @property
    def vertex_a(self):
        return self.vertex_a

    @property
    def vertex_b(self):
        return self.vertex_b

    @property
    def vertex_c(self):
        return self.vertex_c

    @property
    def side_ab(self):
        return self.side_ab

    @property
    def side_ac(self):
        return self.side_ac

    @property
    def side_bc(self):
        return self.side_bc

    @height.setter
    def height(self, value):
        self.height = value

    @base.setter
    def base(self, value):
        self._base = value

    @vertex_a.setter
    def vertex_a(self, value):
        self._vertex_a = value

    @side_ab.setter
    def side_ab(self, value):
        self.side_ab = value

    @side_ac.setter
    def side_ac(self, value):
        self.side_ac = value

    @side_bc.setter
    def side_bc(self, value):
        self.side_bc = value

    @vertex_b.setter
    def vertex_b(self, value):
        self.vertex_b = value

    @vertex_c.setter
    def vertex_c(self, value):
        self.vertex_c = value
