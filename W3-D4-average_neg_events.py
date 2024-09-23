#Richard Hudson
#Assignment Requirements
# Write a function average_neg_evens that takes a list of numbers as a
# parameter, and adds all the negative even numbers (less than 0 and
# divisible by 2) together and returns their average.
# Example function call:
# print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
# Outputs: -3

def average_neg_evens(list):
        # define aggregator variables to calc average
        sum = 0
        count = 0

        for num in list:
                if num < 0 and num % 2 == 0:
                        sum += num
                        count += 1

        return sum / count # avg = sum / count

# Example function call:
# list = [“HELLO”, “goodbye”, “1234 Oooh!”]
# print(count_letter(list, “o”))
# Outputs: 6

def count_letter(list,letter):
        count = 0
        letter = letter.lower()

        for string in list:
                count += string.lower().count(letter)

        return count # number of times letter occurs, both upper- & lower-cased.

def main():
        print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4])) #-3
        list = ["HELLO", "goodbye", "1234 Oooh!"]
        print(count_letter(list, "o")) # 6

main()