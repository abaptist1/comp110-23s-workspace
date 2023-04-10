"""EX07 Dictionary Utils Test File."""


__author__ = "730473328"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_1() -> None:
    """First unit test for invert, edge case for lists dicts where there are numbers."""
    test_dict: dict[str, str] = {"A": "1", "B": "2", "C": "3"}
    assert invert(test_dict) == {"1": "A", "2": "B", "3": "C"}


def test_invert_2() -> None:
    """2nd unit test for invert, use case where dict has capital and lowercase letters."""
    test_dict: dict[str, str] = {"A": "a", "B": "b", "C": "c"}
    assert invert(test_dict) == {"a": "A", "b": "B", "c": "C"}


def test_invert_3() -> None:
    """3rd unit test for invert, use case where dict has positive and negative numbers."""
    test_dict: dict[str, str] = {"-1": "1", "-2": "2", "-3": "3"}
    assert invert(test_dict) == {"1": "-1", "2": "-2", "3": "-3"}


def test_favorite_color_1() -> None:
    """1st unit test for favorite_color, edge case where there's only 1 color."""
    test_dict: dict[str, str] = {"Ben": "Red", "Zack": "Red", "Kyra": "Red"}
    assert favorite_color(test_dict) == "Red"


def test_favortite_color_2() -> None:
    """2nd unit test for favorite_color, use case where theres a clear winner."""
    test_dict: dict[str, str] = {"Ben": "Blue", "Kyra": "Blue", "Zack": "Red"}
    assert favorite_color(test_dict) == "Blue"


def test_favorite_color_3() -> None:
    """3rd unit test for favorite_color, use case where there's a tie and the color that appears first is the winner."""
    test_dict: dict[str, str] = {"Kyra": "Blue", "Ben": "Green", "Zack": "Red"}
    assert favorite_color(test_dict) == "Blue"


def test_count_1() -> None:
    """1st unit test for count, use case where there's only one item multiple times in the list."""
    test_list: list[str] = ["A", "A", "A"]
    assert count(test_list) == {"A": 3}


def test_count_2() -> None:
    """2nd unit test for count, use case where there's varying amounts of each item."""
    test_list: list[str] = ["A", "B", "A", "C"]
    assert count(test_list) == {"A": 2, "B": 1, "C": 1}


def test_count_3() -> None:
    """3rd unit test for count, edge use case where there's an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}