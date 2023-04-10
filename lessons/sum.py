"""Example function for unit tests"""

def sum_old(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    return sum_total

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs using for loops"""
    sum_total: float = 0.0
    for idx in range(0,len(xs)):
        sum_total += xs[idx]
    return sum_total