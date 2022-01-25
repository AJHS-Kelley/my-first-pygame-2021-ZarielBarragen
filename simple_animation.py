# Simple Animation with Pygame, Isaiah Reyes, 1/25/22, 2:48, v0.8

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

        if b['rect'].top < 0:
            # The box had moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
            if b['rect'].bottom > WINDOWHEIGHT:
                # The box has moved past the bottom
                if b['dir'] == DOWNLEFT:
                    b['dir'] = UPLEFT
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = UPRIGHT
            if b['rect'].left < 0:
                # The box has moved past the left.
                if b['dir'] == DOWNLEFT:
                    b['dir'] = UPLEFT
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = UPRIGHT
            if b['rect'].right > WINDOWIDTH:
                # The box has moved past the right
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPLEFT:
                    b['dir'] = UPRIGHT

        # Draw the box onto the game surface.
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # Draw the window to the screen
    pygame.display.update()
    time.sleep(0.02)
