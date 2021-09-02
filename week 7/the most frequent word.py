"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если
таких слов несколько, выведите то, которое меньше в лексикографическом порядке.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> apple orange banana banana orange
banana

Тест 2
>>> oh you touch my tralala mmm my ding ding dong
ding

Тест 3
>>> q w e r t y u i o p
>>> a s d f g h j k l
>>> z x c v b n m
a
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

    max_count = None
    for word, count in sorted(word_count.items()):
        if max_count is None or max_count < count:
            max_count = count
            most_frequent_word = word

    print(most_frequent_word)


main()
