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
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __str__(self):
        """Print prettier version of our point"""
        return f"({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point: # Overwrites the multiplication operatior * so it can use a point and an int
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __getitem__(self, index: int) -> float:
        """Overloading subscription notation"""
        if index == 0:
            return self.x
        elif index == 1: # Can replace this line with an else statement with an if statement inside
                return self.y
        else:
            raise IndexError

a: Point = Point(1.0, 2.0)
# b: Point = a.scale(3.0)
b: Point = a * 3.0
print(b[3]) #gives y- coordinate using tje __getitem__ magic method
