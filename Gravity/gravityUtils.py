import math
from Vector import Vector

def addGravity(gameObjects):
    gravity = Vector(math.pi, 0.05)
    for gameObject in gameObjects:
        gameObject.velocityVector = gameObject.velocityVector.addVector(gravity)

