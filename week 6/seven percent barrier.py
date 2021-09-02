"""
В Государственную Думу Федерального Собрания Российской Федерации выборы
производятся по партийным спискам. Каждый избиратель указывает одну партию, за
которую он отдаёт свой голос. В Государственную Думу попадают партии, которые
набрали не менее 7% от числа голосов избирателей.

Дан список партий и список голосов избирателей. Выведите список партий, которые
попадут в Государственную Думу.


Формат ввода:
В первой строке входного файла написано слово PARTIES:. Далее идёт список
партий, участвующих в выборах.

Затем идёт строка, содержащая слово VOTES:. За ним идут названия партий, за
которые проголосовали избиратели, по одному названию в строке. Названия могут
быть только строками из первого списка.


Формат вывода:
Программа должна вывести названия партий, получивших не менее 7% от числа
голосов в том порядке, в котором они следуют в первом списке.


Примеры:
Тест 1
>>> PARTIES:
>>> Party one
>>> Party two
>>> Party three
>>> VOTES:
>>> Party one
>>> Party one
>>> Party three
>>> Party one
>>> Party one
>>> Party three
>>> Party two
>>> Party one
>>> Party three
>>> Party three
>>> Party one
>>> Party one
>>> Party three
>>> Party three
>>> Party one
Party one
Party three

Тест 2
>>> PARTIES:
>>> Party one
>>> VOTES:
>>> Party one
>>> Party one
>>> Party one
>>> Party one
>>> Party one
>>> Party one
>>> Party one
Party one

Тест 3
>>> PARTIES:
>>> The first party
>>> The best party
>>> VOTES:
>>> The best party
>>> The best party
>>> The best party
>>> The best party
>>> The best party
>>> The best party
>>> The best party
>>> The first party
>>> The best party
>>> The best party
>>> The best party
>>> The best party
>>> The best party
>>> The best party
The first party
The best party
"""


INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    parties = dict()
    vote_count = 0
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
                vote_count += 1
    input_file.close()

    for party, votes in parties.items():
        if votes / vote_count >= 0.07:
            print(party)


main()
