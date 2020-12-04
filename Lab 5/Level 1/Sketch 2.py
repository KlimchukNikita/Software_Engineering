# Вывести построчно матрицу 2x3

A = [[1, 2, 3], [4, 5, 6]]

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()
