#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from triad_date import Date, Triad


def main() -> None:
    """Основная функция демонстрации"""
    print("=" * 50)
    print("Демонстрация возможностей классов Triad и Date")
    print("=" * 50)

    # Демонстрация класса Triad
    print("\n1. Демонстрация класса Triad:")
    print("-" * 30)

    triad1: Triad = Triad(10, 20, 30)
    print(f"Создан: {triad1}")

    triad1.increase_a()
    print(f"После увеличения A: {triad1}")

    triad1.increase_b()
    print(f"После увеличения B: {triad1}")

    triad1.increase_c()
    print(f"После увеличения C: {triad1}")

    triad1.increase_all()
    print(f"После увеличения всех полей: {triad1}")

    # Демонстрация класса Date
    print("\n2. Демонстрация класса Date:")
    print("-" * 30)

    date1: Date = Date(2023, 12, 31)
    print(f"Создана дата: {date1}")

    date1.increase_day()
    print(f"После увеличения дня: {date1}")

    date2: Date = Date(2023, 2, 28)
    print(f"\nСоздана дата: {date2}")
    date2.increase_day()
    print(f"После увеличения дня (невисокосный год): {date2}")

    date3: Date = Date(2024, 2, 28)  # 2024 - високосный год
    print(f"\nСоздана дата: {date3}")
    date3.increase_day()
    print(f"После увеличения дня (високосный год): {date3}")
    date3.increase_day()
    print(f"После еще одного увеличения дня: {date3}")

    # Увеличение на несколько дней
    print("\n3. Увеличение даты на несколько дней:")
    print("-" * 40)

    date4: Date = Date(2023, 1, 1)
    print(f"Начальная дата: {date4}")
    date4.increase_by_days(365)
    print(f"После увеличения на 365 дней: {date4}")

    # Демонстрация полиморфизма
    print("\n4. Демонстрация полиморфизма:")
    print("-" * 35)

    objects: list[Triad] = [Triad(1, 2, 3), Date(2023, 6, 15)]

    for obj in objects:
        print(f"\nОбъект: {obj}")
        obj.display()
        obj.increase_a()
        print(f"После увеличения первого поля: {obj}")
        obj.increase_b()
        print(f"После увеличения второго поля: {obj}")
        obj.increase_c()
        print(f"После увеличения третьего поля: {obj}")

    # Тестирование сеттеров и свойств
    print("\n5. Тестирование свойств:")
    print("-" * 25)

    date_test: Date = Date(2023, 5, 10)
    print(f"Исходная дата: {date_test}")
    print(f"Год: {date_test.year}")
    print(f"Месяц: {date_test.month}")
    print(f"День: {date_test.day}")

    date_test.year = 2024
    date_test.month = 12
    date_test.day = 25
    print(f"После изменения через свойства: {date_test}")

    # Тестирование обработки ошибок
    print("\n6. Тестирование обработки ошибок:")
    print("-" * 35)

    try:
        Date(2023, 13, 1)  # Неверный месяц
    except ValueError as e:
        print(f"Ошибка при создании даты: {e}")

    try:
        valid_date: Date = Date(2023, 12, 31)
        valid_date.day = 32  # Неверный день
    except ValueError as e:
        print(f"Ошибка при установке дня: {e}")

    print("\n" + "=" * 50)
    print("Демонстрация завершена!")
    print("=" * 50)


if __name__ == "__main__":
    main()
