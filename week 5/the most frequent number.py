"""
Дан список. Не изменяя его и не используя дополнительные списки, определите,
какое число в этом списке встречается чаще всего. Если таких чисел несколько,
выведите любое из них.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 1 2 3 2 3 3
3

Тест 2
>>> 1 2 3 4 5 6 7 8 9 1
1

Тест 3
>>> 1 1 2 2 3 3 4 4 5 5 5
5
"""


def main():
    lst = list(map(int, input().split()))

    n, s = 0, 0
    for elem in lst:
        if lst.count(elem) > n:
            n = lst.count(elem)
            s = elem
    print(s)


main()