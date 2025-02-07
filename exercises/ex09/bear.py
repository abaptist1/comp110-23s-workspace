"""File to define Bear class."""


class Bear:
    """Defines the Bear object."""
    # attributes
    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bears."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates one bear day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Models the bear's eating habits."""
        self.hunger_score += num_fish
        return None