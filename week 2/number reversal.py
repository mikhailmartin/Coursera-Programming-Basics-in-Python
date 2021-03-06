"""
Переставьте цифры числа в обратном порядке.


Формат ввода:
Задано единственное число N.


Формат вывода:
Необходимо вывести цифры данного числа в обратном порядке.


Примеры:
Тест 1
>>> 1
1

Тест 2
>>> 12
21

Тест 3
>>> 874
478
"""

n = int(input())
while n != 0:
    print(n % 10, end="")
    n //= 10
