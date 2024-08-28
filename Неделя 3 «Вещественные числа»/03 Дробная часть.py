"""
Дробная часть

Дано положительное действительное число X. Выведите его дробную часть.


Формат ввода:
Вводится положительное действительное число.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 17.9
output: 0.9

Тест 2
input: 10.34
output: 0.34

Тест 3
input: 0.001
output: 0.001
"""
x = float(input())
integer_part = int(x)

fractional_part = x - integer_part
print(fractional_part)
