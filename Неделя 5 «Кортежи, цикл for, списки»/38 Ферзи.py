"""
Ферзи

Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди
них пара бьющих друг друга.


Формат ввода:
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
координаты 8 ферзей.


Формат вывода:
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


Примеры:
Тест 1
input: 1 7
input: 2 4
input: 3 2
input: 4 8
input: 5 6
input: 6 1
input: 7 3
input: 8 5
output: NO

Тест 2
input: 1 8
input: 2 7
input: 3 6
input: 4 5
input: 5 4
input: 6 3
input: 7 2
input: 8 1
output: YES

Тест 3
input: 3 4
input: 8 5
input: 4 1
input: 7 3
input: 6 6
input: 1 7
input: 5 8
input: 2 2
output: YES
"""
xs = []
ys = []
difs_xy = []
sums_xy = []
for i in range(8):
    x, y = map(int, input().split())
    dif_xy = x - y
    sum_xy = x + y

    xs.append(x)
    ys.append(y)
    difs_xy.append(dif_xy)
    sums_xy.append(sum_xy)

xs = set(xs)
ys = set(ys)
difs_xy = set(difs_xy)
sums_xy = set(sums_xy)
if len(xs) == 8 and len(ys) == 8 and len(difs_xy) == 8 and len(sums_xy) == 8:
    print("NO")
else:
    print("YES")
