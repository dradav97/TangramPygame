import pygame
import sys

from pygame.constants import MOUSEBUTTONUP

pygame.init()
screen = pygame.display.set_mode((800,600))

x,y = 100,1000

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        
    pygame.draw.circle(screen, (50,150,250),(x,y),30,2)
    pygame.display.flip()