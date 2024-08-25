#  Basic While
#  Richard Hudson

# 1. What is output by the following programs?
# a.
# j=4
# while j > -4:
#          print(j)
#          j -= 1
# Output: 4 through -3
#
# b.
# string = "Hello"
# builder = ""
# i=0
# while i < len(string):
#     builder += string[i].swapcase()
#     print(i, builder)
#     i += 1
# print(string, "->", builder)
# print the value of i (0 through 4)
# then print the characters of the string swapping case for characters in string to the value of i
# finally print string -> builder or Hello -> hELLO
# c.
# x=0
# i=1
# while x < 20:
#     if x > 5:
#         x += 15
#     else:
#         x += 1
#     print(i, x)
#     i += 1
# print i, x while x < 20 values of i (1 2 3 4 5 6 7) values of x (1 2 3 4 5 6 21)
# Learning Exercise: Combining While
# 2. What is output by the following programs? a.
# string = “HELLO”
# x=0
# while string[x] != ‘L’:
# print(string[x], end=”...
#          x += 1
#       print(“\n”, string, “first L
# “)
# is at”, x)
# # Assume the user enters the
# # hello goodbye cat dog DONE done
# list = []
# prompt = “Please enter word,
# response = input(prompt)
# while response != “done”:
#     list.append(response)
#     response = input(prompt)
# print(sorted(list))
# x=0
# while x < 20:
#   if x > 5:
#     if x % 2 == 0:
# x *= 2 else:
# x *= -1 else:
# x += 10 x += 1
# print(x)