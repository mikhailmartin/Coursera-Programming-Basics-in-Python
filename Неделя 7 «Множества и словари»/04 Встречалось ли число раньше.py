"""
Встречалось ли число раньше

Во входной строке записана последовательность чисел через пробел. Для каждого
числа выведите слово YES (в отдельной строке), если это число ранее встречалось
в последовательности или NO, если не встречалось.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Примеры:
Тест 1
input: 1 2 3 2 3 4
output: NO
output: NO
output: NO
output: YES
output: YES
output: NO
"""
a = list(map(int, input().split()))

b = set()
for num in a:
    print("YES" if num in b else "NO")
    b.add(num)
