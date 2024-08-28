"""
Количество нулей

Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это
количество.


Формат ввода:
Cначала вводится число N, затем вводится ровно N целых чисел.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 5
input: 0
input: 7
input: 0
input: 2
input: 2
output: 2

Тест 2
input: 7
input: 1
input: 2
input: 3
input: 4
input: 5
input: 6
input: 7
output: 0

Тест 3
input: 6
input: 0
input: 0
input: 0
input: 0
input: 0
input: 0
output: 6
"""
n = int(input())

number = 0
for i in range(n):
    if int(input()) == 0:
        number += 1
print(number)
