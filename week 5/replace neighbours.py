"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.). Если
элементов нечётное число, то последний элемент остаётся на своём месте.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 1 2 3 4 5
2 1 4 3 5

Тест 2
>>> 4 5 3 4 2 3
5 4 4 3 3 2

Тест 3
>>> 9 4 5 2 3
4 9 2 5 3
"""


def main():
    lst = list(map(int, input().split()))

    length = len(lst) if len(lst) % 2 == 0 else len(lst) - 1
    for i in range(0, length, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    print(*lst)


main()
