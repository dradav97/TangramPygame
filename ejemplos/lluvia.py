import random
import sys
import pygame

pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)

# Definimos algunos colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VIOLET = (245, 0, 245)
LEELA = (255, 245, 255)
clock = pygame.time.Clock()

# Definimos las 50 coordenadas de cada gota de manera aleatoria
coors = []
for i in range(50):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    coors.append([x, y])

while True:
    clock.tick(60)
    screen.fill(LEELA)
    for event in pygame.event.get():
        # print(event) podemoa imprimir todos los eventos
        if event.type == pygame.QUIT:
            sys.exit()

# Dibujamos las 50 gotas usando las coordenadas generadas en la linea 20-24
    for coor in coors:
        pygame.draw.circle(screen, VIOLET, coor, 2)
        coor[1] += 1

        # Si una gota sale del margen inferior generamos una nueva coordenada en la parte superior
        # con una coordenada en y de 0 y en x aleatoriamente para que el patron no se repita
        if coor[1] > 400:
            # Para que aparezca en la parte superior coor[0] = 0
            coor[1] = 0

            # Para que aparezca de manera aleatoria en el eje horizontal
            coor[0] = random.randint(0, 400)
    pygame.display.flip()