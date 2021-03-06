"""
В олимпиаде участвовало N человек. Каждый получил определённое количество
баллов, при этом оказалось, что у всех участников разное число баллов.
Упорядочите список участников олимпиады в порядке убывания набранных баллов.


Формат ввода:
Программа получает на вход число участников олимпиады N. Далее идёт N строк, в
каждой строке записана фамилия участника, затем, через пробел, набранное им
количество баллов.


Формат вывода:
Выведите список участников (только фамилии) в порядке убывания набранных
баллов.


Примеры:
Тест 1
>>> 3
>>> Ivanov 15
>>> Petrov 10
>>> Sidorov 20
Sidorov
Ivanov
Petrov

Тест 2
>>> 3
>>> Ivanov 15
>>> Petrov 20
>>> Sidorov 10
Petrov
Ivanov
Sidorov

Тест 3
>>> 3
>>> Ivanov 10
>>> Petrov 15
>>> Sidorov 20
Sidorov
Petrov
Ivanov
"""


def main():
    n = int(input())
    structs = []
    for _ in range(n):
        structs.append(input().split())

    structs.sort(key=lambda x: int(x[1]), reverse=True)

    for i in structs:
        print(i[0])


main()
