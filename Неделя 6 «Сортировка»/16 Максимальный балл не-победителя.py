"""
Максимальный балл не-победителя

Зачёт проводится отдельно в каждом классе. Победителями олимпиады становятся
школьники, которые набрали наибольший балл среди всех участников в данном
классе.

Для каждого класса определите максимальный балл, который набрал школьник, не
ставший победителем в данном классе.


Формат вывода:
Выведите три целых числа.


Примеры:
Тест 1
input: Иванов Сергей 9 80
input: Сергеев Петр 10 82
input: Петров Василий 11 82
input: Васильев Андрей 9 81
input: Андреев Александр 10 81
input: Александров Роман 9 81
input: Романов Иван 11 83
output: 80 81 82

Тест 2
input: Иванов Сергей 9 0
input: Сергеев Петр 10 1
input: Васильев Андрей 9 1
input: Андреев Александр 10 0
input: Александров Роман 11 2
input: Петров Василий 11 1
output: 0 0 1

Тест 3
input: Иванов Сергей 9 10
input: Сергеев Петр 10 20
input: Петров Василий 11 40
input: Васильев Андрей 9 11
input: Андреев Александр 10 15
input: Александров Роман 9 8
input: Романов Иван 11 30
input: Алексеев Сергей 9 11
input: Егоров Николай 9 12
input: Николаев Степан 11 30
input: Степанов Гаврила 10 20
input: Гаврилов Виктор 11 30
input: Викторов Павел 11 35
output: 11 15 35
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

winner9 = None
second9 = None
winner10 = None
second10 = None
winner11 = None
second11 = None

for line in input_file:
    grade = int(line.split()[-2])
    score = int(line.split()[-1])
    if grade == 9:
        if winner9 is None:
            winner9 = score
        elif score == winner9:
            continue
        elif score > winner9:
            second9 = winner9
            winner9 = score
        elif second9 is None or score > second9:
            second9 = score
    elif grade == 10:
        if winner10 is None:
            winner10 = score
        elif score == winner10:
            continue
        elif score > winner10:
            second10 = winner10
            winner10 = score
        elif second10 is None or score > second10:
            second10 = score
    elif grade == 11:
        if winner11 is None:
            winner11 = score
        elif score == winner11:
            continue
        elif score > winner11:
            second11 = winner11
            winner11 = score
        elif second11 is None or score > second11:
            second11 = score
input_file.close()

print(second9, second10, second11)
