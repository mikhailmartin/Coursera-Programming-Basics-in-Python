"""
Сумма последовательности

Дана последовательность чисел, завершающаяся числом 0. Найдите сумму всех этих
чисел, не используя цикл.


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0
в последовательность не входит, а служит как признак её окончания).


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 7
input: 9
input: 0
output: 17

Тест 2
input: 1
input: 1
input: 1
input: 1
input: 1
input: 1
input: 1
input: 1
input: 1
input: 0
output: 9

Тест 3
input: 34
input: 2345
input: 2345
input: 2345
input: 2345
input: 345
input: 3
input: 345
input: 3
input: 345
input: 1
input: 3
input: 424
input: 5
input: 453
input: 0
output: 11341
"""


def sequence_sum():

    x = int(input())

    if x:
        return x + sequence_sum()
    else:
        return 0


print(sequence_sum())
