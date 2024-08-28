"""
Делаем срезы

Формат ввода:
Дана строка.


Формат вывода:
Сначала выведите третий символ этой строки.

Во второй строке выведите предпоследний символ этой строки.

В третьей строке выведите первые пять символов этой строки.

В четвертой строке выведите всю строку, кроме последних двух символов.

В пятой строке выведите все символы с чётными индексами (считая, что индексация
начинается с 0, поэтому символы выводятся начиная с первого).

В шестой строке выведите все символы с нечётными индексами, то есть начиная со
второго символа строки.

В седьмой строке выведите все символы в обратном порядке.

В восьмой строке выведите все символы строки через один в обратном порядке,
начиная с последнего.

В девятой строке выведите длину данной строки.


Примечание:
Данная строка имеет достаточную длину для выполнения всех предложенных срезов.


Примеры:
Тест 1
input: Abrakadabra
output: r
output: r
output: Abrak
output: Abrakadab
output: Arkdba
output: baaar
output: arbadakarbA
output: abdkrA
output: 11

Тест 2
input: Hello
output: l
output: l
output: Hello
output: Hel
output: Hlo
output: el
output: olleH
output: olH
output: 5

Тест 3
input: qwertyuiop
output: e
output: o
output: qwert
output: qwertyui
output: qetuo
output: wryip
output: poiuytrewq
output: piyrw
output: 10
"""
s = input()

print(s[2])
print(s[-2])
print(s[0:5])
print(s[:len(s) - 2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))
