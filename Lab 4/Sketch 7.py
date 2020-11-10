mas = [7, 7, 7, 7, 7, 7]

maximum = mas[0]

for i in range(1, len(mas)):
    if mas[i] > maximum:
            maximum = mas[i]

maximums = maximum

mas1 = mas

for i in range(0, len(mas1)):
    if mas1[i] < maximum:
        maximums = mas1[i]

if maximums == maximum:
    print("No")

else:
    for i in range(0, len(mas1)):
        if mas[i] > maximums and  mas1[i] < maximum:
            maximums = mas1[i]
    print(maximums)
