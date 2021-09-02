import turtle
turtle.bgcolor('black')
def drawshape(turtle,r):
    turtle.circle(r,extent=60)
    turtle.lt(120)
    turtle.circle(r,extent=60)
    
def drawflower():
    p=turtle.Turtle()
    p.color('magenta')
    p.speed(0)
    p.pensize(4)
    no_of_p=15
    r=300
    for i in range(no_of_p):
        drawshape(p,r)
        p.lt(360/no_of_p)

drawflower()
turtle.done()
