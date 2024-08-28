"""
Количество элементов, равных максимуму

Последовательность состоит из натуральных чисел и завершается числом 0.
Определите количество элементов этой последовательности, которые равны её
наибольшему элементу.


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
output: 1

Тест 2
input: 1
input: 3
input: 3
input: 1
output: 2

Тест 3
input: 1
input: 2
input: 3
input: 4
input: 5
input: 0
output: 1
"""
eof = False
maximum = None
while not eof:
    n = int(input())
    if n == 0:
        eof = True
        continue
    if maximum is None or n > maximum:
        maximum = n
        count = 1
    elif n == maximum:
        count += 1
print(count)
