"""
Удаление фрагмента

Дана строка, в которой буква h встречается минимум два раза. Удалите из этой
строки первое и последнее вхождение буквы h, а также все символы, находящиеся
между ними.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: In the hole in the ground there lived a hobbit
output: In tobbit

Тест 2
input: qwertyhasdfghzxcvb
output: qwertyzxcvb

Тест 3
input: asdfghhzxcvb
output: asdfgzxcvb
"""
s = input()

left_index = s.find('h')
right_index = len(s) - s[::-1].find('h') - 1
s = s[:left_index] + s[right_index + 1:]
print(s)
