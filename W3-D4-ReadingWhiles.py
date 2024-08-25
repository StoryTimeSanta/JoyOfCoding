# JOC D4 While Loops
# Richard Hudson

#a.
j = 4
while j > -4:
    print (j)
    j -= 1

# this will print 4 and each number to -3

#b.
string = "Hello"
builder = ""
i = 0
while i < len(string):
    builder += string[i].swapcase()
    print (i, builder)
    i += 1
print (string, "->", builder)

#this code will print the line number i and each letter of the string alternating the case of the letters.
