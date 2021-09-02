"""
XOR для произвольного числа аргументов определяется следующим образом:

xor(a₁, a₂, …, an) = xor(a₁, xor(a₂, xor(a₃, … xor(an))…)

XOR от n последовательностей A₁, …, An (Aᵢ = Aᵢ₁, …, Aᵢk) равных длин k  —  это
последовательность C = xor(A₁, …, An), такая, что:

cᵢ = xor(A₁ᵢ, … Anᵢ)

Посчитайте XOR от n последовательностей равной длины k.


Формат ввода:
На первой строке записано число 2≤n≤1000  —  количество последовательностей.

На последующих n строках записаны последовательности A₁, …, An из 0 и 1,
разделённых пробелами равной длины 1≤k≤1000.


Формат вывода:
Выведите последовательность C = xor(A₁, …, An), разделяя числа
последовательности пробелами.


Примеры:
Тест 1
>>> 2
>>> 0 0 1 1
>>> 0 1 0 1
0 1 1 0

Тест 2
>>> 3
>>> 0 0 0 0
>>> 1 1 1 1
>>> 0 1 0 1
1 0 1 0

Тест 3
>>> 4
>>> 0 0 1 0 1 0 1 0 0 0 1
>>> 1 0 1 1 1 0 0 0 1 1 1
>>> 1 1 1 1 0 0 0 1 0 1 0
>>> 0 0 0 1 1 1 0 0 0 0 0
0 1 1 1 1 1 1 1 1 0 0
"""

from functools import reduce

print(
    *map(
        lambda x: reduce(
            lambda a, b: a ^ b, x
        ),
        zip(
            *map(
                lambda x: map(
                    int,
                    input().split()
                ),
                range(
                    int(
                        input()
                    )
                )
            )
        )
    )
)
