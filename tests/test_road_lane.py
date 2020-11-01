import numpy as np

from ex import ValueExpectedException
from car import Car
from road_lane import RoadLane


def test_init():
    try:
        RoadLane(0)
        assert False
    except ValueExpectedException as ex:
        print()
        print(ex.message)
        assert True


def test_capacity():
    rl = RoadLane()
    assert rl.capacity == 1
    rl.capacity = 7
    assert rl.capacity == 7


def test_add():
    rl = RoadLane(3, [Car(1)])
    assert np.all(rl.cells == [0, 1, 0])
    rl.addCar(Car(10))
    assert np.all(rl.cells == [1, 1, 0])
    rl.addCar(Car(70), pos=2)
    assert np.all(rl.cells == [1, 1, 1])


def test_rm():
    c1, c2, c3 = Car(), Car(1), Car(2)
    rl = RoadLane(3, [c1, c2, c3])
    assert np.all(rl.cells == [1, 1, 1])
    rl.rmCar(c2)
    assert np.all(rl.cells == [1, 0, 1])


def test_update():
    rl = RoadLane(3, [Car()])
    assert np.all(rl.cells == [1, 0, 0])
    rl.update()
    assert np.all(rl.cells == [0, 1, 0])
    rl.update()
    assert np.all(rl.cells == [0, 0, 1])
    # TODO тест случая, когда машина "выходит" с дороги (pos > capacity)
