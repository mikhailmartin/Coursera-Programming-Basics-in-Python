"""
Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 1 2 2 3 3 3
1

Тест 2
>>> 4 3 5 2 5 1 3 5
4 2 1
"""


def main():
    lst = list(map(int, input().split()))

    uniqs = []
    for elem in lst:
        if lst.count(elem) == 1:
            uniqs.append(elem)
    print(*uniqs)


main()
