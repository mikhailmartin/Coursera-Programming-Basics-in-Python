"""
Угадай число-2

Август и Беатриса продолжают играть в игру, но Август начал жульничать. На
каждый из вопросов Беатрисы он выбирает такой вариант ответа YES или NO, чтобы
множество возможных задуманных чисел оставалось как можно больше. Например,
если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2, то
Август ответит NO, а если Беатриса спросит про 1, 2, 3, то Август ответит YES.
Если же Бетриса в своём вопросе перечисляет ровно половину из задуманных чисел,
то Август из вредности всегда отвечает NO. Наконец, Август при ответе учитывает
все предыдущие вопросы Беатрисы и свои ответы на них, то есть множество
возможных задуманных чисел уменьшается.


Формат ввода:
Вам дана последовательность вопросов Беатрисы. Приведите ответы Августа на них.
Первая строка входных данных содержит число n — наибольшее число, которое мог
загадать Август. Далее идут строки, содержащие вопросы Беатрисы. Каждая строка
представляет собой набор чисел, разделённых пробелами. Последняя строка входных
данных содержит одно слово HELP.


Формат вывода:
Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос. После этого
выведите (через пробел, в порядке возрастания) все числа, которые мог загадать
Август после ответа на всевопросы Беатрисы.


Примеры:
Тест 1
input: 10
input: 1 2 3 4 5
input: 2 4 6 8 10
input: HELP
output: NO
output: YES
output: 6 8 10

Тест 2
input: 10
input: 1
input: 2
input: 3
input: 4
input: 5
input: 6
input: 7
input: 8
input: 9
input: HELP
output: NO
output: NO
output: NO
output: NO
output: NO
output: NO
output: NO
output: NO
output: NO
output: 10

Тест 3
input: 16
input: 1 2 3 4 5 6 7 8
input: 9 10 11 12
input: 13 14
input: 16
input: HELP
output: NO
output: NO
output: NO
output: NO
output: 15
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

n = int(input_file.readline())
st = set(range(1, n + 1))

for line in input_file:
    if line.strip() == "HELP":
        break

    current_st = set(map(int, line.split()))
    yes_st = st & current_st
    no_st = st - current_st
    if len(yes_st) > len(no_st):
        print("YES")
        st = yes_st
    else:
        print("NO")
        st = no_st
input_file.close()

print(*sorted(st))
