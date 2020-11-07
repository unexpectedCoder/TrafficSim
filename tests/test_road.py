import numpy as np

from ex import ValueExpectedException
from car import Car
from road import Road


def test_init():
    try:
        Road(1, 2, -30, [])
        assert False
    except ValueExpectedException as ex:
        print()
        print(ex.message)
        assert True


def test_capacity():
    r = Road(1, 2, 30, [])
    assert r.lane_capacity == 30
    r.lane_capacity = 7
    assert r.lane_capacity == 7


def test_add():
    r = Road(1, 2, 3, [Car((0, 1))])
    assert np.all(r.cells == [0, 1, 0])
    r.addCar(Car(), pos=(0, 2))
    assert np.all(r.cells == [0, 1, 1])
    r.addCar(Car())
    assert np.all(r.cells == [1, 1, 1])


def test_rm():
    c1, c2, c3 = Car(), Car((0, 1)), Car((0, 2))
    r = Road(1, 2, 3, [c1, c2, c3])
    assert np.all(r.cells == [1, 1, 1])
    r.rmCar(c2)
    assert np.all(r.cells == [1, 0, 1])


def test_update():
    r = Road(1, 2, 3, [Car()])
    assert np.all(r.cells == [1, 0, 0])
    r.update()
    assert np.all(r.cells == [0, 1, 0])
    r.update()
    assert np.all(r.cells == [0, 0, 1])
    # TODO тест случая, когда машина "выходит" с дороги (pos > capacity)
