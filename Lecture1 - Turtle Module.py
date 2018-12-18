import turtle
import math


def S_letter():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def square():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)


def circle():
    for _ in range(360):
        turtle.left(1)
        turtle.forward(100 * math.pi / 360)


def embedded_squares():
    for side in range(10, 110, 10):
        turtle.pendown()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.penup()
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(180)


def spider():
    n = 12
    for _ in range(n):
        turtle.forward(80)
        turtle.goto(0, 0)
        turtle.left(30)


def helix():
    n = 140
    angle = 10
    for step in range(n):
        turtle.forward(step)
        turtle.left(angle)


def squared_helix():
    n = 140
    angle = 90
    for step in range(n):
        turtle.forward(step)
        turtle.left(angle)


def embedded_polygons():
    a = 100
    for n in range(3, 13):
        angle = (180 - (360 / n))
        y = math.radians(360 / (2 * n))
        r = a / (2 * math.sin(y))
        turtle.penup()
        turtle.goto(r, 0)
        turtle.setheading(0)
        turtle.pendown()
        turtle.left(180 - angle / 2)
        for _ in range(n):
            turtle.forward(a)
            turtle.left(180 - angle)
        a += 15


def flower():
    r = 50
    angle = 60
    for i in range(6):
        turtle.left(angle)
        turtle.circle(r)


def butterfly():
    r = 30
    angle = 180
    turtle.setheading(90)
    for i in range(10):
        turtle.circle(r)
        turtle.left(angle)
        turtle.circle(r)
        turtle.left(angle)
        r += 3


def spring():
    r1 = 50
    r2 = 10
    for i in range(5):
        turtle.setheading(90)
        turtle.circle(-r1, 180)
        turtle.circle(-r2, 180)


def smile():
    r = 200
    turtle.color('black', 'yellow')
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.goto(-r / 2, 4 * r / 3)
    turtle.pendown()
    turtle.color('black', 'blue')
    turtle.begin_fill()
    turtle.circle(r / 10)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.goto(r / 2, 4 * r / 3)
    turtle.pendown()
    turtle.color('black', 'blue')
    turtle.begin_fill()
    turtle.circle(r / 10)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.goto(0, 2 * r / 3)
    turtle.left(90)
    turtle.pensize(10)
    turtle.pendown()
    turtle.forward(r / 2)
    turtle.penup()
    turtle.home()
    turtle.goto(2 * r / 3, r)
    turtle.color('red')
    turtle.setheading(90)
    turtle.pendown()
    turtle.circle(2 * r / 3, -180)


def star_5():
    a = 100
    n = 5
    angle = 36
    turtle.setheading(90)
    turtle.left(angle / 2)
    for _ in range(n):
        turtle.forward(a)
        turtle.left(180 - angle)


def star_11():
    a = 400
    n = 11
    angle = 360 / (2 * n)
    turtle.setheading(90)
    turtle.left(angle / 2)
    for _ in range(n):
        turtle.forward(a)
        turtle.left(180 - angle)


def main():
    #S_letter()
    #square()
    #circle()
    #embedded_squares()
    #spider()
    #helix()
    #squared_helix()
    #embedded_polygons()
    #flower()
    #butterfly()
    #spring()
    #smile()
    #star_5()
    star_11()


if __name__ == '__main__':
    main()
