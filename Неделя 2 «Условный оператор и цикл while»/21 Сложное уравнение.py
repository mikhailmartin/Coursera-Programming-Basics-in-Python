"""
Сложное уравнение

Решить в целых числах уравнение: (ax + b) / (cx + d) = 0


Формат ввода:
Вводятся 4 числа: a, b, c, d; c и d не равны нулю одновременно.


Формат вывода:
Необходимо вывести все решения, если их число конечно, “NO” (без кавычек), если
решений нет, и “INF” (без кавычек), если решений бесконечно много.


Примеры:
Тест 1
input: 1
input: 1
input: 2
input: 2
output: NO

Тест 2
input: 2
input: -4
input: 7
input: 1
output: 2
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a == 0) and (b == 0):
    print("INF")
elif a == 0:
    print("NO")
elif b == 0:
    if d == 0:
        print("NO")
    else:
        print("0")
else:
    x = -b / a
    if x % 1 == 0:
        if (c * x + d) == 0:
            print("NO")
        else:
            print(int(x))
    else:
        print("NO")
