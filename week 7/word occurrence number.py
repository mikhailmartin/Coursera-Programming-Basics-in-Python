"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов. Слова
разделены одним или большим числом пробелов или символами конца строки. Для
каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом
тексте ранее.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> one two one tho three
0 0 1 0 0

Тест 2
>>> She sells sea shells on the sea shore;
>>> The shells that she sells are sea shells I'm sure.
>>> So if she sells sea shells on the sea shore,
>>> I'm sure that the shells are sea shore shells.
0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0

Тест 3
>>> aba aba; aba @?"
0 0 1 0
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    word_count = dict()
    for line in input_file:
        for word in line.split():
            print(word_count.get(word, 0), end=' ')
            word_count[word] = word_count.get(word, 0) + 1


main()
