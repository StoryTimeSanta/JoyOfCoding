#  Writing List
#   Richard Hudson
#   1 Write a program that creates a list of 20 numbers input by the user and prints the average (mean) of the list.

# numbers = []
# for i in range(4):  # change value to total numbers to be entered
#     numbers.append(eval(input("Please enter a number: ")))
# avg = sum(numbers) / len(numbers)  # calculate average from user input divided by the range value
# print("You entered:", numbers)
# print("The average is:", avg)
# print()

#   2 Write a function mangle that takes a string as a parameter and returns the string after performing
#       the following operations:
#   i. Converting the string to all upper case letters
#   ii. Removing the third character
#   iii. Removing the third to last character
#  Example Calls:
#  print(mangle(“hellothere”)) HELOTHRE
#  print(mangle(“42 degrees Celsius”)) 42DEGREES CELSUS
#  print(mangle(“eeeeeee”)) EEEEE


def mangle(string):
    # Convert the string to all upper case letters
    uppercase_string = string.upper()

    # Remove the third character
    no_third_char = uppercase_string[:2] + uppercase_string[3:]

    # Remove the third to last character
    without_third_to_last_char = no_third_char[:-3] + no_third_char[-2:]

    return without_third_to_last_char


# Example usage:
print(mangle("hellothere"))
print(mangle("42 degrees Celsius"))
print(mangle("eeeeeee"))


def main():
    print(mangle("hellothere"))
    input_test = ["hellothere", "42 degrees Celsius", "eeeeeee"]
    output_test = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
    for test in range(len(input_test)):
        #  result = mangle(input_test)
        print("Mangle", input_test[test] + ":", mangle(input_test[test]) == output_test[test])
    print()


main()


# 3. Write a function, count_e, that takes a list of strings as a parameter and
# returns the total number of upper and lower case e’s (“E” and “e”) in all the
# strings in the list. Test that your function works with multiple examples.
# Example function call: Output:
# print(count_e([“hi”, “hello”, “EEK!”])) 3


def count_e(string_list):
    total = 0
    for string in string_list:
        total += string.lower().count('e')
    return total


example = ["hi", "hello", "EEK!"]
result = count_e(example)
print(f"The total count of 'E' and 'e' is: {result}")
print()


# 4. Write a function, count_vowels, that takes a list of strings as a parameter
# and returns the total number of upper and lower case vowels (A, E, I, O, U) in all
# the strings in the list.
# Example function call: Output:
# print(count_vowels([“hi”, “hello”, “OOF!”])) 5


def count_vowels(string_list):
    vowels = "AEIOUaeiou"
    total = 0
    for string in string_list:
        total += sum(1 for char in string if char in vowels)
    return total


example_strings = ["hi", "hello", "OOF!"]
result = count_vowels(example_strings)
print(f"The total count of vowels is: {result}")
