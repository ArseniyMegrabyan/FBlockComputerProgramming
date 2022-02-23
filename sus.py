
from pickle import TRUE
from re import A
from turtle import Turtle, penup, reset, speed
carpoints = (
    (4,0),
    (2,2),
    (1,4),
    (1,8),
    (0,8),
    (0.10),
    (1,10),
    (1,18),
    (0,18),
    (0,20),
    (1,20),
    (1,24),
    (2,26),
    (4,28),
    (7,28),
    (9,26),
    (10,24),
    (10,20),
    (11,20),
    (11,18),
    (10,18),
    (10,10),
    (11,10),
    (11,8),
    (10,8),
    (10,4),
    (9,2),
    (7.0)
)
height = 500
width = 700
distance = 10

ben = Turtle()
screen = ben.getscreen()
screen.register_shape("car", (
    (4,0),
    (2,2),
    (1,4),
    (1,8),
    (0,8),
    (0,10),
    (1,10),
    (1,18),
    (0,18),
    (0,20),
    (1,20),
    (1,24),
    (2,26),
    (4,28),
    (7,28),
    (9,26),
    (10,24),
    (10,20),
    (11,20),
    (11,18),
    (10,18),
    (10,10),
    (11,10),
    (11,8),
    (10,8),
    (10,4),
    (9,2),
    (7,0)
))
ben.shape("car")
ben.color("black", "blue")

timer = Turtle()
timer.hideturtle()
timer.penup()
timer.left(90)
timer.forward(300)

speed = 0
angle = 10
update = 0.2

screen.bgpic("nn2.gif")

def accelerate():
    global speed
    speed = speed + update

def decelerate():
    global speed
    speed = speed - update

def moveleft():
    ben.left(angle)

def moveright():
    ben.right(angle)


def stop():
    global speed
    speed = 0
    
 
def reset():
    global time, speed
    time = 0
    ben.pu()
    ben.goto(-265, 0)
    ben.setheading(90)
    ben.pd()
    speed = 0

screen.listen()
screen.onkeypress(accelerate, "w")
screen.onkeypress(decelerate, "s")
screen.onkeypress(moveright,"d")
screen.onkeypress(moveleft,"a")
screen.onkeypress(stop, "space")
screen.onkeypress(accelerate,"Up")
screen.onkeypress(decelerate, "Down")
screen.onkeypress(moveright,"Right")
screen.onkeypress(moveleft,"Left")
screen.onkeypress(reset,"q")


ben.pu()
ben.goto(-265, 0)
ben.left(90)
ben.pd()
time = 0
scoring = False

while True:

    allowedforward = True

    if ben.ycor() < -height and ben.heading == 180:
        allowedforward = False

    ben.forward(speed)

    



    if scoring: 
        time += 0.1
        timer.clear()
        timer.write(f"{time:02.2f}", False, "center", ("Arial", 30, "bold"))
    if abs(ben.xcor() - (-265)) < 10 and ben.ycor() > 0:
        if time < 10:
            scoring = True
        else:
            scoring = False
    if allowedforward == TRUE:
        ben.forward(distance)

    screen.update()