import turtle

screen = turtle.Screen()
tess = turtle.Turtle()
for sides in [3, 4, 6, 8]:
    for side in range(sides):
        tess.forward(100)       # length of all sides
        tess.right(360/sides)    # angles must be same
