"""
Упорядочить список партий по числу голосов

Формат входных данных аналогичен предыдущей задаче. Выведите список всех
партий, участвовавших в выборах, отсортировав его в порядке убывания количества
голосов избирателей, а при равном количестве голосов - в лексикографическом
порядке.


Примеры:
Тест 1
input: PARTIES:
input: Party one
input: Party two
input: Party three
input: VOTES:
input: Party one
input: Party two
input: Party three
input: Party two
input: Party three
output: Party three
output: Party two
output: Party one


Тест 2
input: PARTIES:
input: Party one
input: Party two
input: Party three
input: Party four
input: Party five
input: Party six
input: Party seven
input: Party eight
input: Party nine
input: Party ten
input: VOTES:
input: Party three
input: Party five
input: Party seven
input: Party ten
input: Party four
input: Party eight
input: Party one
input: Party two
input: Party six
input: Party nine
output: Party eight
output: Party five
output: Party four
output: Party nine
output: Party one
output: Party seven
output: Party six
output: Party ten
output: Party three
output: Party two


Тест 3
input: PARTIES:
input: Party three
input: Party one
input: Party five
input: Party nine
input: Party six
input: Party seven
input: Party eight
input: Party ten
input: Party four
input: Party two
input: VOTES:
input: Party two
input: Party five
input: Party seven
input: Party four
input: Party ten
input: Party four
input: Party three
input: Party seven
input: Party two
input: Party three
input: Party six
input: Party three
input: Party ten
input: Party six
input: Party nine
input: Party seven
input: Party five
input: Party eight
input: Party five
input: Party seven
input: Party ten
input: Party eight
input: Party five
input: Party nine
input: Party five
input: Party six
input: Party eight
input: Party six
input: Party nine
input: Party six
input: Party eight
input: Party eight
input: Party ten
input: Party six
input: Party eight
input: Party eight
input: Party seven
input: Party nine
input: Party seven
input: Party eight
input: Party seven
input: Party ten
input: Party nine
input: Party ten
input: Party nine
input: Party nine
input: Party nine
input: Party ten
input: Party nine
input: Party ten
input: Party ten
input: Party ten
input: Party four
input: Party four
input: Party one
output: Party ten
output: Party nine
output: Party eight
output: Party seven
output: Party six
output: Party five
output: Party four
output: Party three
output: Party two
output: Party one
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

parties = dict()
mode = None
for line in input_file:
    line = line.strip()
    if line == "PARTIES:":
        mode = "parties"
    elif line == "VOTES:":
        mode = "votes"
    else:
        if mode == "parties":
            parties[line] = 0
        elif mode == "votes":
            parties[line] += 1
input_file.close()

parties = [(party, score) for party, score in parties.items()]
parties.sort(key=lambda x: (-x[1], x[0]))

print(*[i[0] for i in parties], sep="\n")
