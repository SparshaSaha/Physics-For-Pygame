import pygame
from pygame.locals import *
from Reflection.physics import Physics
from PhysicsObject import PhysicsObject
import math

class Particle(PhysicsObject):

    def __init__(self):
        self.angle = math.pi/3
        self.speed = 15
        self.colour = (0,0,0)
        self.x = 20
        self.y = 20
        super().__init__(self.x, self.y, self.angle, self.speed, False)

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), 5, 1)
    

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Basic Pygame program')


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


screen.blit(background, (0,0))
pygame.display.flip()
par = Particle()
p = Physics(600, 600)
p.registerMovingObject(par)
c = True

while c:
    for event in pygame.event.get():
        if event.type == QUIT:
            c = False
    p.performReflectionPhysics()
    screen.blit(background, (0,0))
    par.display()
    pygame.display.flip()

