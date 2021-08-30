import sys
import math
import pygame

pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VIOLET = (125, 125, 125)
alfa = 0
clock = pygame.time.Clock()
while True:
    x = math.sin(alfa) * 100 + 200
    y = math.cos(alfa) * 100 + 200
    alfa += 0.01
    screen.fill(WHITE)
    for event in pygame.event.get():
        # print(event) podemoa imprimir todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()
    # Aqui dibujamos
    pygame.draw.line(screen, BLACK, [200, 199], [x, y], 1)
    pygame.draw.circle(screen, GREEN, (200, 200), 3)
    pygame.draw.circle(screen, RED, (x, y), 3)
    clock.tick(60)
    # Aqui dibujamos
    pygame.display.flip()