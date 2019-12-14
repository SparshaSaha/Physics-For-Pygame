import pygame
from pygame.locals import *
from Reflection.physics import Physics

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Basic Pygame program')


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
font = pygame.font.Font(None, 36)
text = font.render("Hello There", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

screen.blit(background, (0,0))
pygame.display.flip()
c = True
while c:
    for event in pygame.event.get():
        if event.type == QUIT:
            c = False
    
    screen.blit(background, (0,0))
    pygame.display.flip()

