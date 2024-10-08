"""
Система линейных уравнений-1

Даны вещественные числа a, b, c, d, e, f. Известно, что система линейных
уравнений:
ax + by = e
cx + dy = f
имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой
системы.


Формат ввода:
Вводятся шесть чисел a, b, c, d, e, f - коэффициенты уравнений системы.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 0
input: 0
input: 1
input: 3
input: 3
output: 3 3

Тест 2
input: 1
input: 2
input: 3
input: 4
input: -1
input: -1
output: 1 -1

Тест 3
input: 3
input: 5
input: 4
input: 4
input: 11
input: 12
output: 2 1
"""
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == 0:
    y = e / b
    x = (f - d * y) / c
    print(x, y)
elif b == 0:
    x = e / a
    y = (f - c * x) / d
    print(x, y)
elif c == 0:
    y = f / d
    x = (e - b * y) / a
    print(x, y)
elif d == 0:
    x = f / c
    y = (e - a * x) / b
    print(x, y)
elif a == 0 and d == 0:
    y = e / b
    x = f / c
    print(x, y)
elif b == 0 and c == 0:
    x = e / a
    y = f / d
    print(x, y)
else:
    y = (a * f - c * e) / (-1 * b * c + a * d)
    x = (e - b * y) / a
    print(x, y)
