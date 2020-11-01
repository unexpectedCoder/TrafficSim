from typing import Union
from uuid import uuid4, UUID

from ex import ValueExpectedException


class Car:
    """Данный класс содержит параметры агента типа ``Car``.

    Свойства (*properties*):
       * pos -- текущая позиция (индекс клетки дорожной полосы);
       * uuid -- уникальный индентификатор объекта данного типа.
    Методы:
       * copy -- создаёт полную копию экземпляра (с тем же ``uuid``).
    Переопределённые методы:
       * __repr__;
       * __eq__ -- сравниваются ``uuid`` двух экземпляров.
    """

    def __init__(self, pos: int = 0, uuid: UUID = None):
        self.pos = pos
        self.uuid = uuid if uuid else uuid4()

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * uuid: {self.uuid}\n" \
               f" * pos: {self.pos}"

    def __eq__(self, other: 'Car'):
        return self.uuid == other.uuid

    def copy(self) -> 'Car':
        return Car(self.pos, self.uuid)

    @property
    def pos(self) -> int:
        """Текущая позиция (индекс клетки) экземпляра."""
        return self._pos

    @pos.setter
    def pos(self, new: int):
        self._checkPos(new)
        self._pos = new

    def _checkPos(self, pos: int):
        if pos < 0:
            raise ValueExpectedException("pos >= 0", f"pos = {pos}", src=self._checkPos.__name__)

    @property
    def uuid(self) -> UUID:
        """ID экземпляра."""
        return self._uuid

    @uuid.setter
    def uuid(self, new: Union[UUID, int]):
        self._uuid = new
