#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from series_package.series import (
    Exponential,
    Linear,
    SeriesReader,
    demonstrate_virtual_call,
)


def main():
    print("=" * 60)
    print("Демонстрация абстрактных классов Series")
    print("Арифметическая и геометрическая прогрессии")
    print("=" * 60)

    # Демонстрация арифметической прогрессии
    print("\n1. Арифметическая прогрессия (Linear):")
    print("-" * 40)

    linear = Linear(2.0, 3.0)
    print(linear)

    print("Элементы прогрессии:")
    for j in range(5):
        print(f"  a_{j} = {linear.get_element(j)}")

    n = 4
    print(f"\nСумма первых {n+1} элементов: {linear.get_sum(n)}")
    print("Проверка: 2 + 5 + 8 + 11 + 14 = 40")

    # Демонстрация геометрической прогрессии
    print("\n2. Геометрическая прогрессия (Exponential):")
    print("-" * 40)

    exponential = Exponential(2.0, 3.0)
    print(exponential)

    print("Элементы прогрессии:")
    for j in range(5):
        print(f"  a_{j} = {exponential.get_element(j)}")

    n = 4
    print(f"\nСумма первых {n+1} элементов: {exponential.get_sum(n)}")
    print("Проверка: 2 + 6 + 18 + 54 + 162 = 242")

    # Демонстрация виртуальных вызовов через функцию
    print("\n3. Демонстрация виртуальных вызовов:")
    print("-" * 40)

    series_list = [
        Linear(1.0, 2.0),
        Exponential(1.0, 2.0),
    ]

    for i, series in enumerate(series_list, 1):
        print(f"Прогрессия {i}:")
        demonstrate_virtual_call(series, j=3, n=4)

    # Демонстрация ввода с клавиатуры через SeriesReader
    print("\n4. Демонстрация ввода с клавиатуры через SeriesReader:")
    print("-" * 50)

    try:
        reader = SeriesReader()

        print("Создание арифметической прогрессии:")
        linear_input = reader.read_linear()
        print(f"Создана арифметическая прогрессия: {linear_input}")
        print(f"a_5 = {linear_input.get_element(5)}")
        print(f"S_5 = {linear_input.get_sum(5)}")

        print("\nСоздание геометрической прогрессии:")
        exponential_input = reader.read_exponential()
        print(f"Создана геометрическая прогрессия: {exponential_input}")
        print(f"a_5 = {exponential_input.get_element(5)}")
        print(f"S_5 = {exponential_input.get_sum(5)}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

    # Демонстрация полиморфизма
    print("\n5. Демонстрация полиморфизма:")
    print("-" * 40)

    progressions = [
        Linear(5.0, 2.0),
        Exponential(5.0, 2.0),
        Linear(10.0, -1.0),
        Exponential(10.0, 0.5),
    ]

    for progression in progressions:
        print(progression)
        print(f"  a_3 = {progression.get_element(3):.2f}")
        print(f"  S_3 = {progression.get_sum(3):.2f}")
        print()


if __name__ == "__main__":
    main()
