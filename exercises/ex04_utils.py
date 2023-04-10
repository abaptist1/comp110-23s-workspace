"""EX 04 List Utility Functions!"""

__author__: str = "730473328"


def all(num_list: list[int], x: int) -> bool:
    """Return true if items in list match given int, false if not."""
    idx: int = 0
    if len(num_list) == 0:
        return False
    while idx < len(num_list):
        if num_list[idx] != x:
            return False
        idx += 1
    return True


def max(max_list: list[int]) -> int:
    """Searches a list for the maximum int value and returns that value."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an emptylist")
    max_idx: int = 0
    max: int = max_list[0]
    while max_idx < len(max_list):
        if max < max_list[max_idx]:
            max = max_list[max_idx]
        max_idx += 1
    return max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks if every item at every index in two seperate lists are the same."""
    if len(list_one) == 0 and len(list_two) == 0:
        return True
    if len(list_one) == 0 or len(list_two) == 0:
        return False
    if len(list_one) != len(list_two):
        return False
    idx_of_list: int = 0
    while idx_of_list < len(list_one) and idx_of_list < len(list_two):
        if list_one[idx_of_list] != list_two[idx_of_list]:
            return False
        idx_of_list += 1
    return True
        
