import sys
import pygame
from figures.Triangle import Triangle
from figures.Vertex import Vertex
from figures.Quadrilateral import Quadrilateral



pygame.init()
size = (800, 700)
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VIOLET = (125, 125, 125)
alfa = 0
clock = pygame.time.Clock()
# (self, height, base, side_ab, side_ac, side_bc, vertex_a, vertex_b, vertex_c, center):

t = Triangle(Vertex([100, 500]), Vertex([700, 500]), Vertex([400, 100]), Vertex([400, 350]), screen)

c = Quadrilateral(Vertex([10, 30]), Vertex([10, 80]), Vertex([90, 80]), Vertex([90, 30]), Vertex([10, 30]), screen)

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        # print(event) podemoa imprimir todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()
    # Aqui dibujamos
    # pygame.draw.polygon(screen, BLACK, [A, B, C, D], 2)
    # pygame.draw.polygon(screen, (0,255,0), (t.vertex_a.vertex, t.vertex_b.vertex , t.vertex_c.vertex ), 2)

    c.draw()
    #pygame.draw.polygon((screen), (0, 255, 0), (c.vertex_a.vertex, c.vertex_b.vertex, c.vertex_c.vertex, c.vertex_d.vertex))
    c.move_l
    g = -0.00172
    #c.rotate(g)

    clock.tick(80)

    # Aqui dibujamos
    pygame.display.flip()
