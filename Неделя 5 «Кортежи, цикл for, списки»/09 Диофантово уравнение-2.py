"""
Диофантово уравнение-2

Даны числа a, b, c, d, e. Подсчитайте количество таких целых чисел от 0 до 1000
(включительно), которые являются корнями уравнения
(ax³ + bx² + cx + d) / (x - e) = 0, и выведите их количество.


Формат ввода:
Вводятся целые числа a, b, c, d и e.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: -2
input: 1
input: 0
input: 1
output: 1

Тест 2
input: 1
input: 1
input: 1
input: 1
input: 1
output: 0

Тест 3
input: 2
input: 4
input: 9
input: 1
input: 5
output: 0
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count = 0
for x in range(1001):
    if x != e and ((a * x ** 3 + b * x ** 2 + c * x + d) / (x - e)) == 0:
        count += 1
print(count)
