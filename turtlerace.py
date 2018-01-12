from turtle import *
from random import randint


penup()
goto(-140, 140)

for x in range(14):
    write(x, align='center')
    speed(10)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
bob = Turtle()
nurcan = Turtle()
isik = Turtle()
ada.color('red')
bob.color('blue')
nurcan.color('yellow')
isik.color('green')

ada.shape('turtle')
bob.shape('turtle')
nurcan.shape('turtle')
isik.shape('turtle')

ada.penup()
bob.penup()
nurcan.penup()
isik.penup()

ada.goto(-160, 100)
bob.goto(-160, 70)
nurcan.goto(-160, 40)
isik.goto(-160, 10)

ada.pendown()
bob.pendown()
nurcan.pendown()
isik.pendown()

for x in range(10):
    ada.right(36)
    bob.right(36)
    nurcan.right(36)
    isik.right(36)

for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    nurcan.forward(randint(1, 5))
    isik.forward(randint(1, 5))
