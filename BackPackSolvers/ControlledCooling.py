import math
import random
from .Shared import *


def find_random_neightbour(backpackState: List[int]) -> List[int]:
    dozmianny = random.randint(0, len(backpackState) - 1)
    return [reverse(element) if dozmianny == number else element for number, element in enumerate(backpackState)]


def jump_probality(current_value, new_value, temperature):
    return math.e ** (-1 * (abs(current_value - new_value)) / temperature)


def backpackCooling(capacity: float, items: list):
    temperature = 1000
    current_state = [1 if random.random() < 0.5 else 0 for _ in range(len(items))]
    current_value = count_backpack_value(current_state, items, capacity)

    for i in range(temperature, 0, -1):
        proposed_state = find_random_neightbour(current_state)
        proposed_value = count_backpack_value(proposed_state, items, capacity)

        if proposed_value > current_value:
            current_state = proposed_state
            current_value = proposed_value
        else:
            if jump_probality(current_value, proposed_value, temperature) < random.random():
                current_state = proposed_state
                current_value = proposed_value

    return current_state, current_value
