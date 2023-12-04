# What does this program output when it's ...
# 1. Monday?
# 2. Saturday?
# 3. Sunday?
# 4. Raining?

# Write what each line should print next to the code above for the 4
# example inputs on lines 2—5. Consult with a peer before running the
# example if possible. Were your hypotheses correct? Why or why not?

# saturday - Wake up at 7 am
# sunday - Wake up at 7 am
# satURday - Wake up at 7 am
# SunDAY - Wake up at 7 am

DoW = input("What day is it?").title()
# DoWT = DoW.title() # This line is the fix for title method
# DoW = "Monday"

if DoW == "Saturday":
    print("Wake up at 9 am")
elif DoW == "Sunday":
    print("Wake up at 10 am")
else:
    print("Wake up at 7 am")

