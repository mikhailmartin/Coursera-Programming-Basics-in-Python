"""
Минимум 4 чисел

Напишите функцию min4(a, b, c, d), вычисляющую минимум четырёх чисел, которая
не содержит инструкции if, а использует стандартную функцию min от двух чисел.
Считайте четыре целых числа и выведите их минимум.


Формат ввода:
Вводятся четыре целых числа.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 4
input: 5
input: 6
input: 7
output: 4

Тест 2
input: 5
input: 4
input: 6
input: 7
output: 4

Тест 3
input: 5
input: 7
input: 4
input: 6
output: 4
"""


def min4(arg1, arg2, arg3, arg4):

    min1 = min(arg1, arg2)
    min2 = min(arg3, arg4)

    return min(min1, min2)


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))
