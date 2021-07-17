import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.hideturtle() # hide turtle
pen.pensize(3)   # change line width

for i in range(5):
    pen.forward(200)
    pen.right(144) # each angle of star shape is 144 degree.
