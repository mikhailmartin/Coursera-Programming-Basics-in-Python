"""
Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
Определите, можно ли разместить одну из этих коробок внутри другой, при
условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.


Формат ввода:
Программа получает на вход числа A₁, B₁, C₁, A₂, B₂, C₂.


Формат вывода:
Программа должна вывести одну из следующих строчек:
- Boxes are equal, если коробки одинаковые,
- The first box is smaller than the second one, если первая коробка может быть
  положена во вторую,
- The first box is larger than the second one, если вторая коробка может быть
  положена в первую,
- Boxes are incomparable, во всех остальных случаях.


Примеры:
Тест 1
>>> 1
>>> 2
>>> 3
>>> 3
>>> 2
>>> 1
Boxes are equal

Тест 2
>>> 2
>>> 2
>>> 3
>>> 3
>>> 2
>>> 1
The first box is larger than the second one
"""

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
# упорядочиваем размеры первой коробки
if a1 > b1:
    a1, b1, c1 = b1, a1, c1
if b1 > c1:
    a1, b1, c1 = a1, c1, b1
if a1 > b1:
    a1, b1, c1 = b1, a1, c1
# упорядочиваем размеры второй коробки
if a2 > b2:
    a2, b2, c2 = b2, a2, c2
if b2 > c2:
    a2, b2, c2 = a2, c2, b2
if a2 > b2:
    a2, b2, c2 = b2, a2, c2
# анализируем размеры
if (a1 == a2) and (b1 == b2) and (c1 == c2):
    print("Boxes are equal")
elif (a1 <= a2) and (b1 <= b2) and (c1 <= c2):
    print("The first box is smaller than the second one")
elif (a1 >= a2) and (b1 >= b2) and (c1 >= c2):
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
