#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Triad:
    """
    Класс Triad (Тройка чисел)
    """

    def __init__(self, a: int = 0, b: int = 0, c: int = 0) -> None:
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self) -> int:
        return self._a

    @a.setter
    def a(self, value: int) -> None:
        self._a = value

    @property
    def b(self) -> int:
        return self._b

    @b.setter
    def b(self, value: int) -> None:
        self._b = value

    @property
    def c(self) -> int:
        return self._c

    @c.setter
    def c(self, value: int) -> None:
        self._c = value

    def increase_a(self) -> None:
        """Увеличить поле A на 1"""
        self._a += 1

    def increase_b(self) -> None:
        """Увеличить поле B на 1"""
        self._b += 1

    def increase_c(self) -> None:
        """Увеличить поле C на 1"""
        self._c += 1

    def increase_all(self) -> None:
        """Увеличить все поля на 1"""
        self.increase_a()
        self.increase_b()
        self.increase_c()

    def edit(self) -> None:
        """Редактирование параметров через консоль"""
        try:
            self._a = int(input("Введите значение A: "))
            self._b = int(input("Введите значение B: "))
            self._c = int(input("Введите значение C: "))
        except ValueError:
            raise ValueError("Некорректный ввод. Ожидаются целые числа.")

    def __str__(self) -> str:
        return f"Triad: A={self._a}, B={self._b}, C={self._c}"


class Date(Triad):
    """
    Производный класс Date (Дата) от Triad
    """

    def __init__(self, year: int = 2000, month: int = 1, day: int = 1) -> None:
        super().__init__(year, month, day)
        self._validate_date()

    @property
    def year(self) -> int:
        return self._a

    @year.setter
    def year(self, value: int) -> None:
        self._a = value
        self._validate_date()

    @property
    def month(self) -> int:
        return self._b

    @month.setter
    def month(self, value: int) -> None:
        self._b = value
        self._validate_date()

    @property
    def day(self) -> int:
        return self._c

    @day.setter
    def day(self, value: int) -> None:
        self._c = value
        self._validate_date()

    def _validate_date(self) -> None:
        """Проверка корректности даты"""
        if self._b < 1 or self._b > 12:
            raise ValueError("Месяц должен быть от 1 до 12")

        days_in_month = self._get_days_in_month()
        if self._c < 1 or self._c > days_in_month:
            raise ValueError(f"День должен быть от 1 до {days_in_month}")

    def _get_days_in_month(self) -> int:
        """Получить количество дней в месяце"""
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Проверка на високосный год для февраля
        if self._b == 2 and self._is_leap_year():
            return 29

        return days_in_month[self._b - 1]

    def _is_leap_year(self) -> bool:
        """Проверка на високосный год"""
        year = self._a
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def increase_year(self) -> None:
        """Увеличить год на 1"""
        self._a += 1
        self._validate_date()

    def increase_month(self) -> None:
        """Увеличить месяц на 1"""
        self._b += 1
        if self._b > 12:
            self._b = 1
            self._a += 1
        self._validate_date()

    def increase_day(self) -> None:
        """Увеличить день на 1"""
        days_in_month = self._get_days_in_month()
        self._c += 1
        if self._c > days_in_month:
            self._c = 1
            self.increase_month()

    # Переопределение методов родительского класса
    def increase_a(self) -> None:
        """Увеличить год на 1"""
        self.increase_year()

    def increase_b(self) -> None:
        """Увеличить месяц на 1"""
        self.increase_month()

    def increase_c(self) -> None:
        """Увеличить день на 1"""
        self.increase_day()

    def increase_by_days(self, days: int) -> None:
        """Увеличить дату на n дней"""
        for _ in range(days):
            self.increase_day()

    def edit(self) -> None:
        """Редактирование даты через консоль"""
        try:
            year = int(input("Введите год: "))
            month = int(input("Введите месяц: "))
            day = int(input("Введите день: "))

            # Устанавливаем значения через свойства для валидации
            self.year = year
            self.month = month
            self.day = day

        except ValueError:
            raise ValueError("Некорректный ввод. Ожидаются целые числа.")

    def __str__(self) -> str:
        return f"Date: {self._c:02d}.{self._b:02d}.{self._a}"
