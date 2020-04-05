import math
from vector import Vector


def addGravity(gameObject):
    gravity = Vector(math.pi, 0.05)
    gameObject.velocityVector = gameObject.velocityVector.addVector(
        gravity)
