import turtle
from turtle import *

move = turtle.Turtle()
follow = turtle.Turtle()

setup(600 , 600)
Screen()
title("Turtle Keys")

def k1():
   move.forward(50)
   a = move.getangle()
   follow.goto(move.xcor, move.ycor)
   follow.setheading(a)
   follow.back(10)

def k2():
   move.left(50)
   a = move.getangle()
   follow.goto(move.xcor, move.ycor)
   follow.setheading(a)
   follow.back(10)
   
def k3():
   move.right(50)
   a = move.getangle()
   follow.goto(move.xcor, move.ycor)
   follow.setheading(a)
   follow.back(10)
   
def k4():
   move.back(50)
   a = move.getangle()
   follow.goto(move.xcor, move.ycor)
   follow.setheading(a)
   follow.back(10)

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

