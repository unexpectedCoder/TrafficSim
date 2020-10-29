from typing import Union
from uuid import uuid4, UUID


class Car:
    """Данный класс содержит параметры агента типа ``Car``.

    Свойства (*properties*):
       * pos -- текущая позиция (индекс клетки дорожной полосы типа ``RoadLane``);
       * uuid -- уникальный индентификатор объекта данного типа;
       * canMove -- может ли переместиться на одну позицию (клетку) вперёд;
       * canChangeLane -- может ли поменять полосу.
    Методы:
       * turnTo -- установливает, куда повернуть (индекс улицы может браться из объекта перекрёстка типа ``Crossroad``);
       * goStraight -- указание ехать прямо.
    """

    def __init__(self, pos: int = 0, uuid: UUID = None):
        self.pos = pos
        self.uuid = uuid if uuid else uuid4()

        self.canMove = False
        self.canChangeLane = False
        self._whereTurn = 0

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * uuid: {self.uuid}\n" \
               f" * canMove: {self.canMove}\n" \
               f" * canChangeLane: {self.canChangeLane}\n" \
               f" * whereTurn: {self.whereTurn}"

    def __eq__(self, other: 'Car'):
        return self.uuid == other.uuid

    def copy(self) -> 'Car':
        c = Car(self.pos, self.uuid)
        c.canMove = self.canMove
        c.canChangeLane = self.canChangeLane
        c.turnTo(self._whereTurn)
        return c

    @property
    def pos(self) -> int:
        return self._pos

    @pos.setter
    def pos(self, new: int):
        self._checkPos(new)
        self._pos = new

    def _checkPos(self, pos: int):
        if pos < 0:
            raise ValueError("\tОшибка: car.pos должна содержать быть >= 0!")

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @uuid.setter
    def uuid(self, new: Union[UUID, int]):
        self._uuid = new

    @property
    def canMove(self) -> bool:
        return self._canMove

    @canMove.setter
    def canMove(self, flag: bool):
        self._canMove = flag

    @property
    def canChangeLane(self) -> bool:
        return self._canChangeLane

    @canChangeLane.setter
    def canChangeLane(self, flag: bool):
        self._canChangeLane = flag

    @property
    def whereTurn(self) -> int:
        return self._whereTurn

    def turnTo(self, to: int):
        """Установить индекс улицы, на которую машина должна повернуть.

        :param to: индекс улицы, на которую машина должна повернуть.
        """
        self._whereTurn = to

    def goStraight(self):
        """Указание ехать прямо (сбрасывает *whereTurn* в 0)."""
        self._whereTurn = 0
