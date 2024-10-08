"""
Исключающее ИЛИ

Напишите функцию xor(x, y), реализующую функцию "Исключающее ИЛИ" двух
логических переменных x и y.

Функция xor должна возвращать True, если ровно один из её аргументов x или y,
но не оба одновременно равны True.


Формат ввода:
Вводится 2 числа - x и y (x и y равны 0 или 1, 0 соответствует значению False,
1 соответствует значению True).


Формат вывода:
Необходимо вывести 0 или 1 - значение функции от x и y.


Примеры:
Тест 1
input: 0
input: 0
output: 0

Тест 2
input: 0
input: 1
output: 1

Тест 3
input: 1
input: 0
output: 1
"""


def xor(x, y):
    return (x + y) % 2


x = float(input())
y = float(input())

print("1" if xor(x, y) else "0")
