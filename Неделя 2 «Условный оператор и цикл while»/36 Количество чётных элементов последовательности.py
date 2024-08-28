"""
Количество чётных элементов последовательности

Определите количество четных элементов в последовательности, завершающейся
числом 0.


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0
в последовательность не входит, а служит как признак ее окончания).


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 2
input: 1
input: 4
input: 0
output: 2

Тест 2
input: 1
input: 3
input: 5
input: 7
input: 9
input: 1
input: 3
input: 5
input: 7
input: 9
input: 0
output: 0

Тест 3
input: 2
input: 4
input: 0
output: 2
"""
eof = False
even_amount = 0
while not eof:
    n = int(input())
    if n == 0:
        eof = True
        continue
    elif n % 2 == 0:
        even_amount += 1
print(even_amount)
