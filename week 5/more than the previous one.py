"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего
элемента.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры
Тест 1
>>> 1 5 2 4 3
5 4

Тест 2
>>> 1 2 3 4 5
2 3 4 5

Тест 3
>>> 5 4 3 2 1
"""


def main():
    lst = map(int, input().split())
    previous = None
    for elem in lst:
        if previous is None:
            previous = elem
            continue
        else:
            current = elem
            if current > previous:
                print(current, end=' ')

            previous = current


main()
