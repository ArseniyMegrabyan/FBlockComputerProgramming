
from turtle import Turtle, speed


ben = Turtle()
racetrack = Turtle()
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

def startdrawing(x, y):
    racetrack.goto(x,y)
    racetrack.pendown()


def stop():
    global speed
    speed = 0
    






screen.listen()
screen.onkeypress(accelerate, "w")
screen.onkeypress(decelerate, "s")
screen.onkeypress(moveright,"d")
screen.onkeypress(moveleft,"a")
screen.onkeypress(stop, "space")
racetrack.onclick(startdrawing)
racetrack.ondrag(racetrack.goto)
racetrack.onrelease(racetrack.penup)

# ##Draw racetrack
# racetrack.forward()

while True:
    ben.forward(speed)
    screen.update()