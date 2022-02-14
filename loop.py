from turtle import *

pencolor("red")

def sawtooth( distance, angle):
    forward(distance)
    left(angle)
    forward(distance)




# for x in range(9):
#  forward(50)
#  left(100)
#  forward(50)
 
#  right(60)
#  forward(50)

# pencolor("blue")
# for x in range(2):
#  forward(300)
#  right(90)
#  forward(300)

#  right(90)
#  forward(300)

# pencolor("green")
# for x in range(10):
#  forward(15)
#  pencolor("orange")
#  forward(15)
#  pencolor("purple")
# right(90)

for x in range (50):
    sawtooth(50, 160)
    sawtooth(50, 160)

done()
