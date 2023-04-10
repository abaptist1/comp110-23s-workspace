"""CQ04 Practice wit Dict Function Writing."""

def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    dict_output: dict[list[str], list[int]] = {}
    key_2: int = 0
    if len(list_1) == 0 or len(list_2) == 0:
        return {}
    if len(list_1) != len(list_2):
        return {}
    for keys in list_1:
        dict_output[keys] = list_2[key_2]
        key_2 += 1
    return dict_output
