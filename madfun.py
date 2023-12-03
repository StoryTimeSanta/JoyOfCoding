# Working with numeric functions
# Richard Hudson

# import math sqrt function
from math import sqrt

# Get a decimal number from the user
decimal = eval(input("Please enter a number with a decimal: "))
print("Absolute Value:", abs(decimal))
print("Rounded:", round(decimal, 0))
print("Square root:", (sqrt(abs(round(decimal)))))
