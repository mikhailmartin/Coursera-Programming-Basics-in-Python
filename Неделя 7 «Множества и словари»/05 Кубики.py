"""
Кубики

Аня и Боря любят играть в разноцветные кубики, причём у каждого из них свой
набор и в каждом наборе все кубики различны по цвету. Однажды дети
заинтересовались, сколько существуют цветов таких, что кубики каждого цвета
присутствуют в обоих наборах. Для этого они занумеровали все цвета случайными
числами. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в
оставшейся части. Номер любого цвета — это целое число в пределах от 0 до 10⁹.


Формат ввода:
В первой строке входного файла записаны числа N и M — количество кубиков у Ани
и Бори соответственно. В следующих N строках заданы номера цветов кубиков Ани.
В последних M строках номера цветов кубиков Бори.


Формат вывода:
Выведите сначала количество, а затем отсортированные по возрастанию номера
цветов таких, что кубики каждого цвета есть в обоих наборах, затем количество и
отсортированные по возрастанию номера остальных цветов у Ани, потом количество
и отсортированные по возрастанию номера остальных цветов у Бори.


Примечание:
Для ускорения ввода попробуйте использовать чтение входных данных из файла.


Примеры:
Тест 1
input: 4 3
input: 0
input: 1
input: 10
input: 9
input: 1
input: 3
input: 0
output: 2
output: 0 1
output: 2
output: 9 10
output: 1
output: 3

Тест 2
input: 2 2
input: 1
input: 2
input: 2
input: 3
output: 1
output: 2
output: 1
output: 1
output: 1
output: 3

Тест 3
input: 0 0
output: 0
output:
output: 0
output:
output: 0
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

n, m = map(int, input_file.readline().split())
anyas = set()
boryas = set()

for i in range(n):
    anyas.add(int(input_file.readline()))
for i in range(m):
    boryas.add(int(input_file.readline()))
input_file.close()

intersection = anyas & boryas
print(len(intersection))
print(*sorted(intersection))
anyas -= intersection
print(len(anyas))
print(*sorted(anyas))
boryas -= intersection
print(len(boryas))
print(*sorted(boryas))
