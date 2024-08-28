"""
Ближайшее число

Напишите программу, которая находит в массиве элемент, самый близкий по
величине к данному числу.


Формат ввода:
В первой строке задаётся одно натуральное число N, не превосходящее 1000 –
размер массива. Во второй строке содержатся N чисел – элементы массива (целые
числа, не превосходящие по модулю 1000). В третьей строке вводится одно целое
число x, не превосходящее по модулю 1000.


Формат вывода:
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько,
выведите любое из них.


Примеры:
Тест 1
input: 5
input: 1 2 3 4 5
input: 6
output: 5

Тест 2
input: 5
input: 5 4 3 2 1
input: 3
output: 3
"""
n = int(input())
lst = list(map(int, input().split()))
x = int(input())

nearest_number = None
for elem in lst:
    current_dist = abs(elem - x)
    if nearest_number is None or current_dist < nearest_dist:
        nearest_dist = current_dist
        nearest_number = elem
print(nearest_number)
