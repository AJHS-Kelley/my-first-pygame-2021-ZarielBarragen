# My First PyGame, Isaiah Reyes, 12/1/21  1:40pm, v0.5

import pygame, sys
from pygame.locals import *

# Start Pygame 
pygame.init()

# Setup our window 
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

#Setup Colors
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CRIMSON = (144, 0, 37)

#Setup Font
basicFont = pygame.font.SysFont(None, 48)

#Setup Text
text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.cenerx = windowsSurface.get_rect().centerx
textRect.cenerx = windowsSurface.get_rect().centery

# Fill backround color
windowSurface.fill(CRIMSON) 

# Draw a polygon onto the screen
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56,277), (0, 106))

