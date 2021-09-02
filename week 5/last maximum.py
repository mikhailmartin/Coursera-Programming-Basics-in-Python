"""
Найдите наибольшее значение в списке и индекс последнего элемента, который
имеет данное значение за один проход по списку, не модифицируя этот список и не
используя дополнительного списка.

Выведите два значения.


Примеры:
Тест 1
>>> 1 2 1 2 1
2 3

Тест 2
>>> 1 2 3 4 5
5 4

Тест 3
>>> 5 4 3 2 1
5 0
"""


def main():
    lst = map(int, input().split())
    max_elem = None
    index_max_elem = None
    for i, elem in enumerate(lst):
        if max_elem is None or max_elem <= elem:
            max_elem = elem
            index_max_elem = i
    print(max_elem, index_max_elem)


main()
