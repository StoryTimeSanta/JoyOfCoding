# JOC W3 Writing Functions
# Richard Hudson

# num1 = 3
# num2 = 6


def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def main():
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    summ = add(num1, num2)
    print("The sum is:", summ)
    product = multiply(num1, num2)
    print("The product is:", product)


main()
