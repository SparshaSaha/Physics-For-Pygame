import math


def performCollisionsWithBoundaries(movingObject, height, width):
    if movingObject.x > width - movingObject.size:
        movingObject.x = 2 * (width - movingObject.size) - movingObject.x
        movingObject.velocityVector.angle = - movingObject.velocityVector.angle
        movingObject.velocityVector.magnitude *= movingObject.elasticity
    elif movingObject.x - movingObject.size < 0:
        movingObject.x = 2 * movingObject.size - movingObject.x
        movingObject.velocityVector.angle = - movingObject.velocityVector.angle
        movingObject.velocityVector.magnitude *= movingObject.elasticity
    elif movingObject.y > height - movingObject.size:
        movingObject.y = 2 * (height - movingObject.size) - movingObject.y
        movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
        movingObject.velocityVector.magnitude *= movingObject.elasticity
    elif movingObject.y - movingObject.size < 0:
        movingObject.y = 2 * movingObject.size - movingObject.y
        movingObject.velocityVector.angle = math.pi - movingObject.velocityVector.angle
        movingObject.velocityVector.magnitude *= movingObject.elasticity


def performCollisionsWithOneAnother(object1, object2):
    dx = object1.x - object2.x
    dy = object1.y - object2.y

    distance = math.hypot(dx, dy)
    if distance < object1.size + object2.size:
        tangent = math.atan2(dy, dx)
        object1.velocityVector.angle = 2 * tangent - object1.velocityVector.angle
        object2.velocityVector.angle = 2 * tangent - object2.velocityVector.angle
        (object1.velocityVector.magnitude, object2.velocityVector.magnitude) = (
            object2.velocityVector.magnitude, object1.velocityVector.magnitude)
        object1.velocityVector.magnitude *= object1.elasticity
        object2.velocityVector.magnitude *= object2.elasticity
        angle = 0.5 * math.pi + tangent
        object1.x += math.sin(angle)
        object1.y -= math.cos(angle)
        object2.x -= math.sin(angle)
        object2.y += math.cos(angle)


def performObjectToObjectCollision(movingObjects, currentObject, i):
    for j in range(i+1, len(movingObjects)):
        if movingObjects[j].isCollidable:
            performCollisionsWithOneAnother(currentObject, movingObjects[j])
