# Richard Hudson


# Write a function, pyramid, that takes a single character and a number as parameters and
# displays an ASCII art pyramid to the screen with numbered rows


def pyramid(char, number):
    for i in range(1, number):
        print(char * i)


# Write a function, absolute_difference, that takes two numbers as parameters and
# returns their absolute difference:


def absolute_difference(num1, num2):
    diff = abs(num1 - num2)
    return diff


def main():
    print("Difference 5 10", absolute_difference (5, 10) == 5)
    print("Difference 10 5", absolute_difference(10, 5) == 5)
    print("Difference 200 -200", absolute_difference(200, -200) == 400)
    print()

    pyramid("*",3)
    print()
    pyramid("+", 6)
    print()
    pyramid("X", 11)


main()
