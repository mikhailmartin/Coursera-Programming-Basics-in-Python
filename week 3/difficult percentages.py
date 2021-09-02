"""
Процентная ставка по вкладу составляет P процентов годовых, которые
прибавляются к сумме вклада через год. Вклад составляет X рублей Y копеек.
Определите размер вклада через K лет.


Формат ввода:
Программа получает на вход целые числа P, X, Y, K.


Формат вывода:
Программа должна вывести два числа: величину вклада через K лет в рублях и
копейках. Дробное число копеек по истечение года отбрасывается. Перерасчет
суммы вклада (с отбрасыванием дробных частей копеек) происходит ежегодно.


Примеры:
Тест 1
>>> 12
>>> 179
>>> 0
>>> 5
315 43

Тест 2
>>> 13
>>> 179
>>> 0
>>> 100
36360285 50

Тест 3
>>> 1
>>> 1
>>> 0
>>> 1000
11881 92
"""

p = int(input())
x = int(input())
y = int(input())
k = int(input())

i = 0
while i < k:
    deposit = x * 100 + y  # депозит в копейках
    deposit += (deposit / 100) * p
    x = int(deposit // 100)
    y = int(deposit % 100)
    i += 1
print(x, y)