import random
from typing import List
from .Shared import count_backpack_value, reverse


def backpackClimbing(capacity: float, items: list):
    current_state = [1 if random.random() < 0.5 else 0 for _ in range(len(items))]
    current_value = count_backpack_value(current_state, items, capacity)

    value_was_changed = True
    while value_was_changed:
        value_was_changed = False
        combined_ways = combine_ways(current_state)
        state, value = find_best_neighbour(combined_ways, items, capacity)

        if value > current_value:
            current_state = state
            current_value = value
            value_was_changed = True

    return current_state, current_value


def combine_ways(currentstate: List[int]) -> List[List[int]]:
    return [[element if numer2 != numer else reverse(element) for numer2, element in enumerate(nowa)]
            for numer, nowa in enumerate([currentstate] * len(currentstate))]


def find_best_neighbour(stateList: List[List[int]], items: list, capacity: float) -> tuple:
    new_state = stateList[0]
    new_value = count_backpack_value(stateList[0], items, capacity)

    for state in stateList[1:]:
        possible_value = count_backpack_value(state, items, capacity)
        if possible_value > new_value:
            new_value = possible_value
            new_state = state

    return new_state, new_value
