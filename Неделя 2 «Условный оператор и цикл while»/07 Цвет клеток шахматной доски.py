"""
Цвет клеток шахматной доски

Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите
слово YES, а если в разные цвета – то NO.


Формат вводы:
Вводятся 4 числа - координаты клеток.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 1
input: 2
input: 2
output: YES

input: 1
input: 1
input: 2
input: 3
output: NO
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if ((abs(x1 - x2) % 2 == 0) and (abs(y1 - y2) % 2 == 0)) or \
        (not (abs(x1 - x2) % 2 == 0) and not (abs(y1 - y2) % 2 == 0)):
    print("YES")
else:
    print("NO")
