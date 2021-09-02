import turtle
import random
trt=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor('black')
trt.color('red','yellow')
trt.pensize(2)
trt.speed(0)
def flower(n=80):
    import random
    sz=random.randrange(200,600)
    trt.begin_fill()
    for i in range (n):
        trt.fd(sz)
        trt.lt(168.5)
        trt.fd(sz)
    trt.end_fill()


flower()

