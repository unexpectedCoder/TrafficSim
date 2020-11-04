from abc import ABC
from typing import Tuple, Union
from uuid import UUID, uuid4

from ex import ValueExpectedException


class Edge(ABC):
    def __init__(self, u: int, v: int, **kwargs):
        self.uv = u, v
        self.name = kwargs['name'] if 'name' in kwargs else None
        self.weight = kwargs['weight'] if 'weight' in kwargs else 0
        self.color = kwargs['color'] if 'color' in kwargs else (0, 0, 0)
        self._uuid = kwargs['uuid'] if 'uuid' in kwargs else uuid4()

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * uv: {self.uv}\n" \
               f" * name: {self.name}\n" \
               f" * weight: {self.weight}\n" \
               f" * color (RGB): {self.color}\n" \
               f" * uuid: {self.uuid}"

    def __hash__(self):
        return self.uuid

    @property
    def uv(self) -> Tuple[int, int]:
        """Направление ребра -- от ``u`` к ``v``."""
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
    def uuid(self) -> UUID:
        """UUID ребра."""
        return self._uuid

    def is_equal_to(self, other: 'Edge') -> bool:
        """Проверить на равенство веса ребра весу другого ребра.

        :param other: другое ребро.
        :return: Веса рёбер равны (*True*) или нет (*False*).
        """
        return self.weight == other.weight
