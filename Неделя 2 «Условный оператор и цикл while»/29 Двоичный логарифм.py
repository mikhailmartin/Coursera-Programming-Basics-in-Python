"""
Двоичный логарифм

По данному натуральному числу N выведите такое наименьшее целое число k,
что 2ᵏ≥N.

Операцией возведения в степень пользоваться нельзя!


Формат ввода:
Вводится натуральное число.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
output: 0

Тест 2
input: 2
output: 1

Тест 3
input: 3
output: 2
"""
n = int(input())

k = 0
power = 1
while power < n:
    k += 1
    power *= 2
print(k)
