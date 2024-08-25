# Portfolio Project Turtle
# Richard Hudson

import turtle
turtle.width(width=None)
turtle.pensize(width=5)
turtle.color("red")

size = 90
deg = 90

turtle.shape("turtle") # optional
turtle.speed(0) # optional

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

def square(size):
  for i in range(4):
    turtle.forward(size)
    turtle.right(deg)

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)

def house(size):
  square(size)
  triangle(size)

#square(90)
#triangle(90)
house(90)
turtle.penup()
turtle.forward(180)
turtle.pendown()
turtle.color("green")
house(45)

turtle.Screen().exitonclick()
# turtle.done()
