# Turtle Triangles
# Richard Hudson

import turtle

#def tred = turtle.color("red")
#def tgreen = turtle.color("green")
#def torange = turtle.color("orange")

#size = 100
#rotate = 120
#draw = turtle.forward(size)

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)

#(tred)
turtle.color("red")
triangle(100)
back(75)
#(torange)
turtle.color("orange")
triangle(50)
back(50)
#(tgreen)
turtle.color("green")
triangle(25)

turtle.Screen().exitonclick()
# turtle.done()