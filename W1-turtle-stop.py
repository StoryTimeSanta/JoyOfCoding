# Portfolio Project Turtle
# Richard Hudson

import turtle
turtle.width(width=None)
turtle.pensize(width=5)
turtle.color("red")
size = 80
len1 = .25  # width of rectangle
len2 = 2  # height of rectangle


turtle.shape("turtle")  # optional
turtle.speed(0)  # optional


def octagon(size):
    for i in range(8):
        turtle.forward(size)
        turtle.left(45)


def rectangle(len1, len2):
    for i in range(2):
        turtle.forward(len1)
        turtle.right(90)
        turtle.forward(len2)
        turtle.right(90)


def stop(size):
    turtle.penup()
    turtle.forward(size * .5)
    turtle.pendown()
    octagon(size)
    turtle.forward(size * .375)
    rectangle(size * len1, size * len2)


stop(size)
turtle.penup()
turtle.forward(150)
turtle.pendown()
turtle.color("green")
stop(size / 2)

turtle.Screen().exitonclick()
# turtle.done()
