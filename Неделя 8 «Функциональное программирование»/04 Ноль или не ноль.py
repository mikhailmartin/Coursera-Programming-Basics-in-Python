"""
Ноль или не ноль

Проверьте, есть ли среди данных N чисел нули.


Формат ввода:
Вводится число N, а затем N чисел.


Формат вывода:
Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в
противном случае.


Примеры:
Тест 1
input: 3
input: 4
input: 19
input: 14
output: False

Тест 2
input: 7
input: 8
input: 8
input: 8
input: 12
input: 12
input: 11
input: 28
output: False

Тест 3
input: 7
input: 0
input: 20
input: 9
input: 14
input: 5
input: 29
input: 4
output: True
"""
print(
    any(
        map(
            lambda x: int(x) == 0,
            open("input.txt", "r", encoding="utf8").read().split()
        )
    )
)
