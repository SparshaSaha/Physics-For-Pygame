import pygame
from pygame.locals import *
from physics import Physics
from physicsObject import PhysicsObject
from vector import Vector
import math


class Particle(PhysicsObject):

    def __init__(self, x, y, angle):
        self.angle = angle
        self.speed = 5
        self.colour = (0, 0, 0)
        self.x = x
        self.y = y
        self.velocityVector = Vector(self.angle, self.speed)
        super().__init__(self.x, self.y, self.velocityVector,
                         10,  False, False, elasticity=0.9)

    def display(self):
        pygame.draw.circle(screen, self.colour,
                           (int(self.x), int(self.y)), 10, 0)


pygame.init()
flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN
screen = pygame.display.set_mode((600, 600), flags)
pygame.display.set_caption('Basic Pygame program')


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

screen.blit(background, (0, 0))
pygame.display.flip()
par = Particle(20, 20, math.pi/3)
par1 = Particle(50, 50, math.pi/6)
par2 = Particle(250, 350, math.pi/7)
p = Physics(600, 600)
p.registerMovingObject(par)
p.registerMovingObject(par1)
p.registerMovingObject(par2)
c = True

while c:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN:
            c = False
    p.performPhysics()
    screen.blit(background, (0, 0))
    par.display()
    par1.display()
    par2.display()
    pygame.display.flip()
pygame.quit()
