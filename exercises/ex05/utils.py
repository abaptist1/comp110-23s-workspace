"""EX 05 List Utils."""

__author__ = "730473328"


def only_evens(given_list: list[int]) -> list[int]:
    """Searches a list for the even values an returns a list wiht just even values."""
    even_list: list[int] = []
    for value in given_list:
        if value % 2 == 0:
            even_list.append(value)
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Takes two lists of ints and adds the second list to the end of the first."""
    concat_list: list[int] = []
    for value in list_one:
        concat_list.append(value)
    for value in list_two:
        concat_list.append(value)
    return concat_list


def sub(initial_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Takes a list and 2 given start and end indexes and makes a new list of the values from the start indeded to the end index -1."""
    sub_list: list[int] = []
    sub_idx = 0
    if start_idx < 0:
        sub_idx = start_idx * -1
    if len(initial_list) == 0 or start_idx > len(initial_list) or end_idx <= 0:
        return list()
    if end_idx > len(initial_list):
        end_idx = len(initial_list)
    while start_idx + sub_idx < len(initial_list) and start_idx + sub_idx < end_idx:
        sub_list.append(initial_list[start_idx + sub_idx])
        sub_idx += 1
    return sub_list