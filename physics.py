import math
from Collision.collisionUtils import performCollisionsWithBoundaries, performObjectToObjectCollision
from Gravity.gravityUtils import addGravity


class Physics(object):

    def __init__(self, height, width):
        self.boundaries = []
        self.movingObjects = []
        self.height = height
        self.width = width

    def registerBoundary(self, boundary):
        self.boundaries.append(boundary)

    def unregisterBoundary(self, boundary):
        if boundary in self.boundaries:
            self.boundaries.remove(boundary)

    def registerMovingObject(self, movingObject):
        self.movingObjects.append(movingObject)

    def unregisterMovingObject(self, movingObject):
        if movingObject in self.movingObjects:
            self.movingObjects.remove(movingObject)

    def __updateCoordinates__(self, movingObject):
        movingObject.x += math.sin(movingObject.velocityVector.angle) * \
            movingObject.velocityVector.magnitude
        movingObject.y -= math.cos(movingObject.velocityVector.angle) * \
            movingObject.velocityVector.magnitude

    def performPhysics(self):
        for i in range(0, len(self.movingObjects)):
            movingObject = self.movingObjects[i]
            addGravity(movingObject)
            performCollisionsWithBoundaries(
                movingObject, self.height, self.width)
            if movingObject.isCollidable:
                performObjectToObjectCollision(
                    self.movingObjects, movingObject, i)
            self.__updateCoordinates__(movingObject)
