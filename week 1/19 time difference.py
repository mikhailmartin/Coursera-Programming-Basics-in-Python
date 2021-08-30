"""
Даны два момента времени в пределах одних и тех же суток. Для каждого момента
указан час, минута и секунда. Известно, что второй момент времени наступил не
раньше первого.

Определите сколько секунд прошло между двумя моментами времени.


Формат ввода:
Программа на вход получает шесть целых чисел через перевод строки. Первые три
целых числа соответствуют часам, минутам и секундам первого момента, следующие
три числа соответствуют второму моменту.

Часы задаются числом от 0 до 23 включительно. Минуты и секунды  —  от 0 до 59.


Формат вывода:
Выведите число секунд между этими моментами времени.


Примеры:
Тест 1
>>> 1
>>> 1
>>> 1
>>> 2
>>> 2
>>> 2
3661
"""

tic_hours = int(input())
tic_minutes = int(input())
tic_seconds = int(input())
toc_hours = int(input())
toc_minutes = int(input())
toc_seconds = int(input())

tic = tic_hours * 3600 + tic_minutes * 60 + tic_seconds
toc = toc_hours * 3600 + toc_minutes * 60 + toc_seconds
time_difference = toc - tic
print(time_difference)
