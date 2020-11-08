def GetSlope (x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

x1,y1,x2,y2,x3,y3,x4,y4 = eval(input("Введите x1,y1,x2,y2,x3,y3,x4,y4: "))

if (GetSlope(x1,y1,x2,y2) == GetSlope(x3,y3,x4,y4)):
    print("Прямые параллельны")

else:
    print("Прямые не параллельны")
