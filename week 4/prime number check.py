"""
Дано натуральное число n > 1. Проверьте, является ли оно простым. Программа
должна вывести слово YES, если число простое и NO, если число составное.
Решение оформите в виде функции IsPrime(n), которая возвращает True для простых
чисел и False для составных чисел. Программа должна иметь сложность
O(корень из n): количество действий в программе должно быть пропорционально
квадратному корню из n (иначе говоря, при увеличении входного числа в k раз,
время выполнения программы должно увеличиваться примерно в корень из k раз).


Формат ввода:
Вводится натуральное число.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> 2
YES

Тест 2
>>> 4
NO

Тест 3
>>> 3
YES
"""


def is_prime(x):
    def min_divisor(a):
        i = 2
        while i <= a ** 0.5:
            if a % i == 0:
                return i
            i += 1
        else:
            return a

    return True if min_divisor(x) == x else False


def main():
    n = int(input())
    print('YES' if is_prime(n) else 'NO')


main()