"""
Наибольший элемент

Дан список чисел. Выведите значение наибольшего элемента в списке, а затем
индекс этого элемента в списке. Если наибольших элементов несколько, выведите
их значение и индекс первого из них.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1 2 3 2 1
output: 3 2

Тест 2
input: 1 2 3
output: 3 2

Тест 3
input: 1 3 2
output: 3 1
"""
lst = list(map(int, input().split()))

max_elem = None
for i, elem in enumerate(lst):
    if max_elem is None or max_elem < elem:
        max_elem = elem
        max_elem_index = i
print(max_elem, max_elem_index)
