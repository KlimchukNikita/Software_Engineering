#«Второй максимум»
# Ввести последовательность S и вывести второй максимум этой последовательности,
# т. е. элемент a∈S : ∃ b∈S : b>a и a⩾c ∀c∈S, c≠b
# Если второго максимума нет, вывести NO
# Пользоваться функциями наподобие max() или sorted() нельзя

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
