"""
Периметр треугольника

Напишите функцию, вычисляющую длину отрезка по координатам его концов. С
помощью этой функции напишите программу, вычисляющую периметр треугольника по
координатам трёх его вершин.


Формат ввода:
На вход программе подаётся 6 целых чисел — координат x₁, y₁, x₂, y₂, x₃, y₃
вершин треугольника. Все числа по модулю не превосходят 30 000.


Формат вывода:
Выведите значение периметра этого треугольника с точностью до 6 знаков после
десятичной точки.


Примеры:
Тест 1
input: 0
input: 0
input: 1
input: 0
input: 0
input: 1
output: 3.4142135624

Тест 2
input: -2
input: -4
input: -3
input: -4
input: -1
input: 1
output: 11.4841843207

Тест 3
input: 6
input: 5
input: 2
input: -3
input: -1
input: -6
output: 26.2253174075
"""


def perimeter(x1, y1, x2, y2, x3, y3):

    dist1 = distance(x1, y1, x2, y2)
    dist2 = distance(x1, y1, x3, y3)
    dist3 = distance(x2, y2, x3, y3)

    perim = dist1 + dist2 + dist3

    return perim


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())

print(perimeter(a1, b1, a2, b2, a3, b3))
