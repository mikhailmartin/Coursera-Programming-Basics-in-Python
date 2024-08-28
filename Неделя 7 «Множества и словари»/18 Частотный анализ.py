"""
Частотный анализ

Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
строку. Слова должны быть отсортированы по убыванию их количества появления в
тексте, а при одинаковой частоте появления — в лексикографическом порядке.


Указание:
После того, как вы создадите словарь всех слов, вам захочется отсортировать его
по частоте встречаемости слова. Желаемого можно добиться, если создать список,
элементами которого будут кортежи из двух элементов: частота встречаемости
слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда
стандартная сортировка будет сортировать список кортежей, при этом кортежи
сравниваются по первому элементу, а если они равны — то по второму. Это почти
то, что требуется в задаче.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: hi
input: hi
input: what is your name
input: my name is bond
input: james bond
input: my name is damme
input: van damme
input: claude van damme
input: jean claude van damme
output: damme
output: is
output: name
output: van
output: bond
output: claude
output: hi
output: my
output: james
output: jean
output: what
output: your

Тест 2
input: oh you touch my tralala
input: mmm my ding ding dong
output: ding
output: my
output: dong
output: mmm
output: oh
output: touch
output: tralala
output: you

Тест 3
input: ai ai ai ai ai ai ai ai ai ai
output: ai
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

word_count = dict()
for line in input_file:
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
input_file.close()

lst = [(word, count) for word, count in word_count.items()]
for word, count in sorted(lst, key=lambda x: (-x[1], x[0])):
    print(word)
