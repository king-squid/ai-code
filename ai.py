import random
print(random.randrange(1, 10))
import turtle

turtle.screensize(canvwidth=350, canvheight=350,) 
                  



t = turtle.Turtle()
t.gotox(random.randrange(1, 10))

    
if turtle.xcor() >= 350:
    turtle.setx(324)
elif turtle.xcor() >= 350:
    turtle.setx(-324)
elif turtle.ycor() >= 350:
    turtle.sety(324)
elif turtle.ycor() >= -350:
    turtle.sety(-324)
