import turtle
square = turtle.Turtle()
def draw(angle):
    for i in range(3):
        square.fd(100)
        square.right(90)
    square.fd(100)
    square.rt(90+angle)
step=36
angle = 360/step
for i in range (step):
    draw(angle)
turtle.done()