"""
Напишите программу, которая считывает целое число и выводит текст, аналогичный
приведённому в примере (важно в точности соблюдать вывод программы: обратите
внимание на пробелы и на точки). Нельзя пользоваться конкатенацией строк,
используйте print с несколькими параметрами.


Формат ввода:
Вводится целое число (гарантируется, что число находится в диапазоне от -1000
до +1000).


Формат вывода:
Выведите две строки, согласно образцу.


Примеры:
Тест 1
>>> 179
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
"""

number = int(input())
next = number + 1
previous = number - 1
print(
    "The next number for the number ",
    number,
    " is ",
    next, ".",
    sep=""
)
print(
    "The previous number for the number ",
    number,
    " is ",
    previous,
    ".",
    sep=""
)
