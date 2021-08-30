"""
Даны три целых числа. Найдите наибольшее из них (программа должна вывести
ровно одно целое число).

Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для
решения этой задачи?


Формат ввода:
Вводится три целых числа.


Формат вывода:
Выведите ответ на задачу.


Примеры:
>>> 1
>>> 2
>>> 3
3
"""

first_number = int(input())
second_number = int(input())
third_number = int(input())
if first_number >= second_number:
    if first_number >= third_number:
        print(first_number)
    else:
        print(third_number)
else:
    if second_number >= third_number:
        print(second_number)
    else:
        print(third_number)
