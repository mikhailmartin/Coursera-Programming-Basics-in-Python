"""
Второй максимум

Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности, то
есть элемента, который будет наибольшим, если из последовательности удалить
одно вхождение наибольшего элемента.


Формат ввода:
Вводится последовательность натуральных чисел, оканчивающаяся числом 0 (само
число 0 в последовательность не входит, а служит как признак ее окончания).


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 7
input: 9
input: 0
output: 7

Тест 2
input: 2
input: 1
input: 0
output: 1

Тест 31 (дополнительный пример)
input: 1
input: 2
input: 2
input: 3
input: 3
input: 0
output: 3
"""
first_maximum = int(input())
second_maximum = int(input())

if second_maximum > first_maximum:
    first_maximum, second_maximum = second_maximum, first_maximum

eof = False
while not eof:
    n = int(input())
    if n == 0:
        eof = True
        continue
    if n > first_maximum:
        first_maximum, second_maximum = n, first_maximum
    elif n > second_maximum:
        second_maximum = n
print(second_maximum)
