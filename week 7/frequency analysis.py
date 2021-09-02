"""
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
>>> hi
>>> hi
>>> what is your name
>>> my name is bond
>>> james bond
>>> my name is damme
>>> van damme
>>> claude van damme
>>> jean claude van damme
damme
is
name
van
bond
claude
hi
my
james
jean
what
your

Тест 2
>>> oh you touch my tralala
>>> mmm my ding ding dong
ding
my
dong
mmm
oh
touch
tralala
you

Тест 3
>>> ai ai ai ai ai ai ai ai ai ai
ai
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    word_count = dict()
    for line in input_file:
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    input_file.close()

    lst = [(word, count) for word, count in word_count.items()]
    for word, count in sorted(lst, key=lambda x: (-x[1], x[0])):
        print(word)


main()
