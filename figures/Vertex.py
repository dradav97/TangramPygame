class Vertex:
    def __init__(self, vertex):

        self._vertex = vertex

    @property
    def x(self):
        return self._vertex[0]

    @property
    def y(self):
        return self._vertex[1]

    @property
    def vertex(self):
        return self._vertex

    @x.setter
    def x(self, value):
        self._vertex[0] = value

    @y.setter
    def y(self, value):
        self._vertex[1] = value

    @vertex.setter
    def vertex(self, new_vertex):
        self._vertex = new_vertex
