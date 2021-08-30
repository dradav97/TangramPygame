class Vertex:
    def __init__(self, vertex):

        self.vertex = vertex

    @property
    def x(self):
        return self.vertex[0]

    @property
    def y(self):
        return self.vertex[1]

    @property
    def vertex(self):
        return self.vertex

    @x.setter
    def x(self, value):
        self.vertex[0] = value

    @y.setter
    def y(self, value):
        self.vertex[1] = value

    @vertex.setter
    def vertex(self, new_vertex):
        self.vertex = new_vertex
