"""
Дано целое число N. Выведите следующее за ним четное число.


Формат ввода:
Вводится целое положительное число, не превышающее 1000.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 7
8

Тест 2
>>> 8
10
"""

number = int(input())
next_even = ((number + 2) // 2) * 2
print(next_even)
