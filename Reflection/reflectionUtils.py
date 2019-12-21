import math

def performCollisionsWithBoundaries(movingObjects, height, width):
    for movingObject in movingObjects:
        if movingObject.x > width - movingObject.size:
            movingObject.x = 2 * (width - movingObject.size) - movingObject.x
            movingObject.velocityVector.angle = - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
        elif movingObject.x - movingObject.size < 0:
            movingObject.x = 2 * movingObject.size - movingObject.x
            movingObject.velocityVector.angle =  - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
        elif movingObject.y > height - movingObject.size:
            movingObject.y = 2 * (height - movingObject.size) - movingObject.y
            movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
        elif movingObject.y - movingObject.size < 0:
            movingObject.y = 2 * movingObject.size - movingObject.y
            movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
            movingObject.velocityVector.magnitude *= movingObject.elasticity
