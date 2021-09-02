import turtle
from random import randint
window=turtle.Screen()
turtle.bgcolor("black")
turtle.color("Yellow")
turtle.speed(-1)
def drawstar():
    turtle.begin_fill()
    turns=5
    while turns>0:
        turtle.fd(25)
        turtle.lt(145)
        turns=turns-1
    turtle.end_fill()

num_stars=0
while num_stars<50:
    x=randint(-300,300)
    y=randint(-300,300)
    drawstar()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    num_stars+=1

window.exitonclick()
