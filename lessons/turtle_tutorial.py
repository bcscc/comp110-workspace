"""Learning how to draw with turtles."""

from turtle import Turtle, colormode, done
colormode(255)

side_length: float = 600

leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.penup()
leo.goto(-300, -250)
leo.pendown()
leo.color((00,00,00), (99, 204, 250))
leo.begin_fill()
i:int = 0
while i < 3:
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.hideturtle()
bob.color((255, 255, 255))
bob.penup()
bob.goto(-300, -250)
bob.pendown()
bob.speed(50)

i = 0
while i < 3:
    bob.forward(side_length)
    bob.left(120)
    i += 1

j:int = 0
while j < 120:
    side_length = side_length * 0.95
    bob.forward(side_length)
    bob.left(122)
    j += 1

done()