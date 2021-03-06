"""
Дан список чисел. Если в нём есть два соседних элемента одного знака, выведите
эти числа. Если соседних элементов одного знака нет - не выводите ничего. Если
таких пар соседей несколько - выведите первую пару.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> -1 2 3 -1 -2
2 3

Тест 2
>>> 1 -3 4 -2 1


Тест 3
>>> 1 2 -3 -4 -5
1 2
"""


def main():
    lst = list(map(int, input().split()))
    for i in range(1, len(lst)):
        if lst[i - 1] * lst[i] > 0:
            print(lst[i - 1], lst[i])
            break


main()
