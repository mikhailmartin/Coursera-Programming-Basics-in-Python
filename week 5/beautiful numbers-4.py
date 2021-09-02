"""
Даны два четырёхзначных числа A и B. Выведите все четырёхзначные числа на
отрезке от A до B, запись которых является палиндромом.


Формат ввода:
Вводятся два целых числа A и B


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 1600
>>> 2100
1661
1771
1881
1991
2002

Тест 2
>>> 4503
>>> 5901
4554
4664
4774
4884
4994
5005
5115
5225
5335
5445
5555
5665
5775
5885

Тест 3
>>> 7337
>>> 7447
7337
7447
"""


def reverse_number(n):
    s = str(n)
    reversed_s = s[::-1]
    return int(reversed_s)


def main():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1):
        if i == reverse_number(i):
            print(i)


main()