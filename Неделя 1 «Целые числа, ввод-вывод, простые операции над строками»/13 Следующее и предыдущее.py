"""
Следующее и предыдущее

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
input: 179
output: The next number for the number 179 is 180.
output: The previous number for the number 179 is 178.
"""
number = int(input())

next = number + 1
previous = number - 1
print(
    f"The next number for the number {number} is {next}.\n"
    f"The previous number for the number {number} is {previous}."
)
