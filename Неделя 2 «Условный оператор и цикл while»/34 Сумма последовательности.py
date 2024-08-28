"""
Сумма последовательности

Определите сумму всех элементов последовательности, завершающейся числом 0.


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0
в последовательность не входит, а служит как признак ее окончания).


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
amount = 0
eof = False
while not eof:
    n = int(input())
    if n == 0:
        eof = True
    amount += n
print(amount)
