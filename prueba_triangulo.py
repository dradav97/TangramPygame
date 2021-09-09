import sys
from copy import deepcopy
import pygame

from figures.Quadrilateral import Quadrilateral
from figures.Triangle import Triangle
from figures.Vertex import Vertex
import numpy as np
pygame.init()
size = (800, 700)
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VIOLET = (125, 125, 125)
YELLOW = (200, 0, 200)
ORANGE = (200, 200, 0)
alfa = 0
clock = pygame.time.Clock()
# (self, height, base, side_ab, side_ac, side_bc, deepcopy_a, deepcopy_b, deepcopy_c, center):
"""
factor = 5
a = np.array([0, 0]) * factor
n = np.array([50, 0]) * factor
b = np.array([100, 0]) * factor
j = np.array([25, 25]) * factor
i = np.array([75, 25]) * factor
l = np.array([0, 50]) * factor
r = np.array([25, 50]) * factor
f = np.array([50, 50]) * factor
q = np.array([75, 50]) * factor
m = np.array([100, 50]) * factor
o = np.array([25, 75]) * factor
s = np.array([50, 75]) * factor
p = np.array([75, 75]) * factor
c = np.array([0, 100]) * factor
h = np.array([25, 100]) * factor
t = np.array([50, 100]) * factor
k = np.array([75, 100]) * factor
d = np.array([100, 100]) * factor

a = [0, 0]
n = [50, 0]
b = [100, 0]
j = [25, 25]
i = [75, 25]
l = [0, 50]
r = [25, 50]
f = [50, 50]
q = [75, 50]
m = [100, 50]
o = [25, 75]
s = [50, 75]
p = [75, 75]
c = [0, 100]
h = [25, 100]
t = [50, 100]
k = [75, 100]
d = [100, 100]
"""
#

factor = 5
a = Vertex(np.array([0, 0]) * factor)
n = Vertex(np.array([50, 0]) * factor)
b = Vertex(np.array([100, 0]) * factor)
j = Vertex(np.array([25, 25]) * factor)
i = Vertex(np.array([75, 25]) * factor)
l = Vertex(np.array([0, 50]) * factor)
r = Vertex(np.array([25, 50]) * factor)
f = Vertex(np.array([50, 50]) * factor)
q = Vertex(np.array([75, 50]) * factor)
m = Vertex(np.array([100, 50]) * factor)
o = Vertex(np.array([25, 75]) * factor)
s = Vertex(np.array([50, 75]) * factor)
p = Vertex(np.array([75, 75]) * factor)
c = Vertex(np.array([0, 100]) * factor)
h = Vertex(np.array([25, 100]) * factor)
t = Vertex(np.array([50, 100]) * factor)
k = Vertex(np.array([75, 100]) * factor)
d = Vertex(np.array([100, 100]) * factor)


tq = Triangle(deepcopy(a), deepcopy(j), deepcopy(n), deepcopy(a), screen, GREEN)
tw = Triangle(deepcopy(n), deepcopy(i), deepcopy(b), deepcopy(n), screen, RED)
ty = Triangle(deepcopy(j), deepcopy(r), deepcopy(f), deepcopy(j), screen, BLUE)
tu = Triangle(deepcopy(i), deepcopy(f), deepcopy(q), deepcopy(i), screen, BLUE)
ti = Triangle(deepcopy(r), deepcopy(o), deepcopy(f), deepcopy(r), screen, VIOLET)
to = Triangle(deepcopy(f), deepcopy(p), deepcopy(q), deepcopy(f), screen, VIOLET)
tp = Triangle(deepcopy(f), deepcopy(o), deepcopy(p), deepcopy(f), screen, BLUE)
ta = Triangle(deepcopy(l), deepcopy(c), deepcopy(o), deepcopy(l), screen, RED)
ts = Triangle(deepcopy(o), deepcopy(c), deepcopy(h), deepcopy(o), screen, BLUE)

cr = Quadrilateral(deepcopy(n), deepcopy(j), deepcopy(f), deepcopy(i), deepcopy(n), screen, ORANGE)
ce = Quadrilateral(deepcopy(a), deepcopy(l), deepcopy(o), deepcopy(j), deepcopy(a), screen, YELLOW)
ct = Quadrilateral(deepcopy(b), deepcopy(i), deepcopy(p), deepcopy(m), deepcopy(b), screen, GREEN)
cd = Quadrilateral(deepcopy(o), deepcopy(h), deepcopy(t), deepcopy(s), deepcopy(o), screen, GREEN)
cf = Quadrilateral(deepcopy(s), deepcopy(t), deepcopy(k), deepcopy(p), deepcopy(s), screen, RED)
cg = Quadrilateral(deepcopy(m), deepcopy(p), deepcopy(k), deepcopy(d), deepcopy(d), screen, YELLOW)




while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        # print(event) podemoa imprimir todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()
    # Aqui dibujamos
    # pygame.draw.polygon(screen, BLACK, [A, B, C, D], 2)
    # pygame.draw.polygon(screen, (0,255,0), (t.deepcopy_a.deepcopy, t.deepcopy_b.deepcopy , t.deepcopy_c.deepcopy ), 2)


    #pygame.draw.polygon((screen), (0, 255, 0), (c.deepcopy_a.deepcopy, c.deepcopy_b.deepcopy, c.deepcopy_c.deepcopy, c.deepcopy_d.deepcopy))


    ################################################
    """
    tq 
    tw 
    ty 
    tu
    ti
    to 
    tp 
    ta 
    ts
    cr
    ce
    ct
    cd
    cf
    cg
    """
    ################################################
    tq.draw()
    tw.draw()
    ty.draw()
    tu.draw()
    ti.draw()
    to.draw()
    tp.draw()
    ta.draw()
    ts.draw()

    cr.draw()
    ce.draw()
    ct.draw()
    cd.draw()
    cf.draw()
    cg.draw()

    g = -0.00172
    #c.rotate(g)
    #tp.move_l
    #tp.move_d
    clock.tick(5)

    # Aqui dibujamos
    pygame.display.flip()
