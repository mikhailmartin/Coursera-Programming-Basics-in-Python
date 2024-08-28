"""
Родословная: подсчёт уровней

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
input: 9
input: Alexei Peter_I
input: Anna Peter_I
input: Elizabeth Peter_I
input: Peter_II Alexei
input: Peter_III Anna
input: Paul_I Peter_III
input: Alexander_I Paul_I
input: Nicholaus_I Paul_I
output: Alexander_I 4
output: Alexei 1
output: Anna 1
output: Elizabeth 1
output: Nicholaus_I 4
output: Paul_I 3
output: Peter_I 0
output: Peter_II 2
output: Peter_III 2

Тест 2
input: 10
input: AQHFYP MKFXCLZBT
input: AYKOTYQ QIUKGHWCDC
input: IWCGKHMFM WPLHJL
input: MJVAURUDN QIUKGHWCDC
input: MKFXCLZBT IWCGKHMFM
input: PUTRIPYHNQ UQNGAXNP
input: QIUKGHWCDC WPLHJL
input: UQNGAXNP WPLHJL
input: YURTPJNR QIUKGHWCDC
output: AQHFYP 3
output: AYKOTYQ 2
output: IWCGKHMFM 1
output: MJVAURUDN 2
output: MKFXCLZBT 2
output: PUTRIPYHNQ 2
output: QIUKGHWCDC 1
output: UQNGAXNP 1
output: WPLHJL 0
output: YURTPJNR 2

Тест 3
input: 10
input: BFNRMLH CSZMPFXBZ
input: CSZMPFXBZ IHWBQDJ
input: FMVQTU FUXATQUGIG
input: FUXATQUGIG IRVAVMQKN
input: GNVIZ IQGIGUJZ
input: IHWBQDJ LACXYFQHSQ
input: IQGIGUJZ JMUPNYRQD
input: IRVAVMQKN GNVIZ
input: JMUPNYRQD BFNRMLH
output: BFNRMLH 3
output: CSZMPFXBZ 2
output: FMVQTU 9
output: FUXATQUGIG 8
output: GNVIZ 6
output: IHWBQDJ 1
output: IQGIGUJZ 5
output: IRVAVMQKN 7
output: JMUPNYRQD 4
output: LACXYFQHSQ 0
"""
INPUT_FILE_NAME = "input.txt"


input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")


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
