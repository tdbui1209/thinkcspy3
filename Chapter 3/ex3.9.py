# tips: same like exercise 3.6

import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

sides = 18 # sides of polygon

for _ in range(sides):
    tess.forward(50)
    tess.right(360/sides)
