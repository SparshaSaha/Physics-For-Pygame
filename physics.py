import math

class Physics(object):

    def __init__(self):
        self.stationaryObjects = []
        self.movingObjects = []
    
    def registerStationaryObjects(self, stationaryObject):
        self.stationaryObjects.append(stationaryObject)
    
    def unregisterStationaryObject(self, stationaryObject):
        if stationaryObject in self.stationaryObjects:
            self.stationaryObjects.remove(stationaryObject)

    def registerMovingObject(self, movingObject):
        self.movingObjects.append(movingObject)
    
    def unregisterMovingObject(self, movingObject):
        if movingObject in self.movingObjects:
            self.movingObjects.remove(movingObject)

    def __updateCoordinates__(self, movingObject):
        movingObject.x += math.sin(movingObject.angle) * movingObject.speed
        movingObject.y -= math.cos(movingObject.angle) * movingObject.speed
    
