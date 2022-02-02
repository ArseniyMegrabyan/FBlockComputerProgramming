from platform import architecture
from turtle import Turtle, forward, left
 
arka = Turtle()
arseniy = Turtle()
artem = Turtle()
arseniy.pencolor("red")
artem.pencolor("blue")
arka.pencolor("green")



artem.left(180)
artem.forward(50)
artem.right(90)
artem.forward(50)
artem.left(90)
artem.forward(50)
artem.right(90)
artem.forward(50)
artem.left(90)
artem.forward(50)
artem.right(90)
artem.forward(100)

arseniy.forward(50)
arseniy.left(90)
arseniy.forward(50)
arseniy.right(90)
arseniy.forward(50)
arseniy.left(90)
arseniy.forward(50)
arseniy.right(90)
arseniy.forward(50)
arseniy.left(90)
arseniy.forward(100)


s = arseniy.getscreen()
s.mainloop()
    