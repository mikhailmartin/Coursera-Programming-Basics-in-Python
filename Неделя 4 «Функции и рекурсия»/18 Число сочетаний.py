"""
Число сочетаний

По данным целым числам n и k (0 ≤ k ≤ n) вычислите C из n по k.

Решение оформите в виде функции C(n, k).

Для решения используйте рекуррентное соотношение:
C^K_N = C^K_{N-1} + C^{K-1}_{N-1}

И равенств:
С(n, 1) = n
C(n, n) = 1


Формат ввода:
Вводятся удовлетворяющие условию задачи числа n и k.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 4
input: 2
output: 6

Тест 2
input: 4
input: 3
output: 4

Тест 3
input: 4
input: 1
output: 4
"""


def C(a, b):
    return int(fact(a) / (fact(a - b) * fact(b)))


def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)


n = int(input())
k = int(input())

print(C(n, k))
