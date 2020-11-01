from typing import List
import numpy as np
import pandas as pd

from car import Car
from ex import ValueExpectedException


class RoadLane:
    """Класс дорожной полосы.

    Свойства (*properties*):
       * possibleStates -- возможные состояния ячеек полосы;
       * capacity -- вместимость полосы;
       * cells -- клетки полосы.
    Методы:
       * addCar -- добавить машину на полосу;
       * rmCar -- убрать машину с полосы;
       * show -- вывести на экран (отладочный метод).
    Переопределённые методы:
       * __repr__.
    """

    _states = pd.Series(data=[0, 1], index=['empty', 'full'], dtype=pd.BooleanDtype)

    def __init__(self, capacity: int, cars: List[Car] = None):
        self._checkCapacity(capacity)

        self._capacity = capacity
        self._cars = cars

        self._initCells()
        if cars:
            self._updateCells()

    def _initCells(self):
        self._cells = np.full(self.capacity, self.possibleStates['empty'])

    def _updateCells(self):
        for car in self._cars:
            if car.pos < self.capacity:
                self._cells[car.pos] = self.possibleStates['full']
            else:
                self._cars.remove(car)

    def _checkCapacity(self, cap: int):
        if cap < 1:
            raise ValueExpectedException("capacity > 0", f"{cap}", src=self._checkCapacity.__name__)

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * capacity: {self.capacity}\n" \
               f" * cells: {self.cells}"

    @property
    def possibleStates(self) -> pd.Series:
        """Список возможных состояний клеток полосы."""
        return self._states

    @property
    def capacity(self) -> int:
        """Ёмкость полосы (максимальное количество объектов транспорта)."""
        return self._capacity

    @property
    def cells(self) -> np.ndarray:
        """Массив клеток полосы (текущее состояние полосы)."""
        return self._cells

    def addCar(self, car: Car, pos: int = 0) -> bool:
        """Добавить машину в полосу.

        :param car: машина, которую необходимо добавить в полосу.
        :param pos: позиция вставки (номер клетки).
        :return: Добавлена ли машина (*True*, если в ячейке есть место) или нет (*False*, если места в ячейке нет).
        """
        if self.cells[pos] == self.possibleStates['empty']:
            car.pos = pos
            self._cars.append(car)
            self._cells[pos] = self.possibleStates['full']
            return True
        return False

    def rmCar(self, car: Car):
        """Удалить указанную машину из списка машин на полосе.

        :param car: машина для удаления.
        """
        self._cars.remove(car)

    def show(self):
        """Вспомогательный (отладочный) метод отрисовки состояния полосы."""
        import matplotlib.pyplot as plt

        positions = np.array([car.pos for car in self._cars])

        plt.figure('Road Lane', figsize=(6, 6))
        plt.scatter(positions, np.zeros_like(positions), color='black', marker='o')
        plt.show()
