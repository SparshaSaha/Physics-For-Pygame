import math

def performCollisionsWithBoundaries(movingObjects, height, width):
    for movingObject in movingObjects:
        if movingObject.x >= width:
            movingObject.velocityVector.angle = - movingObject.velocityVector.angle
        elif movingObject.x <= 0:
            movingObject.velocityVector.angle =  - movingObject.velocityVector.angle
        elif movingObject.y >= height:
            movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
        elif movingObject.y <= 0:
            movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
