import math

def IsDegree(a):
    i = j = 2
    a0 = 0

    while (i <= a):

        while (a0 < a):

            a0 = math.pow(i, j)

            if (a0 == a):
                return True

                j = j + 1
            i = i + 1

            return False

x = int(input("Введите натуральное число: "))

if IsDegree(x):
    print("Число является степенью натурального числа")

else:
    print("Число не является степенью натурального числа")
