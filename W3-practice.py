# Write a function, pyramid, that takes a single character and a number as parameters and
# displays an ASCII art pyramid to the screen with numbered rows
#Richard Hudson

# print("*")
# print("*" * 2)
#
# for i in range (1, 6):
#     print("+" * i)


def pyramid(char, number):
    for i in range(1, number):
        print(char * i)


pyramid("*",3)
pyramid("+", 6)
pyramid("X", 11)

