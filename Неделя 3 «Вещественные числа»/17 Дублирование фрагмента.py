"""
Дублирование фрагмента

Дана строка, в которой буква h встречается как минимум два раза. Выведите
изменённую строку: повторите последовательность символов, заключённую между
первым и последним появлением буквы h два раза (сами буквы h не входят в
повторяемый фрагмент, т.е. их повторять не надо).


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: In the hole in the ground there lived a hobbit
output: In the hole in the ground there lived a e hole in the ground there lived a
output: hobbit

Тест 2
input: qwertyhasdfghzxcvb
output: qwertyhasdfgasdfghzxcvb

Тест 3
input: asdfghhzxcvb
output: asdfghhzxcvb
"""
s = input()

left_index = s.find('h')
right_index = len(s) - s[::-1].find('h') - 1
s = s[:right_index] + s[left_index + 1:]
print(s)
