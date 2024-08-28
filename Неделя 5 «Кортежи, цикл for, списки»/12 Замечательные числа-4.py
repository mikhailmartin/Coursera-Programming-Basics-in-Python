"""
Замечательные числа-4

Даны два четырёхзначных числа A и B. Выведите все четырёхзначные числа на
отрезке от A до B, запись которых является палиндромом.


Формат ввода:
Вводятся два целых числа A и B


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1600
input: 2100
output: 1661
output: 1771
output: 1881
output: 1991
output: 2002

Тест 2
input: 4503
input: 5901
output: 4554
output: 4664
output: 4774
output: 4884
output: 4994
output: 5005
output: 5115
output: 5225
output: 5335
output: 5445
output: 5555
output: 5665
output: 5775
output: 5885

Тест 3
input: 7337
input: 7447
output: 7337
output: 7447
"""


def reverse_number(n):

    s = str(n)
    reversed_s = s[::-1]

    return int(reversed_s)


a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i == reverse_number(i):
        print(i)
