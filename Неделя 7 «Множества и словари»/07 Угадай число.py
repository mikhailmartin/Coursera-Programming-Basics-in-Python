"""
Угадай число

Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
Беатриса пытается угадать это число, для этого она называет некоторые множества
натуральных чисел. Август отвечает Беатрисе YES, если среди названных ею чисел
есть задуманное или NO в противном случае. После нескольких заданных вопросов
Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и
просит вас помочь ей определить, какие числа мог задумать Август.


Формат ввода:
Первая строка входных данных содержит число n — наибольшее число, которое мог
загадать Август. Далее идут строки, содержащие вопросы Беатрисы. Каждая строка
представляет собой набор чисел, разделённых пробелами. После каждой строки с
вопросом идёт ответ Августа: YES или NO. Наконец, последняя строка входных
данных содержит одно слово HELP.


Формат вывода:
Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог
задумать Август.


Примеры:
Тест 1
input: 10
input: 1 2 3 4 5
input: YES
input: 2 4 6 8 10
input: NO
input: HELP
output: 1 3 5

Тест 2
input: 10
input: 1 2 3 4 5 6 7 8 9 10
input: YES
input: 1
input: NO
input: 2
input: NO
input: 3
input: NO
input: 4
input: NO
input: 6
input: NO
input: 7
input: NO
input: 8
input: NO
input: 9
input: NO
input: 10
input: NO
input: HELP
output: 5
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

n = int(input_file.readline())
st = set(range(1, n + 1))

for line in input_file:
    if line.strip() == "HELP":
        break

    if line.strip() == "YES":
        st &= question
    elif line.strip() == "NO":
        st -= question
    else:
        question = set(map(int, line.split()))
input_file.close()

print(*sorted(st))
