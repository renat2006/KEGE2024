"""
Исполнитель обрабатывает двоичные числа. У него есть три команды, которым присвоены номера:

прибавь 1
припиши справа 0
припиши справа 1
Программа для исполнителя – это последовательность команд. Первая команда увеличивает число на 1. Вторая команда приписывает к двоичной записи числа ноль справа. Например, число 101 преобразуется в число 1010. Третья команда приписывает к двоичной записи числа единицу справа. Например, число 101 преобразуется в число 1011.

Сколько существует программ, которые число 102 преобразуют в число 100002?
"""
import math
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


@lru_cache(None)
def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c + 1, e) + f(c * 2, e) + f(c * 2 + 1, e)


print(f(int("10", 2), int("10000", 2)))
