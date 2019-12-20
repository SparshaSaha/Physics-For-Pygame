import math

class Vector:

    def __init__(self, angle, magnitude):
        self.angle = angle
        self.magnitude = magnitude
    
    def addVector(self, vector):
        resultantVector = Vector(0, 0)
        x = math.sin(self.angle) * self.magnitude + math.sin(vector.angle) * vector.magnitude
        y = math.cos(self.angle) * self.magnitude + math.cos(vector.angle) * vector.magnitude
        resultantVector.magnitude = math.hypot(x, y)
        resultantVector.angle = 0.5 * math.pi - math.atan2(y, x)
        return resultantVector
