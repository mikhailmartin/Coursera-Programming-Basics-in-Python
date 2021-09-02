"""
В одну транспортную компанию поступил заказ на перевозку двух ящиков из одного
города в другой. Для перевозки ящики решено было упаковать в специальный
контейнер.

Ящики и контейнер имеют вид прямоугольных параллелепипедов. Длина, ширина и
высота первого ящика  —  l₁, w₁ и h₁, соответствующие размеры второго ящика –
l₂, w₂ и h₂. Контейнер имеет длину, ширину и высоту lc, wc и hc.

Поскольку ящики содержат хрупкое оборудование, после упаковки в контейнер
каждый из них должен остаться в строго вертикальном положении. Таким образом,
ящики можно разместить рядом или один на другом. Для надёжного закрепления в
контейнере стороны ящиков должны быть параллельны его сторонам. Иначе говоря,
если исходно ящики были расположены так, что все их стороны параллельны
соответствующим сторонам контейнера, то каждый из них разрешается перемещать и
поворачивать относительно вертикальной оси на угол, кратный 90 градусам
(относительно горизонтальной оси ни контейнер, ни ящики поворачивать нельзя).

Разумеется, после упаковки оба ящика должны полностью находиться внутри
контейнера и не должны пересекаться.

Выясните, можно ли поместить ящики в контейнер с соблюдением указанных условий.


Формат ввода:
Во входных данных записаны числа l₁, w₁, h₁, l₂, w₂, h₂, lc, wc и hc. Все
размеры  —  целые положительные числа, не превышающие 1000. Числа в строках
разделены пробелами.


Примеры:
Тест 1
>>> 2
>>> 2
>>> 3
>>> 3
>>> 3
>>> 3
>>> 3
>>> 5
>>> 3
YES

Тест 2
>>> 2
>>> 3
>>> 3
>>> 3
>>> 2
>>> 3
>>> 4
>>> 4
>>> 4
YES

Тест 3
>>> 4
>>> 1
>>> 2
>>> 3
>>> 3
>>> 2
>>> 4
>>> 3
>>> 4
YES

Тест 4
>>> 1
>>> 1
>>> 4
>>> 1
>>> 1
>>> 3
>>> 10
>>> 10
>>> 3
NO

Тест 5
>>> 3
>>> 2
>>> 2
>>> 3
>>> 1
>>> 2
>>> 5
>>> 2
>>> 3
NO
"""

# габариты первой коробки
l1 = int(input())
w1 = int(input())
h1 = int(input())
# габариты второй коробки
l2 = int(input())
w2 = int(input())
h2 = int(input())
# габариты контейнера
lc = int(input())
wc = int(input())
hc = int(input())

# пусть сторона, которая длиннее будет длиной, а которая короче, шириной
if l1 < w1:
    l1, w1 = w1, l1
if l2 < w2:
    l2, w2 = w2, l2
if lc < wc:
    lc, wc = wc, lc

# ящик не пролезает хотя бы по одному размеру
if h1 > hc or h2 > hc or l1 > lc or l2 > lc or w1 > wc or w2 > wc:
    print('NO')
# можно поставить оба вдоль или один на другой
elif l1 + l2 <= lc or w1 + w2 <= wc or h1 + h2 <= hc:
    print('YES')
# один вдоль, другой поперек
elif l1 + w2 <= lc and (l2 <= wc or l1 <= wc):
    print('YES')
# оба поперек
elif w1 + w2 <= lc and l1 <= wc and l2 <= wc:
    print('YES')
# ящик не пролезает хотя бы по одному размеру
else:
    print('NO')