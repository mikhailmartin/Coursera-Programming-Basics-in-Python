"""
Дана строка. Получите новую строку, вставив между каждыми двумя символами
исходной строки символ *. Выведите полученную строку.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> Python
P*y*t*h*o*n

Тест 2
>>> Hello
H*e*l*l*o

Тест 3
>>> A
A
"""

s = input()
s = s.replace('', '*')
print(s[1:-1])
