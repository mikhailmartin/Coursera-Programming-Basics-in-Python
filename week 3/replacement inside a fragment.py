"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме
первого и последнего вхождения.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> In the hole in the ground there lived a hobbit
In the Hole in tHe ground tHere lived a hobbit

Тест 2
>>> qwertyhahsdhfghzxcvb
qwertyhaHsdHfghzxcvb

Тест 3
>>> asdfghhzxcvb
asdfghhzxcvb
"""

s = input()
s = s.replace('h', 'H')
s = s.replace('H', 'h', 1)
s = s[::-1]
s = s.replace('H', 'h', 1)
s = s[::-1]
print(s)
