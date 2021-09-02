"""
Даны два целых числа. Программа должна вывести число "1", если первое число
больше второго, число "2", если второе больше первого или число "0", если они
равны.


Формат ввода:
Вводятся два целых числа.


Формат вывода:
Выведите ответ на задачу.


Примечания:
Эту задачу желательно решить с использованием каскадных инструкций
if... elif... else.


Примеры:
Тест 1
>>> 1
>>> 2
2
"""

first_number = int(input())
second_number = int(input())
if first_number > second_number:
    print("1")
elif second_number > first_number:
    print("2")
else:
    print("0")