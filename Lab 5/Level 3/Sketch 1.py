class Matrix:
    """Первый способ вывода матрицы"""
    def __init__(self, A):
        self.A = A
 
    def __str__(self):
        s = ''
        for row in self.A:
            for cell in row:
                s += f'{cell} '
            s += '\n'
        return s
 
B = [[1, 4], [2, 6]]

matrix = Matrix(B)
print(matrix)
