from __future__ import annotations

class Point:
    """Model a 2D Point""" 

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a point with its x, y components"""
        self.x = x
        self.y = y

    def scale_by(self, factor: float):
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y *factor)
        return scaled
    
p0 = Point(x = 1.0, y = 2.0)

p0.scale_by(2.0)
p1: Point = p0.scale(2.0)

print(p1.y)
