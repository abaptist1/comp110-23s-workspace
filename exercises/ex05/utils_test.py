"""Unit Tests file containing test functions for ex05."""


__author__: str = "730473328"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_1() -> None:
    """First unit test for only_evens, edge case for lists with no even numbers."""
    test_list: list[int] = [1, 3, 7]
    assert only_evens(test_list) == []


def test_only_evens_2() -> None:
    """2nd unit test for only_evens, used to pick ages of people and sort into a group of people with even ages."""
    test_list: list[int] = [20, 31, 46, 38]
    assert only_evens(test_list) == [20, 46, 38]


def test_only_evens_3() -> None:
    """3rd unit test for only_evens, used to sort groups of positive and negative numbers into even and odd."""
    test_list: list[int] = [-1, -4, 4, 6, 7]
    assert only_evens(test_list) == [-4, 4, 6]


def test_concat_1() -> None:
    """1st unit test for concat, takes two lists of ticket entries matched to a number and adds them together."""
    test_list_1: list[int] = [2230, 4563, 4435]
    test_list_2: list[int] = [1530, 8756, 9658]
    assert concat(test_list_1, test_list_2) == [2230, 4563, 4435, 1530, 8756, 9658]


def test_concat_2() -> None:
    """2nd unit test for concat, take two lists of oustanding orders assigned numbers and adds them together."""
    order_list_1: list[int] = [34, 2, 45]
    order_list_2: list[int] = [15, 32, 75]
    assert concat(order_list_1, order_list_2) == [34, 2, 45, 15, 32, 75]


def test_concat_3() -> None:
    """3rd unit test edge case, one empty list and one list with values."""
    test_list_1: list[int] = [1, 3, 4]
    test_list_2: list[int] = []
    assert concat(test_list_1, test_list_2) == [1, 3, 4]


def test_sub_1() -> None:
    """1st use case for sub, removing the first and last values of a list."""
    test_list: list[int] = [1, 3, 5, 7, 34]
    start_idx: int = 1
    end_idx: int = 4
    assert sub(test_list, start_idx, end_idx) == [3, 5, 7]


def test_sub_2() -> None:
    """2nd use case for sub, finding ranges in a data set of grades."""
    test_list: list[int] = [78, 85, 89, 93, 98]
    start_idx: int = 0
    end_idx: int = 4
    assert sub(test_list, start_idx, end_idx) == [78, 85, 89, 93]


def test_sub_3() -> None:
    """3rd use case for sub, edge case where the length of the list is 0 and must return an empty list."""
    test_list: list[int] = []
    start_idx: int = 0
    end_idx: int = 3
    assert sub(test_list, start_idx, end_idx) == []