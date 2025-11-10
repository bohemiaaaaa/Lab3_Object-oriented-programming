#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from series_package.series import Exponential, Linear, Series
from triad_date import Date, Triad


class TestTriad:
    """Тесты для класса Triad (Задание 1)"""

    def test_triad_initialization(self):
        """Тест инициализации Triad"""
        triad = Triad(1, 2, 3)
        assert triad.a == 1
        assert triad.b == 2
        assert triad.c == 3

    def test_triad_default_values(self):
        """Тест значений по умолчанию"""
        triad = Triad()
        assert triad.a == 0
        assert triad.b == 0
        assert triad.c == 0

    def test_triad_increase_a(self):
        """Тест увеличения поля A"""
        triad = Triad(1, 2, 3)
        triad.increase_a()
        assert triad.a == 2
        assert triad.b == 2
        assert triad.c == 3

    def test_triad_increase_b(self):
        """Тест увеличения поля B"""
        triad = Triad(1, 2, 3)
        triad.increase_b()
        assert triad.a == 1
        assert triad.b == 3
        assert triad.c == 3

    def test_triad_increase_c(self):
        """Тест увеличения поля C"""
        triad = Triad(1, 2, 3)
        triad.increase_c()
        assert triad.a == 1
        assert triad.b == 2
        assert triad.c == 4

    def test_triad_increase_all(self):
        """Тест увеличения всех полей"""
        triad = Triad(1, 2, 3)
        triad.increase_all()
        assert triad.a == 2
        assert triad.b == 3
        assert triad.c == 4

    def test_triad_string_representation(self):
        """Тест строкового представления"""
        triad = Triad(1, 2, 3)
        expected = "Triad: A=1, B=2, C=3"
        assert str(triad) == expected

    def test_triad_properties(self):
        """Тест свойств (property)"""
        triad = Triad()
        triad.a = 10
        triad.b = 20
        triad.c = 30
        assert triad.a == 10
        assert triad.b == 20
        assert triad.c == 30


class TestDate:
    """Тесты для класса Date (Задание 1)"""

    def test_date_initialization(self):
        """Тест инициализации Date"""
        date = Date(2023, 12, 31)
        assert date.year == 2023
        assert date.month == 12
        assert date.day == 31

    def test_date_default_values(self):
        """Тест значений по умолчанию"""
        date = Date()
        assert date.year == 2000
        assert date.month == 1
        assert date.day == 1

    def test_date_invalid_month(self):
        """Тест неверного месяца"""
        with pytest.raises(ValueError, match="Месяц должен быть от 1 до 12"):
            Date(2023, 13, 1)

    def test_date_invalid_day(self):
        """Тест неверного дня"""
        with pytest.raises(ValueError):
            Date(2023, 1, 32)

    def test_date_increase_year(self):
        """Тест увеличения года"""
        date = Date(2023, 6, 15)
        date.increase_year()
        assert date.year == 2024
        assert date.month == 6
        assert date.day == 15

    def test_date_increase_month(self):
        """Тест увеличения месяца"""
        date = Date(2023, 6, 15)
        date.increase_month()
        assert date.year == 2023
        assert date.month == 7
        assert date.day == 15

    def test_date_increase_month_year_boundary(self):
        """Тест увеличения месяца через границу года"""
        date = Date(2023, 12, 15)
        date.increase_month()
        assert date.year == 2024
        assert date.month == 1
        assert date.day == 15

    def test_date_increase_day(self):
        """Тест увеличения дня"""
        date = Date(2023, 6, 15)
        date.increase_day()
        assert date.year == 2023
        assert date.month == 6
        assert date.day == 16

    def test_date_increase_day_month_boundary(self):
        """Тест увеличения дня через границу месяца"""
        date = Date(2023, 6, 30)
        date.increase_day()
        assert date.year == 2023
        assert date.month == 7
        assert date.day == 1

    def test_date_leap_year_february(self):
        """Тест високосного года для февраля"""
        date = Date(2024, 2, 28)  # 2024 - високосный
        date.increase_day()
        assert date.year == 2024
        assert date.month == 2
        assert date.day == 29

    def test_date_non_leap_year_february(self):
        """Тест невисокосного года для февраля"""
        date = Date(2023, 2, 28)  # 2023 - невисокосный
        date.increase_day()
        assert date.year == 2023
        assert date.month == 3
        assert date.day == 1

    def test_date_increase_by_days(self):
        """Тест увеличения на несколько дней"""
        date = Date(2023, 1, 1)
        date.increase_by_days(5)
        assert date.year == 2023
        assert date.month == 1
        assert date.day == 6

    def test_date_string_representation(self):
        """Тест строкового представления"""
        date = Date(2023, 6, 15)
        expected = "Date: 15.06.2023"
        assert str(date) == expected

    def test_date_inheritance(self):
        """Тест наследования от Triad"""
        date = Date(2023, 6, 15)
        assert isinstance(date, Triad)

        # Проверка полиморфизма
        date.increase_a()  # Должен увеличить год
        assert date.year == 2024


