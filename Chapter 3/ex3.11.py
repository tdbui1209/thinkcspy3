import turtle

screen = turtle.Screen()
screen.bgcolor('lightgreen')
tess = turtle.Turtle()

tess.pensize(5)
tess.color('blue')
tess.hideturtle()
tess.speed(10)

# turtle forward 100, and draw small line with length = 10
# then back to (0, 0) position.
for _ in range(12):
    tess.penup()            # penup() to avoid draw a line forward 100
    tess.forward(100)
    tess.pendown()          # pendown() to draw small line
    tess.forward(10)
    tess.penup()            # penup() to avoid draw line back to (0, 0) position
    tess.goto(0, 0)
    tess.right(360/12)

# turtle forward 130, and stamp turtle
# then back to (0, 0) position.
tess.shape('turtle')
tess.showturtle()
for _ in range(12):
    tess.forward(130)
    tess.stamp()
    tess.goto(0, 0)
    tess.right(360/12)
