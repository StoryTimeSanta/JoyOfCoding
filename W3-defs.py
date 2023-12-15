# What does this program do?
# Richard Hudson


def double(x):
    return 2 * x


def quad(x):
    return double(double(x))


def hello(name):
    print("Hello", name + ", how are you today?")


def repeat (string, n):
    return string * n


def square(string, n):
    for i in range(n):
        print(repeat(string, n))


print(double(5))  # Will print 10
print(quad(4))  # Will print 16
hello("Joe")  # Will print Hello, Joe, how are you today?
print(repeat("hi", 10))  # will print hi 10 times
square("*", 4)  # Will print **** 4 times


# 1. What do you think def & return do?
    # def defines a function and return sends a value back to the calling function

# 2. What's the difference between return and print?
    # return sends the value back to the function and print displays on screen only
# 3. In the code above, identify the following:
    # a. Formal Parameters
        # double, quad, hello, repeat, square
    # b. Actual Parameters
        # x, name
    # c. Void functions
        # print,
    # d. Fruitful functions
        # return,
