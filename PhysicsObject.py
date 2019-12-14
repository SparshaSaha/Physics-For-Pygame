class PhysicsObject:

    def __init__(self, x, y, angle, speed, size, isGravityAffected):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.isGravityAffected = isGravityAffected
        self.size = size
