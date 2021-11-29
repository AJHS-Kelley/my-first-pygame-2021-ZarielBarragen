# My First PyGame, Isaiah Reyes, 11/29/21  2:25pm, v0.2

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

#Setup Font
basicFont = pygame.font.SysFont(None, 48)

#Setup Text
text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.cenerx = windowsSurface.get_rect().centerx
textRect.cenerx = windowsSurface.get_rect().centery
