"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для
каждого города укажите, в какой стране он находится.


Формат ввода:
Программа получает на вход количество стран N. Далее идёт N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны.
Название каждого город состоит из одного слова. В следующей строке записано
число M, далее идут M запросов — названия каких-то M городов, перечисленных
выше.


Формат вывода:
Для каждого из запроса выведите название страны, в котором находится данный
город.


Примеры:
Тест 1
>>> 2
>>> Russia Moscow Petersburg Novgorod Kaluga
>>> Ukraine Kiev Donetsk Odessa
>>> 3
>>> Odessa
>>> Moscow
>>> Novgorod
Ukraine
Russia
Russia

Тест 2
>>> 5
>>> A B
>>> C D
>>> E F
>>> G H
>>> I J
>>> 5
>>> J
>>> H
>>> F
>>> D
>>> B
I
G
E
C
A

Тест 3
>>> 5
>>> A B
>>> C D E
>>> F G H I
>>> J K L M N
>>> O P Q R S T
>>> 15
>>> T
>>> S
>>> N
>>> R
>>> M
>>> I
>>> Q
>>> L
>>> H
>>> E
>>> P
>>> K
>>> G
>>> D
>>> B
O
O
J
O
J
F
O
J
F
C
O
J
F
C
A
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')
    n = int(input_file.readline())
    my_dict = dict()
    for i in range(n):
        line = input_file.readline().split()
        country = line[0]
        cities = line[1:]

        for city in cities:
            my_dict[city] = country

    m = int(input_file.readline())
    for j in range(m):
        city = input_file.readline().strip()
        print(my_dict[city])


main()
