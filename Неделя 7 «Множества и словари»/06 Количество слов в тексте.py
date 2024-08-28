"""
Количество слов в тексте

Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку
sys) записан текст. Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом пробелов или символами
конца строки. Определите, сколько различных слов содержится в этом тексте.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: She sells sea shells on the sea shore;
input: The shells that she sells are sea shells I'm sure.
input: So if she sells sea shells on the sea shore,
input: I'm sure that the shells are sea shore shells.
output: 19
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

all_words = set()
for line in input_file:
    words_in_line = set(line.split())
    all_words |= words_in_line
input_file.close()

print(len(all_words))
