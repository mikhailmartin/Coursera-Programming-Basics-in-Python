"""
Школы с наибольшим числом участников олимпиады

В олимпиаде по информатике принимало участие N человек. Определите школы, из
которых в олимпиаде принимало участие больше всего участников. В этой задаче
необходимо считывать данные построчно, не сохраняя в памяти данные обо всех
участниках, а только подсчитывая число участников для каждой школы.


Формат ввода:
Информация о результатах олимпиады записана в файле, каждая из строк которого
имеет вид:

фамилия имя школа балл

Фамилия и имя — текстовые строки, не содержащие пробелов. Школа — целое число
от 1 до 99. Балл — целое число от 0 до 100.


Формат вывода:
Выведите номера этих школ в порядке возрастания.


Примеры:
Тест 1
input: Иванов Сергей 14 56
input: Сергеев Петр 23 74
input: Петров Василий 3 99
input: Васильев Андрей 3 56
input: Андреев Роман 14 75
input: Романов Иван 27 68
output: 3 14

Тест 2
input: Иванов Сергей 10 43
input: Сергеев Петр 20 24
input: Петров Василий 45 74
input: Васильев Андрей 10 24
input: Андреев Александр 15 45
input: Александров Роман 14 35
input: Романов Иван 11 45
input: Алексеев Сергей 10 56
input: Егоров Николай 1 56
input: Николаев Степан 3 15
output: 10

Тест 3
input: Иванов Сергей 10 43
input: Сергеев Петр 20 24
input: Петров Василий 45 74
input: Васильев Андрей 10 24
input: Андреев Александр 15 45
input: Александров Роман 14 35
input: Романов Иван 45 89
input: Алексеев Сергей 10 56
input: Егоров Николай 45 56
input: Николаев Степан 3 15
output: 10 45
"""
INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

count = dict()
for line in input_file:
    school = int(line.split()[-2])
    if school not in count.keys():
        count[school] = 1
    else:
        count[school] += 1
input_file.close()

max_count = max(count.values())
max_school = []
for key, value in count.items():
    if value == max_count:
        max_school.append(key)
max_school.sort()

output_file = open(OUTPUT_FILE_NAME, "w", encoding="utf8")
print(*max_school, file=output_file, end=" ")
output_file.close()
