#  Richard Hudson

# What does this program output?

my_list = ["one", "two", "three", "four", "five"]

print(my_list[0])  # Will print one
print(my_list[-1])  # Will print five
print(my_list[2:4])  # Will print three, four

for num in my_list:
    if num.count("o") > 0:
        print(num)  # Will print all with an o (one two four)

phrase = "Green Eggs & Ham"
print("green" in phrase)  # False
print("Green" in phrase)  # True
print("two" in my_list)  # True

phrase = "Monty Python"
for letter in phrase:
    print(letter, end="-")  # M-o-n-t-y- -P-y-t-h-o-n-
print()

# Assume the user enters the following numbers:
# 5 10 15 20 25
numbers = []
for i in range(5):
    numbers.append(eval(input("Please enter a number: ")))
print(sum(numbers))  # Will print 75


#  In the code above, identify the following:
#  1. Loop variables: num, letter, i
#  2. List initializations: my_list =, numbers =
#  3. Function definitions: none
#  4. Function calls: print, string count, list.append, eval, input, sum
#  5. Conditions: if num.count("o") > 0:
#  6. Boolean Expressions: “green” in phrase, “Green” in phrase, “two” in my_list, num.count(“o”) > 0
#  7. String Literals: everything in ""
