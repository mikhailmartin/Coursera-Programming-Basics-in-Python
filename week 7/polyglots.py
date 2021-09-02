"""
Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.


Формат ввода:
Первая строка входных данных содержит количество школьников N. Далее идёт N
чисел Mᵢ, после каждого из чисел идёт Mᵢ строк, содержащих названия языков,
которые знает i-й школьник. Длина названий языков не превышает 1000 символов,
количество различных языков не более 1000. 1 ≤ N ≤ 1000, 1 ≤ Mᵢ ≤ 500.


Формат вывода:
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких
языков.


Примеры:
Тест 1
>>> 3
>>> 3
>>> Russian
>>> English
>>> Japanese
>>> 2
>>> Russian
>>> English
>>> 1
>>> English
1
English
3
Russian
Japanese
English
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    allknown_langs = set()
    all_langs = set()

    n = int(input_file.readline())
    for i in range(n):
        m = int(input_file.readline())
        current_langs = set()
        for j in range(m):
            lang = input_file.readline().strip()
            current_langs.add(lang)
        all_langs |= current_langs
        if i == 0:
            allknown_langs = current_langs
        else:
            allknown_langs &= current_langs
    input_file.close()

    print(len(allknown_langs))
    print(*allknown_langs, sep='\n')
    print(len(all_langs))
    print(*all_langs, sep='\n')


main()
