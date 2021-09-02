"""
Дана строка. Если в этой строке буква f встречается только один раз, выведите
её индекс. Если она встречается два и более раз, выведите индекс её первого и
последнего появления. Если буква f в данной строке не встречается, ничего не
выводите. При решении этой задачи нельзя использовать метод count и циклы.


Формат ввода:
Вводится строка.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
>>> comfort
3

Тест 2
>>> office
1 2

Тест 3
>>> hello

"""

s = input()
if s.find('f') != -1:
    print(s.find('f'), end=' ')
    if s.find('f', s.find('f') + 1) != -1:
        print(len(s) - s[::-1].find('f') - 1)