"""
Ряд-2

Даны два целых числа A и В. Выведите все числа от A до B включительно, в
порядке возрастания, если A < B, или в порядке убывания в противном случае.


Формат ввода:
Вводятся два целых числа.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 10
output: 1 2 3 4 5 6 7 8 9 10

Тест 2
input: 10
input: 1
output: 10 9 8 7 6 5 4 3 2 1

Тест 3
input: 179
input: 179
output: 179
"""
a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")
elif a > b:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
elif a == b:
    print(a)
