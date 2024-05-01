import turtle

turtle.Turtle()
from turtle import *
setup(600 , 600)
Screen()
title("Turtle Keys")
turtle.pencolor("red")
move = Turtle()
showturtle()
c_turtle = turtle.Turtle()
   




def k1():
    c_turtle.shape('circle')
    turtle.color("red")
    move.forward(45)

def k2():
    c_turtle.shape('circle')
    turtle.color("red")
    move.left(45)

def k3():
    c_turtle.shape('circle')
    turtle.color("red")
    move.right(45)

def k4():
    c_turtle.shape('circle')
    turtle.color("red")
    move.back(45)

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()
if turtle.xcor() > 290 or turtle.xcor() < -290 or turtle.ycor() > 290 or turtle.ycor() < -290:
        time.sleep(1)
        turtle.goto(0, 0)
        turtle.direction = "stop"

