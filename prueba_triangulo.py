import sys
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
    screen.fill(WHITE)
    for event in pygame.event.get():
        # print(event) podemoa imprimir todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()
    # Aqui dibujamos
    #pygame.draw.polygon(screen, BLACK, [A, B, C, D], 2)

    pygame.draw.polygon(screen, (0,255,0), [[10, 10], [10, 110], [110, 110], [110, 10]], 2)
    clock.tick(60)
    # Aqui dibujamos
    pygame.display.flip()