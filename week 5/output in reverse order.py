"""
Выведите элементы данного списка в обратном порядке, не изменяя сам список.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 1 2 3 4 5
5 4 3 2 1

Тест 2
>>> 4 5 3 4 2 3
3 2 4 3 5 4

Тест 3
>>> 9 4 5 2 3
3 2 5 4 9
"""


def main():
    lst = list(map(int, input().split()))
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i], end=' ')


main()