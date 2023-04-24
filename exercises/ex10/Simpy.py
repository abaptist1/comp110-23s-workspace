"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730473328"


class Simpy:
    """Defines the Simpy Class."""

    values: list[float]
    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        """Initialize the values attribute of Simpy to the argument passed in."""
        self.values = values

    def __str__(self) -> str:
        """Convert Simpy Object into String Representation."""
        return f"Simpy({str(self.values)})"
    
    def fill(self, val_filled: float, num_vals_to_fill: int) -> None:
        """Fill Simpy's values with a repeating value."""
        self.values = [val_filled] * num_vals_to_fill

    def arange(self, start: float, stop: float, step: float = 1) -> None:
        """Arrange a range of values in order by a certain step value."""
        assert step != 0.0
        self.values = []
        if step > 0:
            while start < stop:
                self.values.append(start)
                start += step
        else:
            while start > stop:
                self.values.append(start)
                start += step
        
    def sum(self) -> float:
        """Sum all the values in a Simpy Object."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Sum individual values in a Simpy object."""
        new_simpy = Simpy(self.values.copy())
        if type(rhs) == float:
            new_simpy.values = [val + rhs for val in self.values]
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                new_simpy.values[i] += rhs.values[i]
        return new_simpy

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise one veach value in self to the power of the corresponding Simpy Value."""
        new_simpy = Simpy(self.values.copy())
        if type(rhs) == float:
            new_simpy.values = [val ** rhs for val in self.values]
        else:
            assert len(self.values) == len(new_simpy.values)
            for i in range(len(self.values)):
                new_simpy.values[i] = self.values[i] ** rhs.values[i]
        return new_simpy

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check to see if values are equal at corresponding indexes of a Simpy."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for val in range(len(self.values)):
                if self.values[val] == rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            for val in range(len(self.values)):
                if self.values[val] == rhs.values[val]:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check to see if values in self are greater than corresponding values in rhs."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Retrieve a specific item from a Simpy."""
        if isinstance(rhs, int):
            output = self.values[rhs]
            return output
        else:
            floats: list[float] = []
            for i in range(0, len(rhs)):
                if rhs[i] is True:
                    floats.append(self.values[i])
            return Simpy(floats)