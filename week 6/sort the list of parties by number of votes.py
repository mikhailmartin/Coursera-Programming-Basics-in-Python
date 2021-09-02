"""
Формат входных данных аналогичен предыдущей задаче. Выведите список всех
партий, участвовавших в выборах, отсортировав его в порядке убывания количества
голосов избирателей, а при равном количестве голосов - в лексикографическом
порядке.


Примеры:
Тест 1
Входные данные:
PARTIES:
Party one
Party two
Party three
VOTES:
Party one
Party two
Party three
Party two
Party three

Вывод программы:
Party three
Party two
Party one


Тест 2
Входные данные:
PARTIES:
Party one
Party two
Party three
Party four
Party five
Party six
Party seven
Party eight
Party nine
Party ten
VOTES:
Party three
Party five
Party seven
Party ten
Party four
Party eight
Party one
Party two
Party six
Party nine

Вывод программы:
Party eight
Party five
Party four
Party nine
Party one
Party seven
Party six
Party ten
Party three
Party two


Тест 3
Входные данные:
PARTIES:
Party three
Party one
Party five
Party nine
Party six
Party seven
Party eight
Party ten
Party four
Party two
VOTES:
Party two
Party five
Party seven
Party four
Party ten
Party four
Party three
Party seven
Party two
Party three
Party six
Party three
Party ten
Party six
Party nine
Party seven
Party five
Party eight
Party five
Party seven
Party ten
Party eight
Party five
Party nine
Party five
Party six
Party eight
Party six
Party nine
Party six
Party eight
Party eight
Party ten
Party six
Party eight
Party eight
Party seven
Party nine
Party seven
Party eight
Party seven
Party ten
Party nine
Party ten
Party nine
Party nine
Party nine
Party ten
Party nine
Party ten
Party ten
Party ten
Party four
Party four
Party one

Вывод программы:
Party ten
Party nine
Party eight
Party seven
Party six
Party five
Party four
Party three
Party two
Party one
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    parties = dict()
    mode = None
    for line in input_file:
        line = line.strip()
        if line == 'PARTIES:':
            mode = 'parties'
        elif line == 'VOTES:':
            mode = 'votes'
        else:
            if mode == 'parties':
                parties[line] = 0
            elif mode == 'votes':
                parties[line] += 1
    input_file.close()

    parties = [(party, score) for party, score in parties.items()]
    parties.sort(key=lambda x: (-x[1], x[0]))

    print(*[i[0] for i in parties], sep='\n')


main()
