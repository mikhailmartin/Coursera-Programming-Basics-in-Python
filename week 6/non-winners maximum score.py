"""
Зачёт проводится отдельно в каждом классе. Победителями олимпиады становятся
школьники, которые набрали наибольший балл среди всех участников в данном
классе.

Для каждого класса определите максимальный балл, который набрал школьник, не
ставший победителем в данном классе.


Формат вывода:
Выведите три целых числа.


Примеры:
Тест 1
>>> Иванов Сергей 9 80
>>> Сергеев Петр 10 82
>>> Петров Василий 11 82
>>> Васильев Андрей 9 81
>>> Андреев Александр 10 81
>>> Александров Роман 9 81
>>> Романов Иван 11 83
80 81 82

Тест 2
>>> Иванов Сергей 9 0
>>> Сергеев Петр 10 1
>>> Васильев Андрей 9 1
>>> Андреев Александр 10 0
>>> Александров Роман 11 2
>>> Петров Василий 11 1
0 0 1

Тест 3
>>> Иванов Сергей 9 10
>>> Сергеев Петр 10 20
>>> Петров Василий 11 40
>>> Васильев Андрей 9 11
>>> Андреев Александр 10 15
>>> Александров Роман 9 8
>>> Романов Иван 11 30
>>> Алексеев Сергей 9 11
>>> Егоров Николай 9 12
>>> Николаев Степан 11 30
>>> Степанов Гаврила 10 20
>>> Гаврилов Виктор 11 30
>>> Викторов Павел 11 35
11 15 35
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

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


main()
