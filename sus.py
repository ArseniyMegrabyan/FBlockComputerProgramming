
from turtle import Turtle, speed


ben = Turtle()
screen = ben.getscreen()
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



ben.pu()
ben.goto(-265, 0)
ben.left(90)
ben.pd()


while True:
    ben.forward(speed)
    screen.update()