import math

def performCollisionsWithBoundaries(movingObjects, height, width):
    for movingObject in movingObjects:
        if movingObject.x >= width:
            movingObject.angle = - movingObject.angle
        elif movingObject.x <= 0:
            movingObject.angle =  - movingObject.angle
        elif movingObject.y >= height:
            movingObject.angle = math.pi - movingObject.angle
        elif movingObject.y <= 0:
            movingObject.angle = math.pi - movingObject.angle
            