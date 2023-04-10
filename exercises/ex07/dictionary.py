"""EX07 Dictionary Utils."""


__author__ = "730473328"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary of strings and inverts the key value pairs in a new dictionary."""
    inverted_dict = {}
    for key in dictionary:
        dict_value = dictionary[key]
        if dict_value in inverted_dict:
            raise KeyError
        inverted_dict[dict_value] = key
    return inverted_dict


def favorite_color(color_dictionary: dict[str, str]) -> str:
    """Counts how many times a value appears in a sict and returns the value that appears the most."""
    fav_color: str = ""
    color_count: dict[str, int] = {}
    for key in color_dictionary:
        if color_dictionary[key] in color_count:
            color_count[color_dictionary[key]] += 1
        else:
            color_count[color_dictionary[key]] = 1
    max_color = 0
    for key in color_count:
        if color_count[key] > max_color:
            max_color = color_count[key]
            fav_color = key
    return fav_color


def count(initial_list: list[str]) -> dict[str, int]:
    """Tales a list and counts how many times a value appears and returns a dict with each list value as a key and the number of times it appeared in the list as a value for that key."""
    result_dict = {}
    for idx in initial_list:
        if idx in result_dict:
            result_dict[idx] += 1
        else:
            result_dict[idx] = 1
    return result_dict
