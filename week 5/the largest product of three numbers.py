"""
В данном списке из n ≤ 10⁵ целых чисел найдите три числа, произведение которых
максимально.

Решение должно иметь сложность O(n), где n - размер списка. То есть сортировку
использовать нельзя.

Выведите три искомых числа в любом порядке.


Примеры:
Тест 1
>>> 3 5 1 7 9 0 9 -3 10
10 9 9

Тест 2
>>> -5 -30000 -12
-5 -12 -30000

Тест 3
>>> 1 2 3
3 2 1
"""


def main():
    lst = list(map(int, input().split()))

    lst2 = lst.copy()
    if len(lst2) > 3:
        max1 = max(lst2)
        lst2.remove(max(lst2))
        max2 = max(lst2)
        lst2.remove(max(lst2))
        max3 = max(lst2)
        min1 = min(lst2)
        lst2.remove(min(lst2))
        min2 = min(lst2)
        if min1 * min2 * max1 > max1 * max2 * max3:
            print(min1, min2, max1)
        else:
            print(max1, max2, max3)
    else:
        print(*lst)


main()
