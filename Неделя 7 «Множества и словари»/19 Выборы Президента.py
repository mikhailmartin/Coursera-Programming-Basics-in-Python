"""
Выборы Президента

В выборах Президента Российской Федерации побеждает кандидат, набравший свыше
половины числа голосов избирателей. Если такого кандидата нет, то во второй тур
выборов выходят два кандидата, набравших наибольшее число голосов.


Формат ввода:
Каждая строка входного файла содержит имя кандидата, за которого отдал голос
один избиратель. Известно, что общее число кандидатов не превосходит 20, но в
отличие от предыдущих задач список кандидатов явно не задан. Читайте данные из
файла input.txt с указанием кодировки utf8.


Формат вывода:
Если есть кандидат, набравший более 50% голосов, программа должна вывести его
имя. Если такого кандидата нет, программа должна вывести имя кандидата,
занявшего первое место, затем имя кандидата, занявшего второе место. Выводите
данные в файл output.txt с указанием кодировки utf8.


Примеры:
Тест 1
input: Полуэкт Варфоломеев
input: Варфоломей Полуэктов
input: Полуэкт Варфоломеев
output: Полуэкт Варфоломеев

Тест 2
input: Полуэкт Варфоломеев
input: Варфоломей Виссарионов
input: Виссарион Полуэктов
input: Варфоломей Виссарионов
input: Варфоломей Виссарионов
input: Полуэкт Варфоломеев
output: Варфоломей Виссарионов
output: Полуэкт Варфоломеев
"""
INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

candidates = dict()
count = 0
for line in input_file:
    candidate = line.strip()
    candidates[candidate] = candidates.get(candidate, 0) + 1
    count += 1
input_file.close()

lst = [(count, candidate) for candidate, count in candidates.items()]
lst.sort(reverse=True)

output_file = open(OUTPUT_FILE_NAME, "w", encoding="utf8")
print(lst[0][1], file=output_file)
if lst[0][0] <= count / 2:
    print(lst[1][1], file=output_file)
output_file.close()
