"""
Количество слов

Дана строка, состоящая из слов, разделённых пробелами. Определите, сколько в
ней слов.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: Hello world
output: 2

Тест 2
input: Hello
output: 1

Тест 3
input: q w e
output: 3
"""
s = input()

number_of_whitespaces = s.count(' ') + 1
print(number_of_whitespaces)
