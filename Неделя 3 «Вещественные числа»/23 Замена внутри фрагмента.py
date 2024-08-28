"""
Замена внутри фрагмента

Дана строка. Замените в этой строке все появления буквы h на букву H, кроме
первого и последнего вхождения.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: In the hole in the ground there lived a hobbit
output: In the Hole in tHe ground tHere lived a hobbit

Тест 2
input: qwertyhahsdhfghzxcvb
output: qwertyhaHsdHfghzxcvb

Тест 3
input: asdfghhzxcvb
output: asdfghhzxcvb
"""
s = input()

s = s.replace('h', 'H')
s = s.replace('H', 'h', 1)
s = s[::-1]
s = s.replace('H', 'h', 1)
s = s[::-1]
print(s)
