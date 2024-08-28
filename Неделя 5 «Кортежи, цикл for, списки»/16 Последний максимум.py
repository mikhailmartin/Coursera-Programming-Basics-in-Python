"""
Последний максимум

Найдите наибольшее значение в списке и индекс последнего элемента, который
имеет данное значение за один проход по списку, не модифицируя этот список и не
используя дополнительного списка.

Выведите два значения.


Примеры:
Тест 1
input: 1 2 1 2 1
output: 2 3

Тест 2
input: 1 2 3 4 5
output: 5 4

Тест 3
input: 5 4 3 2 1
output: 5 0
"""
lst = map(int, input().split())

max_elem = None
index_max_elem = None
for i, elem in enumerate(lst):
    if max_elem is None or max_elem <= elem:
        max_elem = elem
        index_max_elem = i
print(max_elem, index_max_elem)
