"""
В списке все элементы попарно различны. Поменяйте местами минимальный и
максимальный элемент этого списка.


Формат ввода:
Вводится список целых чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 3 4 5 2 1
3 4 1 2 5

Тест 2
>>> 1 5 4 3 2
5 1 4 3 2

Тест 3
>>> -30000 30000
30000 -30000
"""


def main():
    lst = list(map(int, input().split()))

    minimum = None
    maximum = None
    for i, elem in enumerate(lst):
        if minimum is None or minimum > elem:
            minimum = elem
            min_index = i
        if maximum is None or maximum < elem:
            maximum = elem
            max_index = i
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
    print(*lst)


main()
