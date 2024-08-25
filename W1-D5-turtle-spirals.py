# Turtle Spirals
# Richard Hudson

import turtle
turtle.color("red")

size = 100


# rotate = 120
# draw = turtle.forward(size)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()


# forward helper function using back
def move(len):
    back(-1 * len)


def triangle(size):
    # run 3 times
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)


def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


def polygon(num, size):
    for i in range(num):
        turtle.forward(size)
        turtle.left(360 / num)


def spiral(len, angle):
    for i in range(len, 5, -5):
        turtle.forward(i)
        turtle.right(angle)


spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)

# polygons draw
# for n in range (3, 10):
#  move(50) #forward
#  polygon(n, 100 / n)
#  back(50)
#  turtle.right(360 / 7)

# turtle.color("red")
# polygon(3, 100)
# square(100)
# triangle(100)
# triangle(50)
# triangle(25)
# back(75)
# turtle.color("orange")
# polygon(4, 50)
# square(50)
# triangle(50)
# back(50)
# turtle.color("green")
# polygon(9, 50)
# triangle(25)

turtle.Screen().exitonclick()
# turtle.done()