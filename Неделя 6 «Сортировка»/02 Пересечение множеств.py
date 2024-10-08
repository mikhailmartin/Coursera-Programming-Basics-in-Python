"""
Пересечение множеств

Даны два списка, упорядоченных по возрастанию (каждый список состоит из
различных элементов).

Найдите пересечение множеств элементов этих списков, то есть те числа, которые
являются элементами обоих списков. Алгоритм должен иметь сложность
O(len(A) + len(B)).

Решение оформите в виде функции Intersection(A, B). Функция должна возвращать
список пересечения данных списков в порядке возрастания элементов.
Модифицировать исходные списки запрещается.


Формат ввода:
Программа получает на вход два возрастающих списка, каждый в отдельной строке.


Формат вывода:
Программа должна вывести последовательность возрастающих чисел, являющихся
элементами обоих списков.


Примеры:
Тест 1
input: 1 3 4 7 9
input: 2 3 7 10 11
output: 3 7

Тест 2
input: 1 4 6 8
input: 1 4 6 8
output: 1 4 6 8

Тест 3
input: 2 4 6 8 10
input: 1 3 5 7 9
output:
"""


def intersection(a, b):

    c = []
    i = j = 0
    len_a = len(a)
    len_b = len(b)
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            c.append(a[i])
            i += 1
            j += 1

    return c


lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

print(*intersection(lst_a, lst_b))
