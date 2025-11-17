#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from triad_date import Date, Triad


def main():
    print("=" * 50)
    print("Демонстрация возможностей классов Triad и Date")
    print("=" * 50)

    # Демонстрация класса Triad
    print("\n1. Демонстрация класса Triad:")
    print("-" * 30)

    triad1 = Triad(10, 20, 30)
    print(triad1)

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

    date1 = Date(2023, 12, 31)
    print(date1)

    date1.increase_day()
    print(f"После увеличения дня: {date1}")

    date2 = Date(2023, 2, 28)
    print(f"\nСоздана дата: {date2}")
    date2.increase_day()
    print(f"После увеличения дня (невисокосный год): {date2}")

    date3 = Date(2024, 2, 28)
    print(f"\nСоздана дата: {date3}")
    date3.increase_day()
    print(f"После увеличения дня (високосный год): {date3}")
    date3.increase_day()
    print(f"После еще одного увеличения дня: {date3}")

    # Увеличение на несколько дней
    print("\n3. Увеличение даты на несколько дней:")
    print("-" * 40)

    date4 = Date(2023, 1, 1)
    print(f"Начальная дата: {date4}")
    date4.increase_by_days(365)
    print(f"После увеличения на 365 дней: {date4}")

    # Демонстрация полиморфизма
    print("\n4. Демонстрация полиморфизма:")
    print("-" * 35)

    objects = [Triad(1, 2, 3), Date(2023, 6, 15)]

    for obj in objects:
        print(f"\nОбъект: {obj}")
        obj.increase_a()
        print(f"После увеличения первого поля: {obj}")
        obj.increase_b()
        print(f"После увеличения второго поля: {obj}")
        obj.increase_c()
        print(f"После увеличения третьего поля: {obj}")


if __name__ == "__main__":
    main()
