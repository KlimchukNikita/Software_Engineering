import math

def isInside(x0, y0, r, x, y):
    if math.pow(x-x0,2) + math.pow(y-y0,2) > r*r:
        return False

    else:
        return True

X0, Y0, R = eval(input("Введите координаты X и Y центра окружности и радиус R: "))
isAllInside = True

while True:
    X, Y = eval(input("Введите координаты X и Y точки: "))
    if X == 0 and Y == 0:
        print ("Все точки принадлежат кругу") if isAllInside else print ("Не все точки принадлежат кругу")
        break

    if isInside(X0, Y0, R, X, Y):
        print("Точка принадлежит кругу")

    else:
        print("Точка не принадлежит кругу")
        isAllInside = False
