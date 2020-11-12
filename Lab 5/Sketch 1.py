A = [[1, 4], [2, 6]]

s = ''

for row in A:
    for cell in row:
        s += f'{cell} '
    s += '\n'

print(s)
