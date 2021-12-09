# Simple Animation with Pygame, Isaiah Reyes, 12/09/21, 2:25, v0.4

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

# setup box data
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':DARKERBLOOD, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':NIGHTSKY, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLACK, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]
