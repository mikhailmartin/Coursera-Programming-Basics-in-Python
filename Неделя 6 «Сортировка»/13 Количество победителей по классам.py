"""
Количество победителей по классам

В условиях предыдущей задачи определите количество школьников, ставших
победителями в каждом классе. Победителями объявляются все, кто набрал
наибольшее число баллов по данному классу. Гарантируется, что в каждом классе
был хотя бы один участник.


Формат вывода:
Выведите три числа: количество победителей олимпиады по 9 классу,
по 10 классу, по 11 классу.


Примеры:
Тест 1
input: Иванов Сергей 9 80
input: Сергеев Петр 10 80
input: Петров Василий 11 81
input: Васильев Андрей 9 81
input: Андреев Александр 10 80
input: Александров Роман 9 81
input: Романов Иван 11 80
output: 2 2 1

Тест 2
input: Егоров Павел 11 30
input: Кострикова Анна 9 49
input: Туаршев Тенгиз 9 91
input: Кузьмин Александр 11 99
input: Перочинская Виктория 11 53
input: Лебедев Дмитрий 11 29
input: Гольсков Алексей 11 92
input: Васильева Александра 11 41
input: Медведев Дмитрий 10 86
input: Аптараули Алексей 9 51
output: 1 1 1

Тест 3
input: Егоров Павел 9 0
input: Кострикова Анна 9 0
input: Туаршев Тенгиз 9 0
input: Кузьмин Александр 11 0
input: Перочинская Виктория 9 0
input: Лебедев Дмитрий 9 0
input: Гольсков Алексей 9 0
input: Васильева Александра 9 0
input: Медведев Дмитрий 10 0
input: Аптараули Алексей 11 0
output: 7 1 2
"""
INPUT_FILE_NAME = "input.txt"


file = open(INPUT_FILE_NAME, "r", encoding="utf-8")

max9 = None
num9 = 1
max10 = None
num10 = 1
max11 = None
num11 = 1

for line in file:
    name, surname, grade, score = line.split()
    score = int(score)
    if grade == "9":
        if score == max9:
            num9 += 1
        elif max9 is None or score > max9:
            max9 = score
            num9 = 1
    elif grade == "10":
        if score == max10:
            num10 += 1
        elif max10 is None or score > max10:
            max10 = score
            num10 = 1
    elif grade == "11":
        if score == max11:
            num11 += 1
        elif max11 is None or score > max11:
            max11 = score
            num11 = 1

file.close()

print(num9, num10, num11)
