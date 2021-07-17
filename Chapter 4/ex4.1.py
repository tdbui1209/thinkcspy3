import turtle


def draw_square(t, sz):
    for _ in range(4):
        t.forward(sz)
        t.right(90)

screen = turtle.Screen()
screen.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

# Move pen to start point (-300, 0)
# penup() to avoid draw line from (0, 0) to (-300, 0)
tess.penup()
tess.goto(-300, 0)
tess.pendown()

for _ in range(5):
    draw_square(tess, 50)
    tess.penup()
    tess.forward(100)
    tess.pendown()
