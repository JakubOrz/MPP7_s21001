import Core
import random


def main():
    backpack = float(input("Podaj pojemność plecaka\n"))
    itemsCount = int(input("Ile przedmiotów będzie\n"))
    items = list()
    for _ in range(itemsCount):
        items.append(input("Waga : Wartość\n").split(" "))
    state, value = Core.backpack(backpack, items)

    print(f"Optymalny układ to {state} otrzymana wartość: {value}")


def main2():
    items_count = 3
    items = [(20, 2), (20, 4), (10, 4), (5, 10)]
    zawartosc = [1 if random.random() < 0.5 else 0 for _ in range(items_count)]
    combined = Core.combine_ways(zawartosc)
    state, value = Core.find_best_neighbour(combined, items, 40)

    print(zawartosc)
    print(combined)
    print(state, value)


if __name__ == '__main__':
    main()
