# My First PyGame, Isaiah Reyes, 12/1/21  2:07pm, v0.9

import pygame, sys
from pygame.locals import *

# Start Pygame 
pygame.init()

# Setup our window 
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

# Setup Colors
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CRIMSON = (144, 0, 37)
DARKARTS = (49, 0, 92)

# Setup Font
basicFont = pygame.font.SysFont(None, 48)

# Setup Text
text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.cenerx = windowsSurface.get_rect().centerx
textRect.cenerx = windowsSurface.get_rect().centery

# Fill backround color
windowSurface.fill(CRIMSON) 

# Draw a polygon onto the screen
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56,277), (0, 106)))

# Draw lines on the screen
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLACK, (75, 60), (120, 75), 2)
pygame.draw.line(windowSurface, DARKARTS, (0, 150), (150, 0), 1)

# Draw a circle
pygame.draw.circle(windowSurface, BLACK, (300, 50), 20, 0)

# Draw a ellipse 
pygame.draw.ellipse(windowSurface, DARKARTS, (300, 250, 40, 80), 1)

# Draw the text triangle
pygame.draw.rect(windowsSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width - 40, textRect.height - 40))