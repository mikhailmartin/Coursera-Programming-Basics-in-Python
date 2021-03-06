"""
Определите среднее значение всех элементов последовательности, завершающейся
числом 0. Использовать массивы в данной задаче нельзя.


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0
в последовательность не входит, а служит как признак ее окончания).


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 1
>>> 7
>>> 9
>>> 0
5.66666666667

Тест 2
>>> 1
>>> 1
>>> 1
>>> 1
>>> 1
>>> 1
>>> 1
>>> 1
>>> 1
>>> 0
1.0

Тест 3
>>> 34
>>> 2345
>>> 2345
>>> 2345
>>> 2345
>>> 345
>>> 3
>>> 345
>>> 3
>>> 345
>>> 1
>>> 3
>>> 424
>>> 5
>>> 453
>>> 0
756.066666667
"""

eof = False
count = 0
amount = 0
while not eof:
    n = int(input())
    if n == 0:
        eof = True
        continue
    count += 1
    amount += n
mean = amount / count
print(mean)
