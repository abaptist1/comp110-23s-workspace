"""File to define Fish class!"""


class Fish:
    """Defines the Fish Class."""
    # attributes
    age: int
    
    def __init__(self):
        """Initializes Fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates one fish day."""
        self.age += 1
        return None