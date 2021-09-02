from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)

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

    def transpose(self):
        t_matrix = list(zip(*self.matrix))
        self.matrix = t_matrix
        return Matrix(t_matrix)

    @staticmethod
    def transposed(matrix):
        t_matrix = list(zip(*matrix.matrix))
        return Matrix(t_matrix)


exec(stdin.read())
