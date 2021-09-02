"""
Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и
копеек нужно заплатить за N пирожков.


Формат ввода:
Программа получает на вход три числа: A, B, N —  целые, неотрицательные, не
превышают 10000.


Формат вывода:
Программа должна вывести два числа: стоимость покупки в рублях и копейках.


Примеры:
Тест 1
>>> 10
>>> 15
>>> 2
20 30

Тест 2
>>> 2
>>> 50
>>> 4
10 0
"""

A = int(input())
B = int(input())
N = int(input())

rubles = (A * N) + ((B * N) // 100)
kopecks = (B * N) % 100
print(rubles, kopecks)