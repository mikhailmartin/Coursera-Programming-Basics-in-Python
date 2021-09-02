"""
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
>>> 0
>>> 0
0

Тест 2
>>> 0
>>> 1
1

Тест 3
>>> 1
>>> 0
1
"""


def xor(x, y):
    return (x + y) % 2


def main():
    x = float(input())
    y = float(input())
    if xor(x, y):
        print('1')
    else:
        print('0')


main()
