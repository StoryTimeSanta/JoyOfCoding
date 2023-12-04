# Module 3 Question 3
# Richard Hudson

# num = eval(input("Enter a number with a decimal: "))
# print(num)

numbers = []
for num in range(1, 11):
    user_input = float(input(f'Enter number with a decimal{num} => '))
    numbers.append(user_input)

result = sum(numbers)
avg= result/10
print("The numbers entered were", numbers)
print(f'\nThe total sum of the numbers is: {result}.')
print(f'\nThe average of the numbers is: {avg}).')
