from BackPackSolvers import HillClimber


def test_backpack_climbing1():
    for _ in range(4):
        items = [(20, 2), (20, 4), (10, 4), (5, 10)]
        state, value = HillClimber.backpackClimbing(40, items)
        assert value == 170 or value == 130
