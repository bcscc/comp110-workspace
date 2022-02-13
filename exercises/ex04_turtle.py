"""EX04 - A beautifully artistic scene painted using turtle.

0. Drawing Functions: lines 35-78
1. Main: lines 218-219
2. Draw something twice: 148-153
3. Loop usage: lines 81-94 or lines 105-123
4. Fill color: lines 126-145
5. Marker color: line 83
6. Types, Linting, Documentation: lines 1-12
7. Break up complex functions: lines 126-145 or lines 156-215
8. Try something fun!: lines 24-25, 105-123
"""

from turtle import Turtle, colormode, done
from random import randint

colormode(255)

leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.penup()

"""Randomly assigns the time_of_day to either day (0) or night (1)."""
time_of_day: int = randint(0, 1) 


def main() -> None:
    """The start of painting."""
    paint_background(leo)
    paint_forest(leo)
    paint_cabin(leo)


def draw_line(a_turtle: Turtle, x1: float, y1: float, x2: float, y2: float) -> None:
    """Component function that draws a line from one coordinate to another."""
    a_turtle.goto(x1, y1)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.goto(x2, y2)
    a_turtle.penup()


def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, height: float) -> None:
    """Component function that draws any size rectangle at a given coordinate."""
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    i: int = 0
    while i < 2:
        a_turtle.pendown()
        a_turtle.forward(length)
        a_turtle.right(90)
        a_turtle.forward(height)
        a_turtle.right(90)
        i += 1
    a_turtle.penup()


def draw_circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Component function that draws any size circle at a given coordinate."""
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.circle(radius)
    a_turtle.penup()


def draw_triangle(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Component function that draws any equilateral triangle at a given coordinate."""
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    i: int = 0
    while i < 3:
        a_turtle.pendown()
        a_turtle.forward(length)
        a_turtle.left(120)
        i += 1
    a_turtle.penup()


def paint_tree(a_turtle: Turtle, x: float, y: float) -> None:
    """Helper function that draws a tree at a given coordinate."""
    a_turtle.color((78, 53, 36), (83, 53, 10))
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, x + 55, y, 90, 70)
    a_turtle.end_fill()
    i: int = 0
    while i < 3:
        a_turtle.color((66, 105, 47), (114, 183, 52))
        a_turtle.begin_fill()
        draw_triangle(leo, x, y, 200)
        a_turtle.end_fill()
        y += 80
        i += 1


def paint_sun(a_turtle: Turtle) -> None:
    """Helper function that paints the sun."""
    a_turtle.color((243, 130, 53), (253, 216, 53))
    a_turtle.begin_fill()
    draw_circle(a_turtle, -325, 255, 50)
    a_turtle.end_fill()


def paint_sky(a_turtle: Turtle) -> None:
    """Helper function that paints the clouds or stars, depending on the time_of_day."""
    i: int = 0
    a_turtle.color((255, 255, 255), (255, 255, 255))
    if time_of_day == 0:
        clouds: int = randint(0, 8)
        while i < clouds:
            a_turtle.begin_fill()
            draw_rectangle(a_turtle, randint(-360, 390), randint(150, 340), randint(60, 100), randint(20, 40))
            a_turtle.end_fill()
            i += 1
    else:
        stars: int = randint(0, 12)
        while i < stars:
            star_size: int = randint(3, 8)
            a_turtle.begin_fill()
            draw_rectangle(a_turtle, randint(-360, 390), randint(150, 340), star_size, star_size)
            a_turtle.end_fill()
            i += 1


def paint_background(a_turtle: Turtle) -> None:
    """Set function thats paints the sky day or night, depending on the time_of_day."""
    if time_of_day == 0:      
        a_turtle.color((39, 193, 241), (39, 193, 241))
        a_turtle.begin_fill()
        draw_rectangle(a_turtle, -360, 340, 750, 670)
        a_turtle.end_fill()
        paint_sky(a_turtle)
        paint_sun(a_turtle)
    else:
        a_turtle.color((0, 0, 0), (0, 0, 0))
        a_turtle.begin_fill()
        draw_rectangle(a_turtle, -360, 340, 750, 670)
        a_turtle.end_fill()
        paint_sky(a_turtle)
    """Paints the ground."""
    a_turtle.color((52, 105, 85), (111, 165, 63))
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, -360, -120, 750, 210)
    a_turtle.end_fill()


def paint_forest(a_turtle: Turtle) -> None:
    """Set function that paints the tree line."""
    paint_tree(a_turtle, 0, -75)
    paint_tree(a_turtle, -180, -85)
    paint_tree(a_turtle, 175, -105)
    paint_tree(a_turtle, -360, -105)


def paint_cabin(a_turtle: Turtle) -> None:
    """Set function that paints the cabin."""
    """Paints the cabin body."""
    a_turtle.color((0, 0, 0), (89, 55, 11))
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, -120, -40, 250, 200)
    a_turtle.end_fill()
    a_turtle.color((89, 55, 11), (89, 55, 11))
    a_turtle.begin_fill()
    draw_line(a_turtle, -120, -40, 130, -40)
    draw_line(a_turtle, 130, -40, 5, 80)
    draw_line(a_turtle, 5, 80, -120, -40)
    a_turtle.end_fill()

    """Paints the chimney."""
    a_turtle.color((0, 0, 0), (88, 88, 88))
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, -93, 90, 30, 70)
    a_turtle.end_fill()

    """Paints the roof."""
    a_turtle.color((0, 0, 0), (66, 41, 7))
    a_turtle.begin_fill()
    draw_line(a_turtle, -120, -40, 5, 80)
    draw_line(a_turtle, 5, 80, 130, -40)
    draw_line(a_turtle, 130, -40, 170, -40)
    draw_line(a_turtle, 170, -40, 5, 115)
    draw_line(a_turtle, 5, 115, -160, -40)
    draw_line(a_turtle, -160, -40, -120, -40)
    a_turtle.end_fill()

    """Paints the window."""
    a_turtle.goto(5, -25)
    a_turtle.color((0, 0, 0), (66, 41, 7))
    a_turtle.begin_fill()
    draw_circle(a_turtle, 5, -25, 35)
    draw_circle(a_turtle, 5, -20, 30)
    a_turtle.end_fill()
    a_turtle.color((0, 0, 0), (117, 72, 12))
    a_turtle.begin_fill()
    draw_circle(a_turtle, 5, -20, 30)
    a_turtle.end_fill()
    draw_line(a_turtle, 5, -20, 5, 40)
    draw_line(a_turtle, -25, 10, 35, 10)

    """Paints the door."""
    a_turtle.goto(-35, -90)
    a_turtle.color((0, 0, 0), (66, 41, 7))
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, -35, -90, 80, 150)
    draw_rectangle(a_turtle, -45, -80, 100, 160)
    a_turtle.end_fill()
    a_turtle.color((0, 0, 0), (117, 72, 12))
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, -35, -90, 80, 150)
    a_turtle.end_fill()
    a_turtle.color((0, 0, 0), (66, 41, 7))
    a_turtle.begin_fill()
    draw_circle(a_turtle, 35, -170, 5)
    a_turtle.end_fill()


if __name__ == "__main__":
    main()

done()