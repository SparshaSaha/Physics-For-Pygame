import math

def performCollisionsWithBoundaries(movingObjects, height, width):
    for movingObject in movingObjects:
        if movingObject.x >= width:
            movingObject.velocityVector.angle = - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
        elif movingObject.x <= 0:
            movingObject.velocityVector.angle =  - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
        elif movingObject.y >= height:
            movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
        elif movingObject.y <= 0:
            movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
