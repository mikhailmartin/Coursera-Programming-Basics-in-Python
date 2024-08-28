"""
Длина отрезка

Даны четыре действительных числа: x₁, y₁, x₂, y₂. Напишите функцию
distance(x1, y1, x2, y2), вычисляющую расстояние между точками (x₁, y₁) и
(x₂, y₂). Считайте четыре действительных числа и выведите результат работы
этой функции.


Формат ввода:
Вводятся четыре действительных числа.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 0
input: 0
input: 1
input: 1
output: 1.41421

Тест 2
input: 0
input: 0
input: 1
input: 0
output: 1

Тест 3
input: 3
input: -2
input: -1
input: 7
output: 9.84886
"""


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


a1 = float(input())
a2 = float(input())
b1 = float(input())
b2 = float(input())

print(distance(a1, a2, b1, b2))
