#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Series(ABC):
    def __init__(self, first_element: float = 0.0) -> None:
        self._a0 = first_element

    @property
    def first_element(self) -> float:
        return self._a0

    @first_element.setter
    def first_element(self, value: float) -> None:
        self._a0 = value

    @abstractmethod
    def get_element(self, j: int) -> float:
        pass

    @abstractmethod
    def get_sum(self, n: int) -> float:
        pass

    @abstractmethod
    def edit(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Linear(Series):
    def __init__(self, first_element: float = 0.0, difference: float = 0.0) -> None:
        super().__init__(first_element)
        self._d = difference

    @property
    def difference(self) -> float:
        return self._d

    @difference.setter
    def difference(self, value: float) -> None:
        self._d = value

    def get_element(self, j: int) -> float:
        if j < 0:
            raise ValueError("Индекс j должен быть неотрицательным")
        return self._a0 + j * self._d

    def get_sum(self, n: int) -> float:
        if n < 0:
            raise ValueError("Количество элементов n должно быть неотрицательным")

        a_n = self.get_element(n)
        return (n + 1) * (self._a0 + a_n) / 2

    def edit(self) -> None:
        try:
            self._a0 = float(input("Введите первый элемент a0: "))
            self._d = float(input("Введите разность d: "))
        except ValueError:
            raise ValueError("Некорректный ввод. Ожидаются числа.")

    def __str__(self) -> str:
        return f"Арифметическая прогрессия: a0={self._a0}, d={self._d}"


class Exponential(Series):
    def __init__(self, first_element: float = 0.0, ratio: float = 1.0) -> None:
        super().__init__(first_element)
        self._r = ratio

    @property
    def ratio(self) -> float:
        return self._r

    @ratio.setter
    def ratio(self, value: float) -> None:
        self._r = value

    def get_element(self, j: int) -> float:
        if j < 0:
            raise ValueError("Индекс j должен быть неотрицательным")
        return self._a0 * (self._r**j)

    def get_sum(self, n: int) -> float:
        if n < 0:
            raise ValueError("Количество элементов n должно быть неотрицательным")
        if self._r == 1:
            return self._a0 * (n + 1)

        a_n = self.get_element(n)
        return (self._a0 - a_n * self._r) / (1 - self._r)

    def edit(self) -> None:
        try:
            self._a0 = float(input("Введите первый элемент a0: "))
            self._r = float(input("Введите знаменатель r: "))
        except ValueError:
            raise ValueError("Некорректный ввод. Ожидаются числа.")

    def __str__(self) -> str:
        return f"Геометрическая прогрессия: a0={self._a0}, r={self._r}"


def demonstrate_virtual_call(series: Series, j: int, n: int) -> None:
    print("\n" + "=" * 50)
    print("Демонстрация виртуального вызова:")
    print("=" * 50)

    print(series)
    print(f"Элемент с индексом {j}: {series.get_element(j)}")
    print(f"Сумма первых {n+1} элементов: {series.get_sum(n)}")

    print("Первые 5 элементов прогрессии:")
    for i in range(5):
        print(f"  a_{i} = {series.get_element(i)}")
