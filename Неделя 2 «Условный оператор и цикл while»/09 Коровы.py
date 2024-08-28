"""
Коровы

Для данного числа n<100 закончите фразу “На лугу пасется...” одним из
возможных продолжений: “n korov”, “n korova”, “n korovy”, правильно склоняя
слово “korova”.


Формат вводы:
Вводится натуральное число.


Формат вывода:
Программа должна вывести введенное число n и одно из слов: korov, korova или
korovy. Между числом и словом должен стоять ровно один пробел.


Примеры:
Тест 1
input: 1
output: 1 korova

Тест 2
input: 2
output: 2 korovy

Test 3
input: 3
output: 3 korovy
"""
number = int(input())

if (number // 10) % 10 == 1:
    print(number, "korov")
elif number % 10 == 1:
    print(number, "korova")
elif number % 10 in [2, 3, 4]:
    print(number, "korovy")
else:
    print(number, "korov")
