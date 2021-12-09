# Simple Animation with Pygame, Isaiah Reyes, 12/09/21, 2:06, v0.1

import pygame, sys, time
from pygame.locals import *

# Setup pygame
pyagame.init()

#Setup the window 
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
