# My First PyGame, Isaiah Reyes, 12/1/21  2:20pm, v1.1

import pygame, sys
from pygame.locals import *

# Start Pygame 
pygame.init()

# Setup our window 
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Yeet Yeet SKRRT')

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
text = basicFont.render('Yeet Yeet SKRRT', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centerx = windowSurface.get_rect().centery

# Fill backround color
windowSurface.fill(CRIMSON) 

# Draw a polygon onto the screen
pygame.draw.polygon(windowSurface, DARKARTS, ((146, 0), (291, 106), (236, 277), (56,277), (0, 106)))

# Draw lines on the screen
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLACK, (75, 60), (120, 75), 2)
pygame.draw.line(windowSurface, DARKARTS, (0, 150), (150, 0), 1)

# Draw a circle
pygame.draw.circle(windowSurface, BLACK, (300, 50), 20, 0)

# Draw a ellipse 
pygame.draw.ellipse(windowSurface, DARKARTS, (300, 250, 40, 80), 1)

# Draw the text triangle
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width - 40, textRect.height - 40))

# Create Pixel Array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = CRIMSON 
del pixArray

# Draw the text onto the surface
windowSurface.blit(text, textRect)

# Update Pygame Display
pygame.display.update()

# Run game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()