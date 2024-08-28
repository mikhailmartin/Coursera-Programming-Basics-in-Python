"""
Количество элементов, больше предыдущего

Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего
элемента.


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
output: 2

Тест 2
input: 1
input: 5
input: 2
input: 4
input: 3
input: 0
output: 2

Тест 3
input: 1
input: 2
input: 3
input: 4
input: 5
input: 0
output: 4
"""
eof = False
previous = int(input())
count = 0
while not eof:
    current = int(input())
    if current == 0:
        eof = True
        continue
    if current > previous:
        count += 1
    previous = current
print(count)
