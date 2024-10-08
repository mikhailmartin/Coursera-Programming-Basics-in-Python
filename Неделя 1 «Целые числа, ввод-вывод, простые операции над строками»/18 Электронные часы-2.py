"""
Электронные часы-2

Электронные часы показывают время в формате h:mm:ss, то есть сначала
записывается количество часов (число от 0 до 23), потом обязательно двузначное
количество минут, затем обязательно двузначное количество секунд. Количество
минут и секунд при необходимости дополняются до двузначного числа нулями.

С начала суток прошло N секунд. Выведите, что покажут часы.


Формат ввода:
Вводится число N — целое, неотрицательное.


Формат вывода:
Выведите показания часов, соблюдая формат.


Примечания:
Вывести числа можно поциферно.


Примеры:
Тест 1
input: 3602
output: 1:00:02
"""
number = int(input())

seconds = number % 60
first_digit_seconds = seconds // 10
second_digit_seconds = seconds % 10

minutes = (number // 60) % 60
first_digit_minutes = minutes // 10
second_digit_minutes = minutes % 10

hours = (number // 3600) % 24

print(
    hours,
    ":",
    first_digit_minutes,
    second_digit_minutes,
    ":",
    first_digit_seconds,
    second_digit_seconds,
    sep=""
)
