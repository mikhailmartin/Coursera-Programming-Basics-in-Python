"""
Вводится число 0 или 1, необходимо вывести 1 или 0 соответственно.


Формат ввода:
Число 0 или 1.


Формат вывода:
Число 0 или 1.


Примеры:
Тест 1
>>> 1
0
"""

digit = int(input())
inverted_digit = (digit + 1) % 2
print(inverted_digit)
