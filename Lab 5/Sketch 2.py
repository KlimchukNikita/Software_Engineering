class Matrix:
    def __init__(self, B):
        self.B = B

    def __str__(self):
        for i in range(len(A)):
            for j in range(len(A[i])):
                print(A[i][j], end=' ')
            print()

A = [[1, 2, 3], [4, 5, 6]]

matrix = Matrix(A)
print(matrix)
