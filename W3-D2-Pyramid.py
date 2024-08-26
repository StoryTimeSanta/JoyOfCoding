#Richard Hudson

# char = input("Please enter a key to build the pyramid: ")
# number = input("Please enter how tall to build the pyramid: ")

def pyramid(char, number):
    for i in range(1, number + 1):
        print(char * i)

def absolute_difference(num1, num2):
    diff = abs(num1 - num2)
    return diff

def main():
    print('pyramid("*", 2)')
    pyramid("*", 2)
    print('pyramid("+", 5)')
    pyramid("+", 5)
    print('pyramid("x", 10)')
    pyramid("x", 10)
    # Calculate and print differences
    diff1 = absolute_difference(5, 10)
    print("difference 5 10 =", diff1)
    diff2 = absolute_difference(10, 5)
    print("difference 10 5 =", diff2)
    diff3 = absolute_difference(200, -200)
    print("difference 200 -200 =", diff3)
    # print("difference 5 10", absolute_difference(5, 10) == 5)
    # print("difference 10 5", absolute_difference(10, 5) == 5)
    # print("difference 200 -200", absolute_difference(200, -200) == 400)

# absolute_difference(5, 10) 5
# absolute_difference(10, 5) 5
# absolute_difference(200, -200) 400

main()