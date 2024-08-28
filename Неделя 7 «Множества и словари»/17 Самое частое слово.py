"""
Самое частое слово

Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если
таких слов несколько, выведите то, которое меньше в лексикографическом порядке.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: apple orange banana banana orange
output: banana

Тест 2
input: oh you touch my tralala mmm my ding ding dong
output: ding

Тест 3
input: q w e r t y u i o p
input: a s d f g h j k l
input: z x c v b n m
output: a
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

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
