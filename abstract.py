from abc import ABC
from uuid import uuid4
from typing import Tuple, Union
from ex import ValueExpectedException


class Node(ABC):
    """Абстрактный класс узла графа.

    Свойства:
       * *id* -- возвращает целочисленный номер;
       * *color* -- цвет узла.
    Переопределяет:
       * *__hash__* -- возвращает ID;
       * *__eq__* -- сравнивает ID.
    """
    def __init__(self, **kwargs):
        self._id = kwargs['id'] if 'id' in kwargs else uuid4().int
        self._color = kwargs['color'] if 'color' in kwargs else (0, 0, 0)

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self) -> int:
        """ID узла графа."""
        return self._id

    @property
    def color(self) -> Tuple[int, int, int]:
        """Цвет узла."""
        return self._color

    @color.setter
    def color(self, c: Tuple[int, int, int]):
        self._color = c


class Edge(ABC):
    """Ребро графа.

    Ребро направлено от узла *u* к узлу *v*.

    Свойства:
       * *uv* (имеет setter) -- кортеж вида ``(u, v)``;
       * *name* (имеет setter) -- название ребра;
       * *weight* (имеет setter) -- вес ребра;
       * *color* (имеет setter) -- цвет ребра;
       * *id* -- ID ребра.
    Методы:
       * *is_equal_to* -- проверить на равенство вес ребра весу другого ребра.
    Переопределяет:
       * *__hash__* -- возвращает UUID ребра;
       * *__eq__* -- сравнивает UUID двух рёбер;
       * *__repr__*.
    """

    def __init__(self, u: int, v: int, **kwargs):
        self.uv = u, v
        self.name = kwargs['name'] if 'name' in kwargs else None
        self.weight = kwargs['weight'] if 'weight' in kwargs else 0
        self.color = kwargs['color'] if 'color' in kwargs else (0, 0, 0)
        self._id = kwargs['id'] if 'id' in kwargs else uuid4().int

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * uv: {self.uv}\n" \
               f" * name: {self.name}\n" \
               f" * weight: {self.weight}\n" \
               f" * color (RGB): {self.color}\n" \
               f" * id: {self.id}"

    def __hash__(self):
        return self.id

    def __eq__(self, other: 'Edge'):
        return self.id == other.id

    @property
    def uv(self) -> Tuple[int, int]:
        """Направление ребра от ``u`` к ``v``."""
        return self._u, self._v

    @uv.setter
    def uv(self, new_uv: Tuple[int, int]):
        self._check_u_v(*new_uv)
        self._u, self._v = new_uv

    def _check_u_v(self, u: int, v: int):
        if u == v:
            raise ValueExpectedException("u != v", f"u({u}) == v({v})", src=self.__class__.__name__)
        if u < 0:
            raise ValueExpectedException("u >= 0", f"u = {u}", src=self.__class__.__name__)
        if v < 0:
            raise ValueExpectedException("v >= 0", f"v = {v}", src=self.__class__.__name__)

    @property
    def name(self) -> Union[str, None]:
        """Название узла."""
        return self._name

    @name.setter
    def name(self, new_name: Union[str, None]):
        self._name = new_name

    @property
    def weight(self) -> int:
        """Вес ребра."""
        return self._weight

    @weight.setter
    def weight(self, w: int):
        self._weight = w

    @property
    def color(self) -> Tuple[int, int, int]:
        """Цвет ребра."""
        return self._color

    @color.setter
    def color(self, c: Tuple[int, int, int]):
        self._check_color(c)
        self._color = c

    def _check_color(self, c: Tuple[int, int, int]):
        for x in c:
            if not (0 <= x < 256):
                raise ValueExpectedException("color value [0; 255]", f"color value {x}", src=self.__class__.__name__)

    @property
    def id(self) -> int:
        """ID ребра."""
        return self._id

    def is_equal_to(self, other: 'Edge') -> bool:
        """Проверить на равенство вес ребра весу другого ребра.

        :param other: другое ребро.
        :return: Веса рёбер равны (*True*) или нет (*False*).
        """
        return self.weight == other.weight
