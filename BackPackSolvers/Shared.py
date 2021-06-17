from typing import List


def count_backpack_value(backpackState: List[int], items: list, max_capacity: float) -> float:
    total_weight = 0
    total_value = 0
    for state, item in zip(backpackState, items):
        total_weight += state * float(item[0])
        if total_weight > max_capacity:
            return 0
        total_value += state * float(item[0]) * float(item[1])
    return total_value


def reverse(__x: int) -> int:
    return 0 if __x == 1 else 1
