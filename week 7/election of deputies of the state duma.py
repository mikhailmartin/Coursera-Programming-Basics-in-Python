"""
Статья 83 закона “О выборах депутатов Государственной Думы Федерального
Собрания Российской Федерации” определяет следующий алгоритм пропорционального
распределения мест в парламенте.

Необходимо распределить 450 мест между партиями, участвовавших в выборах.
Сначала подсчитывается сумма голосов избирателей, поданных за каждую партию и
подсчитывается сумма голосов, поданных за все партии. Эта сумма делится на 450,
получается величина, называемая “первое избирательное частное” (его смысл - это
количество голосов избирателей, которое необходимо набрать для получения одного
места в парламенте). Далее каждая партия получает столько мест в парламенте,
чему равна целая часть от деления числа голосов за данную партию на первое
избирательное частное. Если после первого раунда распределения мест сумма
количества мест, отданных партиям, меньше 450, то оставшиеся места передаются
по одному партиям, в порядке убывания дробной части частного от деления числа
голосов за данную партию на первое избирательное частное. Если же для двух
партий эти дробные части равны, то преимущество отдаётся той партии, которая
получила большее число голосов.


Формат ввода:
На вход программе подаётся список партий, участвовавших в выборах. Каждая
строка входного файла содержит название партии (строка, возможно, содержащая
пробелы), затем, через пробел, количество голосов, полученных данной партией –
число, не превосходящее 10⁸.


Формат вывода:
Программа должна вывести названия всех партий и количество голосов в
парламенте, полученных данной партией. Названия необходимо выводить в том же
порядке, в котором они шли во входных данных.


Примеры:
Тест 1
>>> Party One 100000
>>> Party Two 200000
>>> Party Three 400000
Party One 64
Party Two 129
Party Three 257

Тест 2
>>> Party number one 100
>>> Partytwo 100
Party number one 225
Partytwo 225

Тест 3
>>> Party number one 449
>>> Partytwo 1
Party number one 449
Partytwo 1
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    vote_dict = dict()
    num_dict = dict()
    vote_count = 0
    for i, line in enumerate(input_file):
        line = line.split()
        party = ' '.join(line[:len(line) - 1])
        votes = int(line[-1])

        vote_dict[party] = vote_dict.get(party, 0) + votes
        vote_count += votes

        num_dict[party] = i
    input_file.close()

    first_electoral_quotient = vote_count / 450

    place_dict = dict()
    part_dict = dict()
    empty_places = 450
    for party, votes in vote_dict.items():
        places = int(votes // first_electoral_quotient)
        place_dict[party] = places
        empty_places -= places

        part = votes % first_electoral_quotient
        part_dict[party] = part

    for party, part in sorted(part_dict.items(), key=lambda x: -x[1]):
        if empty_places:
            place_dict[party] += 1
            empty_places -= 1
        else:
            break

    for party, i in sorted(num_dict.items(), key=lambda x: x[1]):
        print(party, place_dict[party])


main()
