"""
Произведение пятых степеней

На вход подаётся последовательность натуральных чисел длины n ≤ 1000.
Посчитайте произведение пятых степеней чисел в последовательности.


Формат ввода:
Вводится последовательность чисел.


Формат вывода:
Выведите ответ на задачу.


Примечания:
Для решения задачи используйте функцию reduce из модуля functools.


Примеры:
Тест 1
input: 1 1 1 2
output: 32

Тест 2
input: 2 1 1 2 2
output: 32768

Тест 3
input: 10 100 1000 10000 2
output: 3200000000000000000000000000000000000000000000000000
"""
import functools


print(
    functools.reduce(
        lambda x, y: x * y,
        map(
            lambda x: x**5,
            map(
                int,
                input().split()
            )
        )
    )
)
