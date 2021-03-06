from typing import Iterable, Union
from uuid import uuid4, UUID
import numpy as np

from ex import ValueExpectedException


class Car:
    """Данный класс содержит параметры агента типа ``Car``.

    Свойства (*properties*):
       * pos -- текущая позиция (индекс клетки дорожной полосы);
       * uuid -- уникальный индентификатор объекта данного типа;
       * name -- название машины (агента).
    Методы:
       * copy -- создаёт полную копию экземпляра (с тем же ``uuid``).
    Переопределённые методы:
       * __repr__;
       * __eq__ -- сравниваются ``uuid`` двух экземпляров.
    """

    def __init__(self, pos: Union[Iterable, np.ndarray] = (0, 0), uuid: UUID = None, name: str = None):
        self.pos = pos
        self.uuid = uuid if uuid else uuid4()
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * uuid: {self.uuid}\n" \
               f" * name: {self.name}\n" \
               f" * pos: {self.pos}"

    def __eq__(self, other: 'Car'):
        return self.uuid == other.uuid

    def __hash__(self):
        return self.uuid

    def copy(self) -> 'Car':
        return Car(self.pos, self.uuid)

    @property
    def pos(self) -> np.ndarray:
        """Текущая позиция (индекс клетки) экземпляра. Здесь строки -- это полосы."""
        return self._pos

    @pos.setter
    def pos(self, new: np.ndarray):
        if not isinstance(new, np.ndarray):
            new = np.array(new)
        self._checkPos(new)
        self._pos = new.copy()

    def _checkPos(self, pos: np.ndarray):
        if np.any(pos < 0):
            raise ValueExpectedException("все значения pos >= 0", f"значения pos = {pos}", src=self.__class__.__name__)

    @property
    def uuid(self) -> UUID:
        """ID экземпляра."""
        return self._uuid

    @uuid.setter
    def uuid(self, new: Union[UUID, int]):
        self._uuid = new

    @property
    def name(self) -> Union[str, None]:
        """Название машины (агента)."""
        return self._name

    @name.setter
    def name(self, n: Union[str, None]):
        self._name = n


if __name__ == '__main__':
    c = Car(pos=(1, 20), name='Prisoner')
    print(c)
