"""
Наименьший нечётный

Выведите значение наименьшего нечётного элемента списка, гарантируется, что
хотя бы один нечётный элемент в списке есть.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 0 1 2 3 4
output: 1

Тест 2
input: 2 4 6 8 10 19
output: 19

Тест 3
input: 5 4 3 2 1 0 -1 -2 -3 -4
output: -3
"""
lst = list(map(int, input().split()))
min_odd_elem = None
for elem in lst:
    if elem % 2 != 0:
        if min_odd_elem is None or min_odd_elem > elem:
            min_odd_elem = elem
print(min_odd_elem)
