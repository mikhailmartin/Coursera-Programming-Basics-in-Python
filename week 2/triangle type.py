"""
Даны три стороны треугольника a, b, c. Определите тип треугольника с заданными
сторонами. Выведите одно из четырех слов: rectangular для прямоугольного
треугольника, acute для остроугольного треугольника, obtuse для тупоугольного
треугольника или impossible, если треугольника с такими сторонами не существует
(считаем, что вырожденный треугольник тоже невозможен).


Формат ввода:
Вводятся три целых числа.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 3
>>> 4
>>> 5
rectangular

Тест 2
>>> 3
>>> 5
>>> 4
rectangular
"""

a = int(input())
b = int(input())
c = int(input())
if (a <= 0) or (b <= 0) or (c <= 0) or \
        ((a + b) <= c) or ((a + c) <= b) or ((c + b) <= a):
    print("impossible")
else:
    if ((b ** 2 + c ** 2 - a ** 2) / b * c) == 0:  # cosBC
        print("rectangular")
    elif ((b ** 2 + c ** 2 - a ** 2) / b * c) < 0:
        print("obtuse")
    elif ((a ** 2 + b ** 2 - c ** 2) / a * b) == 0:  # cosAB
        print("rectangular")
    elif ((a ** 2 + b ** 2 - c ** 2) / a * b) < 0:
        print("obtuse")
    elif ((a ** 2 + c ** 2 - b ** 2) / a * c) == 0:  # cosCA
        print("rectangular")
    elif ((a ** 2 + c ** 2 - b ** 2) / a * c) < 0:
        print("obtuse")
    else:
        print("acute")
