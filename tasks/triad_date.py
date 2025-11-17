#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Triad:
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
        self._a += 1

    def increase_b(self) -> None:
        self._b += 1

    def increase_c(self) -> None:
        self._c += 1

    def increase_all(self) -> None:
        self.increase_a()
        self.increase_b()
        self.increase_c()

    def __str__(self) -> str:
        return f"Triad: A={self._a}, B={self._b}, C={self._c}"


class Date(Triad):
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
        if self._b < 1 or self._b > 12:
            raise ValueError("Месяц должен быть от 1 до 12")

        days_in_month = self._get_days_in_month()
        if self._c < 1 or self._c > days_in_month:
            raise ValueError(f"День должен быть от 1 до {days_in_month}")

    def _get_days_in_month(self) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self._b == 2 and self._is_leap_year():
            return 29

        return days_in_month[self._b - 1]

    def _is_leap_year(self) -> bool:
        year = self._a
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def increase_year(self) -> None:
        self._a += 1
        self._validate_date()

    def increase_month(self) -> None:
        self._b += 1
        if self._b > 12:
            self._b = 1
            self._a += 1
        self._validate_date()

    def increase_day(self) -> None:
        days_in_month = self._get_days_in_month()
        self._c += 1
        if self._c > days_in_month:
            self._c = 1
            self.increase_month()

    def increase_a(self) -> None:
        self.increase_year()

    def increase_b(self) -> None:
        self.increase_month()

    def increase_c(self) -> None:
        self.increase_day()

    def increase_by_days(self, days: int) -> None:
        for _ in range(days):
            self.increase_day()

    def __str__(self) -> str:
        return f"Date: {self._c:02d}.{self._b:02d}.{self._a}"
