"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите,
какое наибольшее число подряд идущих элементов этой последовательности равны
друг другу.


Формат ввода:
Вводится последовательность натуральных чисел, оканчивающаяся числом 0 (само
число 0 в последовательность не входит, а служит как признак ее окончания).


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 1
>>> 7
>>> 7
>>> 9
>>> 1
>>> 0
2

Тест 2
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> 6
>>> 7
>>> 8
>>> 9
>>> 10
>>> 11
>>> 0
1

Тест 3
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 4
>>> 0
15
"""

eof = False
max_count = 0
current_count = 0
current_number = None
while not eof:
    n = int(input())
    if n == 0:
        eof = True
        break

    if current_number is None:
        current_number = n

    if n == current_number:
        current_count += 1
        if max_count < current_count:
            max_count = current_count
    else:
        current_number = n
        current_count = 1
print(max_count)