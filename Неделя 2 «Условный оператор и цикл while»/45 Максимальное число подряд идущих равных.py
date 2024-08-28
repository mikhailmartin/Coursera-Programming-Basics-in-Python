"""
Максимальное число подряд идущих равных

Дана последовательность натуральных чисел, завершающаяся числом 0. Определите,
какое наибольшее число подряд идущих элементов этой последовательности равны
друг другу.


Формат ввода:
Вводится последовательность натуральных чисел, оканчивающаяся числом 0 (само
число 0 в последовательность не входит, а служит как признак ее окончания).


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1
input: 7
input: 7
input: 9
input: 1
input: 0
output: 2

Тест 2
input: 1
input: 2
input: 3
input: 4
input: 5
input: 6
input: 7
input: 8
input: 9
input: 10
input: 11
input: 0
output: 1

Тест 3
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 4
input: 0
output: 15
"""
eof = False
max_count = 0
current_count = 0
current_number = None
while not eof:
    n = int(input())
    if n == 0:
        eof = True
        break

    if current_number is None:
        current_number = n

    if n == current_number:
        current_count += 1
        if max_count < current_count:
            max_count = current_count
    else:
        current_number = n
        current_count = 1
print(max_count)
