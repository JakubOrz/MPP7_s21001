from BackPackSolvers import Hc, Sa
import sys


def do_the_thing(mode: str):
    backpackCapacity = float(input("Podaj pojemność plecaka\n"))
    itemsCount = int(input("Ile przedmiotów będzie\n"))
    items = list()
    for _ in range(itemsCount):
        items.append(input("Waga : Wartość\n").split(" "))

    state, value = None, None
    if mode == "HC":
        state, value = Hc(backpackCapacity, items)
    elif mode == "SA":
        state, value = Sa(backpackCapacity, items)

    print(f"Optymalny układ to {state} otrzymana wartość: {value}")


def main():
    if len(sys.argv) < 1:
        print("Nie podano w argumencie wywołania trybu algorytmu")
        return
    elif sys.argv[1] == "HC":
        do_the_thing("HC")
        return
    elif sys.argv[1] == "SA":
        do_the_thing("SA")
        return
    else:
        print("Niepoprawny argument wywołania oczekiwany: HC / SA")
        return


if __name__ == '__main__':
    main()
