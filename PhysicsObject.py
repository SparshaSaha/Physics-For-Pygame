class PhysicsObject:

    def __init__(self, x, y, vector, size, isGravityAffected, isCollidable, elasticity=1.0):
        self.x = x
        self.y = y
        self.velocityVector = vector
        self.isGravityAffected = isGravityAffected
        self.size = size
        self.elasticity = elasticity
        self.isCollidable = isCollidable
