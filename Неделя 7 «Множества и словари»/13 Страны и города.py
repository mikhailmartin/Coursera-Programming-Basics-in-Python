"""
Страны и города

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
input: 2
input: Russia Moscow Petersburg Novgorod Kaluga
input: Ukraine Kiev Donetsk Odessa
input: 3
input: Odessa
input: Moscow
input: Novgorod
output: Ukraine
output: Russia
output: Russia

Тест 2
input: 5
input: A B
input: C D
input: E F
input: G H
input: I J
input: 5
input: J
input: H
input: F
input: D
input: B
output: I
output: G
output: E
output: C
output: A

Тест 3
input: 5
input: A B
input: C D E
input: F G H I
input: J K L M N
input: O P Q R S T
input: 15
input: T
input: S
input: N
input: R
input: M
input: I
input: Q
input: L
input: H
input: E
input: P
input: K
input: G
input: D
input: B
output: O
output: O
output: J
output: O
output: J
output: F
output: O
output: J
output: F
output: C
output: O
output: J
output: F
output: C
output: A
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")
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
