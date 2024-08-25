# Turtle Triangle
# Richard Hudson

import turtle

turtle.color("red")

size = 100
rotate120 = 120

draw = turtle.forward(size)
# (draw)

# draw = turtle.forward(size)
for i in range(3):
    turtle.forward(size)
    turtle.left(rotate120)

turtle.left(rotate120)
turtle.forward(size)
turtle.left(rotate120)
turtle.forward(size)
turtle.left(rotate120)


turtle.Screen().exitonclick()
# turtle.done()
