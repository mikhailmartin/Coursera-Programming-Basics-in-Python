"""
Делёж яблок-2

N школьников поделили K яблок поровну, не делящийся остаток остался в корзинке.
Сколько яблок осталось в корзинке?


Формат ввода:
Программа получает на вход числа N и K — натуральные, не превышают 10000.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 3
input: 14
output: 2
"""
number_schoolchild = int(input())
number_apples = int(input())

apples_per_schoolchild = number_apples % number_schoolchild
print(apples_per_schoolchild)
