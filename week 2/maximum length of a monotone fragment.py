"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите
наибольшую длину монотонного фрагмента последовательности (то есть такого
фрагмента, где все элементы либо больше предыдущего, либо меньше).


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0
в последовательность не входит, а служит как признак ее окончания).


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
11

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
1
"""

current = int(input())
seq_pos = seq_neg = seq_max = 1
while current != 0:
    previous = current
    current = int(input())
    if current > previous and current != 0:
        seq_pos += 1
        seq_neg = 1
        if seq_pos > seq_max:
            seq_max = seq_pos
    elif current < previous and current != 0:
        seq_neg += 1
        seq_pos = 1
        if seq_neg > seq_max:
            seq_max = seq_neg
    elif current == previous and current != 0:
        seq_pos = seq_neg = 1
print(seq_max)
