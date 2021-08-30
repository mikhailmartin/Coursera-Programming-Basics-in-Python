"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно
один раз разломить по прямой на две части. Определите, можно ли таким образом
отломить от шоколадки часть, состоящую ровно из k долек.


Формат ввода:
Программа получает на вход три числа: n, m, k.


Формат вывода:
Программа должна вывести одно из двух слов: YES или NO.


Примеры:
Тест 1
>>> 4
>>> 2
>>> 6
YES

Тест 2
>>> 2
>>> 10
>>> 7
NO
"""

n = int(input())
m = int(input())
k = int(input())
if k >= n * m:
    print("NO")
elif (k % n == 0) or (k % m == 0):
    print("YES")
else:
    print("NO")
