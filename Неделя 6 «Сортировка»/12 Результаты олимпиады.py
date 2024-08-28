"""
Результаты олимпиады

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
input: 3
input: Ivanov 15
input: Petrov 10
input: Sidorov 20
output: Sidorov
output: Ivanov
output: Petrov

Тест 2
input: 3
input: Ivanov 15
input: Petrov 20
input: Sidorov 10
output: Petrov
output: Ivanov
output: Sidorov

Тест 3
input: 3
input: Ivanov 10
input: Petrov 15
input: Sidorov 20
output: Sidorov
output: Petrov
output: Ivanov
"""
n = int(input())
structs = []
for _ in range(n):
    structs.append(input().split())

structs.sort(key=lambda x: int(x[1]), reverse=True)

for i in structs:
    print(i[0])
