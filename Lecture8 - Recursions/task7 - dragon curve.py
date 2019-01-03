import turtle


def dragon_curve(length, n):
    def x(n):
        if n == 0:
            return
        x(n - 1)
        turtle.right(90)
        y(n - 1)
        turtle.forward(length)

    def y(n):
        if n == 0:
            return
        turtle.forward(length)
        x(n - 1)
        turtle.left(90)
        y(n - 1)
    turtle.forward(length)
    x(n)


if __name__ == '__main__':
    dragon_curve(30, 10)
