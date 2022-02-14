
from turtle import Turtle


ben = Turtle()
racetrack = Turtle()
screen = ben.getscreen()
distance = 0
angle = 10
update = 0.2

def accelerate():
    global distance
    distance+=update

def decelerate():
    global distance
    distance-=update

def moveleft():
    ben.left(angle)

def moveright():
    ben.right(angle)

def startdrawing(x, y):
    racetrack.goto(x,y)
    racetrack.pendown()


screen.listen()
screen.onkeypress(accelerate, "w")
screen.onkeypress(decelerate, "s")
screen.onkeypress(moveright,"d")
screen.onkeypress(moveleft,"a")
racetrack.onclick(startdrawing)
racetrack.ondrag(racetrack.goto)
racetrack.onrelease(racetrack.penup)

# ##Draw racetrack
# racetrack.forward()

while True:
    ben.forward(distance)
    screen.update()