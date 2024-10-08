"""
Принадлежит ли точка области

Проверьте, принадлежит ли точка данной закрашенной области:

Если точка принадлежит области (область включает границы), выведите слово YES,
иначе выведите слово NO. Решение должно содержать функцию IsPointInArea(x, y),
возвращающую True, если точка принадлежит области и False, если не принадлежит.
Основная программа должна считать координаты точки, вызвать функцию
IsPointInArea и в зависимости от возвращенного значения вывести на экран
необходимое сообщение. Функция IsPointInArea не должна содержать инструкцию if.


Формат ввода:
Вводится два действительных числа.


Формат вывода:
Выведите ответ на задачу.


Замечание:
В задаче подразумевается, что нижняя область продолжается вниз бесконечно
(картинка может ввести в заблуждение, как будто область заканчивается на
y = -3.5).
input: 0
input: -5
output: YES


Примеры:
Тест 1
input: -4
input: -4
output: NO

Тест 2
input: -4
input: -3
output: NO

Тест 3
input: -4
input: -2
output: NO
"""


def is_point_in_area(x, y):

    a = (x + 1) ** 2 + (y - 1) ** 2 <= 2 ** 2 and x + y >= 0 and \
        y - 2 * x - 2 >= 0
    b = (x + 1) ** 2 + (y - 1) ** 2 >= 2 ** 2 and x + y <= 0 and \
        y - 2 * x - 2 <= 0

    return a or b


x = float(input())
y = float(input())

if is_point_in_area(x, y):
    print("YES")
else:
    print("NO")
