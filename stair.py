from turtle import Turtle, left
 
 arka = Turtle()
arseniy = Turtle()
artem = Turtle()
arseniy.pencolor("red")
artem.pencolor("blue")
 
artem.speed(999)
arseniy.speed(999)
artem.left(180)
for _ in range(200):
    arseniy.forward(200)
    arseniy.left(50)
    
    artem.forward(200)
    artem.left(50)
    