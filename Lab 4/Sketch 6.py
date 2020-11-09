def Sort(m):
    f=m.copy()
    if len(m)% 2 == 0:
        start = len(m)-2
        i = 0

        while start>-1:
            f[i] = m[start]
            start = start - 2
            i = i + 1
        start = 1

        while start<=len(m):
            f[i] = m[start]
            start = start + 2
            i = i + 1
    else:
        start = len(m)-1
        i = 0

        while start>-1:
            f[i] = m[start]
            start = start - 2
            i = i + 1
        start = 1

        while start<=len(m):
            f[i] = m[start]
            start = start + 2
            i = i + 1
    return f

c = [0,1,2,3,4,5,6,7,8,9,10,11]
g = Sort(c)

for i in g:
    print(i)
