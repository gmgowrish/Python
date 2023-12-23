import pygame, sys, os

from pygame.locals import *

red = [255, 0, 0]

pygame.init()

# window setup

window = pygame.display.set_mode((1000, 600))

pygame.display.set_caption('Slither.eat - The Snake Game')

# set up drawing surface
screen = pygame.display.get_surface()

screen.fill(red)

pygame.display.set_caption('snake')
pygame.display.flip()

count = 0

while True:
    print("Slither.eat - The Snake Game!")
    pass
