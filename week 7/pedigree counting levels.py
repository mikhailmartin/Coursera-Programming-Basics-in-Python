"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно
один родитель. Каждому элементу дерева сопоставляется целое неотрицательное
число, называемое высотой. У родоначальника высота равна 0, у любого другого
элемента высота на 1 больше, чем у его родителя. Вам дано генеалогическое
древо, определите высоту всех его элементов.


Формат ввода:
Программа получает на вход число элементов в генеалогическом древе N. Далее
следует N - 1 строка, задающие родителя для каждого элемента древа, кроме
родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.


Формат вывода:
Программа должна вывести список всех элементов древа в лексикографическом
порядке. После вывода имени каждого элемента необходимо вывести его высоту.


Примечания:
Эта задача имеет решение сложности O(n), но вам достаточнонаписать решение
сложности O(n²) (не считая сложности обращения к элементам словаря). Пример
ниже соответствует приведённому древу рода Романовых.


Примеры:
Тест 1
>>> 9
>>> Alexei Peter_I
>>> Anna Peter_I
>>> Elizabeth Peter_I
>>> Peter_II Alexei
>>> Peter_III Anna
>>> Paul_I Peter_III
>>> Alexander_I Paul_I
>>> Nicholaus_I Paul_I
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2

Тест 2
>>> 10
>>> AQHFYP MKFXCLZBT
>>> AYKOTYQ QIUKGHWCDC
>>> IWCGKHMFM WPLHJL
>>> MJVAURUDN QIUKGHWCDC
>>> MKFXCLZBT IWCGKHMFM
>>> PUTRIPYHNQ UQNGAXNP
>>> QIUKGHWCDC WPLHJL
>>> UQNGAXNP WPLHJL
>>> YURTPJNR QIUKGHWCDC
AQHFYP 3
AYKOTYQ 2
IWCGKHMFM 1
MJVAURUDN 2
MKFXCLZBT 2
PUTRIPYHNQ 2
QIUKGHWCDC 1
UQNGAXNP 1
WPLHJL 0
YURTPJNR 2

Тест 3
>>> 10
>>> BFNRMLH CSZMPFXBZ
>>> CSZMPFXBZ IHWBQDJ
>>> FMVQTU FUXATQUGIG
>>> FUXATQUGIG IRVAVMQKN
>>> GNVIZ IQGIGUJZ
>>> IHWBQDJ LACXYFQHSQ
>>> IQGIGUJZ JMUPNYRQD
>>> IRVAVMQKN GNVIZ
>>> JMUPNYRQD BFNRMLH
BFNRMLH 3
CSZMPFXBZ 2
FMVQTU 9
FUXATQUGIG 8
GNVIZ 6
IHWBQDJ 1
IQGIGUJZ 5
IRVAVMQKN 7
JMUPNYRQD 4
LACXYFQHSQ 0
"""

INPUT_FILE_NAME = 'input.txt'


def main():
    input_file = open(INPUT_FILE_NAME, 'r', encoding='utf8')

    def height(name):
        return 0 if name not in pedigree else height(pedigree[name]) + 1

    n = int(input_file.readline())
    pedigree = dict()
    for _ in range(n - 1):
        child, parent = input_file.readline().split()
        pedigree[child] = parent

    all_persons = set(pedigree.keys() | pedigree.values())
    for person in sorted(all_persons):
        print(person, height(person))


main()
