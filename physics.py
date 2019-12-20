import math
from Reflection.reflectionUtils import performCollisionsWithBoundaries

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

    def __updateCoordinates__(self):
        for movingObject in self.movingObjects:
            movingObject.x += math.sin(movingObject.angle) * movingObject.speed
            movingObject.y -= math.cos(movingObject.angle) * movingObject.speed
    
    def performReflectionPhysics(self):
        performCollisionsWithBoundaries(self.movingObjects, self.height, self.width)
        self.__updateCoordinates__()
                


    
