"""
Алгоритм Евклида

Для быстрого вычисления наибольшего общего делителя двух чисел используют
алгоритм Евклида. Он построен на следующем соотношении:
НОД(a, b) = НОД(b, a % b).

Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).


Формат ввода:
Вводится два целых положительных числа.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 1
output: 1

Тест 2
input: 2
input: 1
output: 1

Тест 3
input: 2
input: 2
output: 2
"""


def gcd(a, b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input())
b = int(input())

print(gcd(a, b))
