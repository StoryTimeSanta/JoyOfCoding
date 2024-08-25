# Fun with Functions
# Richard Hudson

import math
from math import sqrt

# Math fun

print("The square root of 25 is", sqrt(25))
print("The log10 of 100 is", math.log10(100))
print("The absolute value of -5 is", abs(-5))

# string fun

phrase = "find your yoda"

print(phrase.upper())
print(phrase.title())
print(phrase.count('o'))
print(phrase.lower())
print(phrase.isdecimal())

# Questions
# 1 What do you think import does?
# Loads function math into RAM.
# 2 What is the difference between import on line 6 vs 7? Does it change how the math functions are called? In what way?
# Changes wheter the module name is needed
# 3 Why do you think we need to import math, but not abs? absolute is built in (it is just a value)
# 4 How are math functions called differently from string functions as compared to other functions we’ve seen so far?
# module.function vs string variable
# 5 In the code above, identify the following:
# a. Comments - everything with a # at the beginning
# b. Variables - phrase (look for an identifier to the left of an = sign)
# c. Function calls - Look for identifier before()
# d. Expressions - no expressions
# e. Assignments - variables numerics
# f. Literals - any value you can see such as strings, numeric literals
# 6 How can you find more information about python functions?
# Google, Peers, experts
