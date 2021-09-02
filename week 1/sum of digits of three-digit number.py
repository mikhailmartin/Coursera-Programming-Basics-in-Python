"""
Дано трёхзначное число. Найдите сумму его цифр.


Формат ввода:
Вводится целое положительное число. Гарантируется, что оно соответствует
условию задачи.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 179
17
"""

number = int(input())
first_left_digit = number % 10
second_left_digit = (number // 10) % 10
third_left_digit = number // 100
sum = first_left_digit + second_left_digit + third_left_digit
print(sum)
