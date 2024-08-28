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
print(
    len(
        set(
            open("input.txt", "r", encoding="utf8")
            .read()
            .strip()
            .split()
        )
    )
)
