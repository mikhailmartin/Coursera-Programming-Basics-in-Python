"""
Проверьте, есть ли среди данных N чисел нули.


Формат ввода:
Вводится число N, а затем N чисел.


Формат вывода:
Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в
противном случае.


Примеры:
Тест 1
>>> 3
>>> 4
>>> 19
>>> 14
False

Тест 2
>>> 7
>>> 8
>>> 8
>>> 8
>>> 12
>>> 12
>>> 11
>>> 28
False

Тест 3
>>> 7
>>> 0
>>> 20
>>> 9
>>> 14
>>> 5
>>> 29
>>> 4
True
"""

print(
    any(
        map(
            lambda x: int(x) == 0,
            open('input.txt', 'r', encoding='utf8').read().split()
        )
    )
)