class TestLinear:
    """Тесты для класса Linear (Задание 2)"""

    def test_linear_initialization(self):
        """Тест инициализации Linear"""
        linear = Linear(2.0, 3.0)
        assert linear.first_element == 2.0
        assert linear.difference == 3.0

    def test_linear_default_values(self):
        """Тест значений по умолчанию"""
        linear = Linear()
        assert linear.first_element == 0.0
        assert linear.difference == 0.0

    def test_linear_get_element(self):
        """Тест вычисления элемента арифметической прогрессии"""
        linear = Linear(2.0, 3.0)
        assert linear.get_element(0) == 2.0  # a0
        assert linear.get_element(1) == 5.0  # a1 = 2 + 3
        assert linear.get_element(2) == 8.0  # a2 = 2 + 2*3
        assert linear.get_element(3) == 11.0  # a3 = 2 + 3*3

    def test_linear_get_element_negative_index(self):
        """Тест вычисления элемента с отрицательным индексом"""
        linear = Linear(2.0, 3.0)
        with pytest.raises(ValueError, match="Индекс j должен быть неотрицательным"):
            linear.get_element(-1)

    def test_linear_get_sum(self):
        """Тест вычисления суммы арифметической прогрессии"""
        linear = Linear(2.0, 3.0)
        # S4 = 5 * (2 + 14) / 2 = 5 * 16 / 2 = 40
        assert linear.get_sum(4) == 40.0

    def test_linear_get_sum_negative_n(self):
        """Тест вычисления суммы с отрицательным n"""
        linear = Linear(2.0, 3.0)
        with pytest.raises(
            ValueError, match="Количество элементов n должно быть неотрицательным"
        ):
            linear.get_sum(-1)

    def test_linear_string_representation(self):
        """Тест строкового представления"""
        linear = Linear(2.0, 3.0)
        expected = "Арифметическая прогрессия: a0=2.0, d=3.0"
        assert str(linear) == expected

    def test_linear_properties(self):
        """Тест свойств (property)"""
        linear = Linear()
        linear.first_element = 5.0
        linear.difference = 2.0
        assert linear.first_element == 5.0
        assert linear.difference == 2.0


class TestExponential:
    """Тесты для класса Exponential (Задание 2)"""

    def test_exponential_initialization(self):
        """Тест инициализации Exponential"""
        exponential = Exponential(2.0, 3.0)
        assert exponential.first_element == 2.0
        assert exponential.ratio == 3.0

    def test_exponential_default_values(self):
        """Тест значений по умолчанию"""
        exponential = Exponential()
        assert exponential.first_element == 0.0
        assert exponential.ratio == 1.0

    def test_exponential_get_element(self):
        """Тест вычисления элемента геометрической прогрессии"""
        exponential = Exponential(2.0, 3.0)
        assert exponential.get_element(0) == 2.0  # a0
        assert exponential.get_element(1) == 6.0  # a1 = 2 * 3
        assert exponential.get_element(2) == 18.0  # a2 = 2 * 3^2
        assert exponential.get_element(3) == 54.0  # a3 = 2 * 3^3

    def test_exponential_get_element_negative_index(self):
        """Тест вычисления элемента с отрицательным индексом"""
        exponential = Exponential(2.0, 3.0)
        with pytest.raises(ValueError, match="Индекс j должен быть неотрицательным"):
            exponential.get_element(-1)

    def test_exponential_get_sum(self):
        """Тест вычисления суммы геометрической прогрессии"""
        exponential = Exponential(2.0, 3.0)
        # S4 = (2 - 162*3) / (1-3) = (2 - 486) / (-2) = (-484) / (-2) = 242
        assert exponential.get_sum(4) == 242.0

    def test_exponential_get_sum_ratio_one(self):
        """Тест вычисления суммы при r=1"""
        exponential = Exponential(2.0, 1.0)
        # S4 = 2 * (4 + 1) = 10
        assert exponential.get_sum(4) == 10.0

    def test_exponential_get_sum_negative_n(self):
        """Тест вычисления суммы с отрицательным n"""
        exponential = Exponential(2.0, 3.0)
        with pytest.raises(
            ValueError, match="Количество элементов n должно быть неотрицательным"
        ):
            exponential.get_sum(-1)

    def test_exponential_string_representation(self):
        """Тест строкового представления"""
        exponential = Exponential(2.0, 3.0)
        expected = "Геометрическая прогрессия: a0=2.0, r=3.0"
        assert str(exponential) == expected

    def test_exponential_properties(self):
        """Тест свойств (property)"""
        exponential = Exponential()
        exponential.first_element = 5.0
        exponential.ratio = 2.0
        assert exponential.first_element == 5.0
        assert exponential.ratio == 2.0


class TestSeriesInheritance:
    """Тесты наследования и полиморфизма для Series (Задание 2)"""

    def test_series_abstract_class(self):
        """Тест, что Series является абстрактным классом"""
        with pytest.raises(TypeError):
            Series()  # Нельзя создать экземпляр абстрактного класса

    def test_linear_inheritance(self):
        """Тест наследования Linear от Series"""
        linear = Linear()
        assert isinstance(linear, Series)

    def test_exponential_inheritance(self):
        """Тест наследования Exponential от Series"""
        exponential = Exponential()
        assert isinstance(exponential, Series)

    def test_polymorphism(self):
        """Тест полиморфизма через базовый класс Series"""
        series_list = [Linear(2.0, 3.0), Exponential(2.0, 3.0)]

        # Все объекты должны иметь методы абстрактного класса
        for series in series_list:
            assert hasattr(series, "get_element")
            assert hasattr(series, "get_sum")
            assert hasattr(series, "edit")
            assert hasattr(series, "__str__")

            # Проверка, что методы работают
            element = series.get_element(2)
            sum_val = series.get_sum(2)
            assert isinstance(element, float)
            assert isinstance(sum_val, float)
