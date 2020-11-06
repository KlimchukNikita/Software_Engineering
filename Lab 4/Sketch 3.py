def IsPalindrome(number):
    if number < 0:
        return False

    else:
        k = number
        m = 0

        while k > 0:
            m = 10 * m + k % 10
            k = k // 10

            if m == number:
                return True

            else:
                return False

a = int(input("Введите целое положительное число: "))

print("Yes") if IsPalindrome(a) else print("No")
