# Richard Hudson
# Assignment Requirements

# 3. Create a program that allows the user to enter in a list of numbers,
# prints them out in sorted order, and prints the sum and average of
# the numbers. Prompt the user to continue entering numbers, and
# enter the number ‘0’ when finished

list1 = []
prompt = "Please enter a number ('0' to finish)"
response = eval(input(prompt))
while response != 0:
    list1.append(response)
    response = eval(input(prompt))
print(sorted(list1))
print(sum(list1))
print(sum(list1) / len(list1))
