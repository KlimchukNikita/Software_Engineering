# Вывести построчно матрицу 2x3
# Реализовать в виде класса

class Matrix:
    def __init__(self, value=None, rows=0, cols=0):
        if value is None:
            # Проверка, что rows > 0
            # Проверка, что cols > 0
            self.value = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.value = value

    def __str__(self):
        s = ''
        for row in self.value:
            for cell in row:
                s += f'{cell} '
            s += '\n'
        return s

    def row_count(self):
        return len(self.value)

    def col_count(self):
        # Проверка, что есть хотя бы одна строка
        return len(self.value[0])

    def set_one(self):
        pass

    def set_zero(self):
        pass

    def transpose(self):
        pass

    def get_range(self):
        return 0

    def det(self):
        # Матрица не квадратная
        # Матрица вырожденная
        return 0

    def __add__(self, other):
        # Если other - не Matrix - кидаем Exception
        # Если не совпали размерности - кидаем Exception
        res = Matrix(None, self.row_count(), self.col_count())
        for row_idx in range(len(self.value)):
            for col_idx in range(len(self.value[row_idx])):
                res.value[row_idx][col_idx] = self.value[row_idx][col_idx] + other.value[row_idx][col_idx]
        return res

    def __mul__(self, other):
        # Если other - не Matrix - кидаем Exception
        # Если не совпали размерности - кидаем Exception
        pass

A = Matrix([[1, 2, 3], [4, 5, 6]])
B = Matrix(None, 2, 3)

print('Matrix A:')
print(A)

B.value[1][1] = 1

print('Matrix B:')
print(B)

C = A + B

print('Matrix C:')
print(C)
