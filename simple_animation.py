# Simple Animation with Pygame, Isaiah Reyes, 12/09/21, 2:46, v0.6

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

# Run the game loop
while True:
    # Check for QUIT event.
    for event in pygame.event.get():
        if event.typ == QUIT
            pygame.quit()
            sys.exit()

windowSurface.fill(WHITE)

for b in boxes:
    # Move the box data structure 
    if b['dir'] == DOWNLEFT:
        b['rect'].left -= MOVESPEED
        b['rect'].top += MOVESPEED
    if b['dir'] == DOWNRIGHT:
        b['rect'].left += MOVESPEED
        b['rect'].top += MOVESPEED
    if b['dir'] == UPLEFT:
        b['rect'].left -= MOVESPEED
        b['rect'].top -= MOVESPEED
    if b['dir'] == UPRIGHT:
        b['rect'].left += MOVESPEED
        b['rect'].top -= MOVESPEED