from typing import List
import numpy as np
import pandas as pd

from car import Car
from ex import ValueExpectedException


class RoadLane:
    """Класс дорожной полосы.

    Свойства (*properties*):
       * cars -- список машин на полосе;
       * possibleStates -- возможные состояния ячеек полосы;
       * capacity -- вместимость полосы;
       * cells -- клетки полосы.
    Методы:
       * update -- обновить состояние полосы как клеточного автомата;
       * addCar -- добавить машину на полосу;
       * rmCar -- убрать машину с полосы;
       * show -- вывести на экран (отладочный метод).
    Переопределённые методы:
       * __repr__.
    Выбрасывает:
       * ``ValueExpectedException``.
    """
    _states = pd.Series(data=[0, 1], index=['empty', 'full'], dtype=pd.Int8Dtype)

    def __init__(self, capacity: int = 1, cars: List[Car] = None):
        self._checkCapacity(capacity)

        self._capacity = capacity
        self._cars = cars.copy() if cars else []

        self._initCells()
        self._updateCarsList()
        self._updateCells()

    def _checkCapacity(self, cap: int):
        if cap < 1:
            raise ValueExpectedException("capacity > 0", f"capacity = {cap}", src='capacity')

    def _initCells(self):
        # Инициализировать/переинициализировать массив клеток
        self._cells = np.full(self.capacity, self.possibleStates['empty'])

    def _updateCarsList(self):
        # Обновить список машин
        if self.cars:
            for car in self.cars:
                if car.pos < self.capacity:
                    self.cells[car.pos] = self.possibleStates['full']
                else:
                    self.cars.remove(car)

    def _updateCells(self):
        # Обновить значения всех клеток согласно списку машин
        self._initCells()
        if self.cars:
            for car in self.cars:
                self._cells[car.pos] = self.possibleStates['full']

    def __repr__(self):
        return f"{self.__class__.__name__}:\n" \
               f" * capacity: {self.capacity}\n" \
               f" * cells: {self.cells}"

    @property
    def possibleStates(self) -> pd.Series:
        """Список возможных состояний клеток полосы."""
        return self._states

    @property
    def cars(self) -> List[Car]:
        """Список машин на полосе."""
        return self._cars

    @cars.setter
    def cars(self, c: List[Car]):
        self._cars = c.copy()
        self._updateCells()

    @property
    def capacity(self) -> int:
        """Ёмкость полосы (максимальное количество объектов транспорта)."""
        return self._capacity

    @capacity.setter
    def capacity(self, cap: int):
        self._checkCapacity(cap)
        self._capacity = cap
        # Обновить состояние клеток и список авто, т.к. на них влияет изменение capacity
        self._initCells()
        self._updateCarsList()
        self._updateCells()

    @property
    def cells(self) -> np.ndarray:
        """Массив клеток полосы (текущее состояние полосы)."""
        return self._cells

    def update(self):
        """Обновить состояние полосы (шаг эволюции полосы как клеточного автомата)."""
        for car in self.cars:
            if car.pos < self.capacity - 1:
                if self.cells[car.pos + 1] == self.possibleStates['empty']:    # если следующая клетка дороги пуста
                    self.cells[car.pos] = self.possibleStates['empty']
                    car.pos += 1
                    self.cells[car.pos] = self.possibleStates['full']
            else:
                pass  # TODO передача в объекта car в обёект перекрёстка

    def addCar(self, car: Car, pos: int = 0) -> bool:
        """Добавить машину в полосу.

        :param car: машина, которую необходимо добавить в полосу.
        :param pos: позиция вставки (номер клетки).
        :return: Добавлена ли машина (*True*, если в ячейке есть место) или нет (*False*, если места в ячейке нет).
        """
        if self.cells[pos] == self.possibleStates['empty']:
            car.pos = pos
            self.cars.append(car)
            self.cells[pos] = self.possibleStates['full']
            return True
        return False

    def rmCar(self, car: Car):
        """Удалить указанную машину из списка машин на полосе.

        :param car: машина для удаления.
        """
        self.cars.remove(car)
        self._updateCells()

    def show(self):
        """Вспомогательный (отладочный) метод отрисовки состояния полосы."""
        import matplotlib.pyplot as plt

        positions = np.array([car.pos for car in self.cars])

        plt.figure('Road Lane', figsize=(12, 3))
        plt.scatter(positions + 1, np.zeros_like(positions), color='black', marker='o')
        plt.xlim(0, self.capacity)
        plt.xticks([i for i in range(self.capacity)])
        plt.grid(True)
        plt.show()
