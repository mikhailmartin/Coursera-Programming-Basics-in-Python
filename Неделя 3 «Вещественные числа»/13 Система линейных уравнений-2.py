"""
Система линейных уравнений-2

Даны числа a, b, c, d, e, f. Решите систему линейных уравнений
ax + by = e
cx + dy = f


Формат ввода:
Вводятся 6 чисел a, b, c, d, e, f — коэффициенты уравнений.


Формат вывода:
Вывод программы зависит от вида решения этой системы.

Если система не имеет решений, то программа должна вывести единственное число
0.

Если система имеет бесконечно много решений, каждое из которых имеет вид
y = px + q, то программа должна вывести число 1, а затем значения p и q.

Если система имеет единственное решение (x₀, y₀), то программа должна вывести
число 2, а затем значения x₀ и y₀.

Если система имеет бесконечно много решений вида x=x₀, y — любое, то программа
должна вывести число 3, а затем значение x₀.

Если система имеет бесконечно много решений вида y = y₀, x — любое, то
программа должна вывести число 4, а затем значение y₀.

Если любая пара чисел (x, y) является решением, то программа должна вывести
число 5.


Примеры:
Тест 1
input: 1
input: 0
input: 0
input: 1
input: 3
input: 3
output: 2 3 3

Тест 2
input: 1
input: 1
input: 2
input: 2
input: 1
input: 2
output: 1 -1 1

Тест 3
input: 0
input: 2
input: 0
input: 4
input: 1
input: 2
output: 4 0.5
"""
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == b == c == d == e == f == 0:
    print('5')
elif a * d == b * c and a * f != c * e:
    print('0')
elif a == 0 == b and e != 0:
    print('0')
elif c == 0 == d and f != 0:
    print('0')
elif a == 0 == c and b * f != d * e:
    print('0')
elif b == 0 == d and a * f != c * e:
    print('0')
elif a * d == b * c and a * f == c * e:
    if b == d == 0:
        if a != 0 and c != 0:
            print('3', e / a)
        elif a == 0:
            if e == 0:
                print('3', f / c)
        elif c == 0:
            if f == 0:
                print('3', e / a)
    elif a == c == 0:
        if b != 0:
            print('4', e / b)
        elif d != 0:
            print('4', f / d)
    elif b != 0:
        print('1', -a / b, e / b)
    elif d != 0:
        print('1', -c / d, f / d)
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print('2', x, y)
