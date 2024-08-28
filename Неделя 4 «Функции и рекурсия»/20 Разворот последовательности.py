"""
Разворот последовательности

Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту
последовательность в обратном порядке. При решении этой задачи нельзя
пользоваться массивами и прочими динамическими структурами данных. Рекурсия вам
поможет.


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 2
input: 3
input: 0
output: 0
output: 3
output: 2
output: 1

Тест 2
input: 8
input: 7
input: 2
input: 3
input: 1
input: 4
input: 5
input: 0
output: 0
output: 5
output: 4
output: 1
output: 3
output: 2
output: 7
output: 8

Тест 3
input: 1
input: 0
output: 0
output: 1
"""


def sequence_reversal():

    a = int(input())

    if a:
        sequence_reversal()
        print(a)
    else:
        print(a)


sequence_reversal()
