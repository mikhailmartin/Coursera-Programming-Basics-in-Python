"""
Даны два натуральных числа n и m.

Сократите дробь (n / m), то есть выведите два других числа p и q таких, что
(n / m) = (p / q) и дробь (p / q) — несократимая.

Решение оформите в виде функции ReduceFraction(n, m), получающая значения n и m
и возвращающей кортеж из двух чисел: return p, q.

Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).


Формат ввода:
Вводятся два натуральных числа.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 12
>>> 16
3 4

Тест 2
>>> 7
>>> 9
7 9

Тест 3
>>> 10
>>> 100
1 10
"""


def gcd(a, b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        return gcd(b, a % b)


def reduce_fraction(a, b):
    return a // gcd(a, b), b // gcd(a, b)


def main():
    n = int(input())
    m = int(input())
    print(*reduce_fraction(n, m))


main()
