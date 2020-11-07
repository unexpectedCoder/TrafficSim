from typing import Dict, List, Tuple
import numpy as np

from ex import ValueExpectedException
from abstract import Edge
from car import Car


class Road(Edge):
    """Класс дороги.

    Свойства:
       * *possible_states* -- возможные состояния ячеек дороги;
       * *cars* (имеет setter) -- список всех машин на дороге;
       * *lane_capacity* (имеет setter) -- вместимость каждой полосы дороги;
       * *cells* -- текущий массив (матрица) ячеек дороги;
       * *n_lanes* (имеет setter) -- количество полос на дороге.
    Методы:
       * *update* -- обновить состояние дороги как клеточного автомата;
       * *addCar* -- добавить объект ``Car`` в заданную позицию на дороге;
       * *rmCar* -- удалить указанный объект ``Car`` из списка машин на дороге.
    Переопределяет:
       * *__repr__*.
    """
    _states = {'empty': 0, 'full': 1}

    def __init__(self, fr: int, to: int, lane_capacity: int, cars: List[Car],
                 name: str = None, n_lanes: int = 1, color: Tuple[int, int, int] = (0, 0, 0)):
        self._check_lane_capacity(lane_capacity)

        Edge.__init__(self, fr, to, name=name, weight=lane_capacity, color=color)
        self.__hash__ = Edge.__hash__
        self.__eq__ = Edge.__eq__

        self._cars = cars.copy() if cars else []
        self._n_lanes = n_lanes

        self._init_cells()
        self._update_cars_list()
        self._update_cells()

    def _check_lane_capacity(self, cap: int):
        if cap < 1:
            raise ValueExpectedException("lane_capacity > 0", f"lane_capacity = {cap}",
                                         src=self.__class__.__name__)

    def _init_cells(self):
        # Инициализировать/переинициализировать массив клеток
        self._cells = np.full([self.n_lanes, self.lane_capacity], self.possible_states['empty'])

    def _update_cars_list(self):
        # Обновить список машин
        if self.cars:
            for car in self.cars:
                if car.pos[0] < self.n_lanes and car.pos[1] < self.lane_capacity:
                    self.cells[car.pos[0], car.pos[1]] = self.possible_states['full']
                else:
                    self.cars.remove(car)

    def _update_cells(self):
        # Обновить значения всех клеток согласно списку машин
        self._init_cells()
        if self.cars:
            for car in self.cars:
                self.cells[car.pos[0], car.pos[1]] = self.possible_states['full']

    def __repr__(self):
        res = Edge.__repr__(self) + '\n'
        return res + f" * n_lanes: {self.n_lanes}\n" \
                     f" * len(cars): {len(self.cars)}"

    @property
    def possible_states(self) -> Dict[str, int]:
        """Список возможных состояний клеток полосы."""
        return self._states

    @property
    def cars(self) -> List[Car]:
        """Список машин на полосе."""
        return self._cars

    @cars.setter
    def cars(self, c: List[Car]):
        self._cars = c.copy()
        self._update_cells()

    @property
    def lane_capacity(self) -> int:
        """Ёмкость полосы (максимальное количество объектов транспорта)."""
        return self.weight

    @lane_capacity.setter
    def lane_capacity(self, cap: int):
        self._check_lane_capacity(cap)
        self.weight = cap
        # Обновить состояние клеток и список авто, т.к. на них влияет изменение capacity
        self._init_cells()
        self._update_cars_list()
        self._update_cells()

    @property
    def cells(self) -> np.ndarray:
        """Массив клеток полосы (текущее состояние полосы)."""
        return self._cells

    @property
    def n_lanes(self) -> int:
        """Количество полос в дороге из ``u`` в ``v``."""
        return self._n_lanes

    @n_lanes.setter
    def n_lanes(self, n: int):
        self._check_n_lanes(n)
        self._n_lanes = n

    def _check_n_lanes(self, n: int):
        if n < 1:
            raise ValueExpectedException("lanes >= 1", f"lanes = {n}", src=self.__class__.__name__)

    def update(self):
        """Обновить состояние полосы (шаг эволюции полосы как клеточного автомата)."""
        for car in self.cars:
            if not self._is_eof_lane(car):
                if self._is_next_cell_empty(car):
                    self.cells[car.pos[0], car.pos[1]] = self.possible_states['empty']
                    car.pos[1] += 1
                    self.cells[car.pos[0], car.pos[1]] = self.possible_states['full']
            else:
                pass  # TODO передача в объекта car в обёект перекрёстка

    def _is_eof_lane(self, car: Car) -> bool:
        if car.pos[1] < self.lane_capacity - 1:
            return False
        return True

    def _is_next_cell_empty(self, car: Car) -> bool:
        if self.cells[car.pos[0], car.pos[1] + 1] == self.possible_states['empty']:
            return True
        return False

    def addCar(self, car: Car, pos: Tuple[int, int] = (0, 0)) -> bool:
        """Добавить машину в полосу.

        :param car: машина, которую необходимо добавить в полосу.
        :param pos: позиция вставки (номер клетки).
        :return: Добавлена ли машина (*True*, если в ячейке есть место) или нет (*False*, если места в ячейке нет).
        """
        if self.cells[pos[0], pos[1]] == self.possible_states['empty']:
            car.pos = pos
            self.cars.append(car)
            self.cells[pos[0], pos[1]] = self.possible_states['full']
            return True
        return False

    def rmCar(self, car: Car):
        """Удалить указанную машину из списка машин на полосе.

        :param car: машина для удаления.
        """
        self.cars.remove(car)
        self._update_cells()


if __name__ == '__main__':
    print(Road(1, 2, 30, [], name='Wall Street', n_lanes=2))

    u, v = 1, 2
    capacity = 30
    lanes = 4
    n = 10
    cars = [Car(pos=(i, j)) for i in range(0, lanes) for j in range(0, n, 2)]

    for car in cars:
        print(car)

    r = Road(u, v, capacity, cars, name='Wall Street', n_lanes=lanes)
    print(r)
    print(r.cells)
