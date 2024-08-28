"""
Факториалы

По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов:

0!, 1!, 2!, …, n!


Формат ввода:
Вводится число n.


Формат вывода:
Выведите последовательность факториалов, разделяя числа пробелами


Примеры:
Тест 1
input: 4
output: 1 1 2 6 24

Тест 2
input: 3
output: 1 1 2 6

Тест 3
input: 1
output: 1 1
"""
import itertools
import operator


print(
    1,
    *itertools.accumulate(
        range(
            1,
            int(input()) + 1
        ),
        operator.mul
    )
)
