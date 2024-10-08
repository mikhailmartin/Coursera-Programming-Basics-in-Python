"""
Квартиры

В доме несколько подъездов. В каждом подъезде одинаковое количество квартир.
Квартиры нумеруются подряд, начиная с единицы. Может ли в некотором подъезде
первая квартира иметь номер x, а последняя – номер y?


Формат ввода:
Вводятся два натуральных числа x и y (x ≤ y).


Формат вывода:
Выведите слово YES (заглавными латинскими буквами), если такое возможно, и NO
в противном случае.


Примеры:
Тест 1
input: 11
input: 15
output: YES

Тест 2
input: 2
input: 10
output: NO
"""
x = int(input())
y = int(input())

if y % (y - x + 1) == 0:
    print("YES")
else:
    print("NO")
