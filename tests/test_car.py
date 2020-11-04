from uuid import uuid4

from car import Car
from ex import ValueExpectedException


def test_init():
    try:
        Car(pos=(1, 2))
        assert True
        Car((-1, 2))
        assert False
    except ValueExpectedException as ex:
        print()
        print(ex.message)   # см. вывод в консоли
        assert True


def test_eq():
    c1 = Car((1, 2))
    c2 = c1.copy()
    assert c1 == c2
    c2.pos = (1, 7)
    assert c1 == c2
    c2.uuid = uuid4()
    assert c1 != c2
