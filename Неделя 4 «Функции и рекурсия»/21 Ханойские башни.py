"""
Ханойские башни

Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами
1, 2, 3. На стержень 1 надета пирамидка из n дисков различного диаметра в
порядке убывания диаметра (снизу находится самый большой диск, а сверху — самый
маленький). Диски можно перекладывать с одного стержня на другой по одному, при
этом диск нельзя класть на диск меньшего диаметра. Необходимо переложить всю
пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.

Напишите программу, которая решает головоломку; для данного числа дисков n
печатает последовательность перекладываний в формате a b c, где a — номер
перекладываемого диска, b — номер стержня с которого снимается данный диск,
c — номер стержня на который надевается данный диск.

Например, строка 1 2 3 означает перемещение диска номер 1 со стержня 2 на
стержень 3. В одной строке печатается одна команда. Диски пронумерованы числами
от 1 до n в порядке возрастания диаметров.

Программа должна вывести минимальный (по количеству произведенных операций)
способ перекладывания пирамидки из данного числа дисков.


Указание:
Подумайте, как переложить пирамидку из одного диска? Из двух дисков? Из трёх
дисков? Из четырёх дисков? Пусть мы научились перекладывать пирамидку из n
дисков с произвольного стержня на любой другой, как переложить пирамидку из
n + 1 диска, если можно пользоваться решением для n дисков.

Напишите функцию move (n, x, y), которая печатает последовательность
перекладываний дисков для перемещения пирамидки высоты n со стержня номер x на
стержень номер y.


Формат ввода:
Вводится натуральное число — количество дисков.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 2
output: 1 1 2
output: 2 1 3
output: 1 2 3

Тест 2
input: 3
output: 1 1 3
output: 2 1 2
output: 1 3 2
output: 3 1 3
output: 1 2 1
output: 2 2 3
output: 1 1 3

Тест 3
input: 1
output: 1 1 3
"""


def hanoi(n, a, b):
    if n == 1:
        print(1, a, b)
    else:
        hanoi(n - 1, a, 6 - a - b)
        print(n, a, b)
        hanoi(n - 1, 6 - a - b, b)


n = int(input())
hanoi(n, 1, 3)
