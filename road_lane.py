from typing import List
import numpy as np
import pandas as pd

from car import Car


class RoadLane:
    """Класс дорожной полосы.

    Свойства (*properties*):
       * possibleStates -- возможные состояния ячеек полосы;
       * capacity -- вместимость полосы;
       * cells -- клетки полосы.
    Методы:
       * addCar -- добавить машину на полосу;
       * rmCar -- убрать машину с полосы;
       * show -- вывести на экран (пока чисто для отладки).
    """

    _states = pd.Series(data=[0, 1], index=['empty', 'full'], dtype=pd.Int8Dtype)

    def __init__(self, capacity: int, cars: List[Car] = None):
        self._checkCapacity(capacity)

        self._capacity = capacity
        self._cars = cars

        self._initCells()

    def _initCells(self):
        if self._cars:
            self._updateCells()

    def _updateCells(self):
        self._cells = np.full(self.capacity, self.possibleStates['empty'])
        for car in self._cars:
            if car.pos < self.capacity:
                self._cells[car.pos] = self.possibleStates['full']

    def _checkCapacity(self, cap: int):
        if cap <= 0:
            raise ValueError(f"\tОшибка: {self.__class__.__name__}.capacity должна быть > 0!")

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * capacity: {self.capacity}\n" \
               f" * cells: {self.cells}"

    @property
    def possibleStates(self) -> pd.Series:
        return self._states

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def cells(self) -> np.ndarray:
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
        # Для отладки в основном
        import matplotlib.pyplot as plt

        positions = np.array([car.pos for car in self._cars])

        plt.figure('Road Lane', figsize=(6, 6))
        plt.scatter(positions, np.zeros_like(positions), color='black', marker='o')
        plt.show()
