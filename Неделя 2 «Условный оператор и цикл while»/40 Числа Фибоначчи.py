"""
Числа Фибоначчи

Последовательность Фибоначчи определяется так:
F[0] = 0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].

По данному числу n определите n-е число Фибоначчи F[n].


Формат ввода:
Вводится натуральное число n.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 6
output: 8

Тест 2
input: 2
output: 1

Тест 3
input: 3
output: 2
"""
n = int(input())
previous = 0
current = 1
new = 1
i = 0

while i <= n:
    i += 1
    new = current + previous
    current, new = new, current
    previous, current = current, previous
print(current)
