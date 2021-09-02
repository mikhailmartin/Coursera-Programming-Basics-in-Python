"""
Добавьте в предыдущий класс следующие методы:
* __add__, принимающий вторую матрицу того же размера и возвращающий сумму
  матриц.
* __mul__, принимающий число типа int или float и возвращающий матрицу,
  умноженную на скаляр.
* __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том
  случае, аргумент находится справа. Для реализации этого метода в коде класса
  достаточно написать __rmul__ = __mul__.


Иллюстрация:
В следующем случае вызовется __mul__: Matrix([[0, 1], [1, 0]) * 10.
В следующем случае вызовется __rmul__ (так как у int не определен __mul__ для
матрицы справа): 10 * Matrix([[0, 1], [1, 0]).

Разумеется, данные методы не должны менять содержимое матрицы.


Формат ввода:
Как в предыдущей задаче.


Формат вывода:
Как в предыдущей задаче.


Примеры:
Тест 1
>>> m = Matrix([[10, 10], [0, 0], [1, 1]])
>>> print(m.size())
(3, 2)

Тест 2
>>> m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
>>> m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
>>> print(m1 + m2)
1	1	0
20	1	-1
-1	-2	1

Тест 3
>>> m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
>>> alpha = 15
>>> print(m * alpha)
>>> print(alpha * m)
15	15	0
0	30	150
150	225	450
15	15	0
0	30	150
150	225	450
"""

from sys import stdin
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        matrix = []
        for i in range(self.size()[0]):
            line = []
            for j in range(self.size()[1]):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            matrix.append(line)
        return Matrix(matrix)

    def __mul__(self, other):
        matrix = []
        for i in range(self.size()[0]):
            line = []
            for j in range(self.size()[1]):
                line.append(self.matrix[i][j] * other)
            matrix.append(line)
        return Matrix(matrix)

    __rmul__ = __mul__

    def size(self):
        num_lines = len(self.matrix)
        num_columns = len(self.matrix[0])
        return num_lines, num_columns


exec(stdin.read())
