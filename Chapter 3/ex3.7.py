import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()

for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.stamp()
    pirate.right(angle) # positive angles are counter-clokwise, so use right()
    pirate.forward(100)
    
