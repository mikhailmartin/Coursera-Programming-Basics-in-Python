"""
Назовем число палиндромом, если оно не меняется при перестановке его цифр в
обратном порядке. Напишите программу, которая по заданному числу K выводит
количество натуральных палиндромов, не превосходящих K.


Формат ввода:
Задано единственное число K (1 ≤ K ≤ 100000).


Формат вывода:
Необходимо вывести количество натуральных палиндромов, не превосходящих K.


Примеры:
Тест 1
>>> 1
1

Тест 2
>>> 100
18

Тест 3
>>> 10
9
"""

k = int(input())
i = 1
amount = 0
while i <= k:
    rev = 0
    tmp = i
    while tmp != 0:
        rev = rev * 10 + tmp % 10
        tmp //= 10
    if i == rev:
        amount += 1
    i += 1
print(amount)
