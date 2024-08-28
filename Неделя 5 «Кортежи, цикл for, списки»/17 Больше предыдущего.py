"""
Больше предыдущего

Дан список чисел. Выведите все элементы списка, которые больше предыдущего
элемента.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры
Тест 1
input: 1 5 2 4 3
output: 5 4

Тест 2
input: 1 2 3 4 5
output: 2 3 4 5

Тест 3
output: input: 5 4 3 2 1
"""
lst = map(int, input().split())

previous = None
for elem in lst:
    if previous is None:
        previous = elem
        continue
    else:
        current = elem
        if current > previous:
            print(current, end=" ")

        previous = current
