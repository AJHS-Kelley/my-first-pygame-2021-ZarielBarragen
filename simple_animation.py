# Simple Animation with Pygame, Isaiah Reyes, 12/09/21, 2:16, v0.3

import pygame, sys, time
from pygame.locals import *

# Setup pygame
pyagame.init()

#Setup the window 
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Set direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4 

# Setup color values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
NIGHTSKY = (77, 0, 118)
DARKERBLOOD = (70, 0, 0)
