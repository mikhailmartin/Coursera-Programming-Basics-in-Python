"""
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
>>> 1
>>> 7
>>> 9
>>> 0
7

Тест 2
>>> 2
>>> 1
>>> 0
1

Тест 31 (дополнительный пример)
>>> 1
>>> 2
>>> 2
>>> 3
>>> 3
>>> 0
3
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
