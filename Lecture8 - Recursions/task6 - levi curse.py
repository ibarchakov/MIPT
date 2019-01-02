import turtle


def levi_curve(length, n):
    if n == 1:
        turtle.left(45)
        turtle.forward(((length ** 2) / 2) ** 0.5)
        turtle.right(90)
        turtle.forward(((length ** 2) / 2) ** 0.5)
    else:
        turtle.left(45)
        levi_curve(((length ** 2) / 2) ** 0.5, n - 1)
        turtle.right(45)
        levi_curve(((length ** 2) / 2) ** 0.5, n - 1)
        turtle.left(45)


if __name__ == '__main__':
    levi_curve(300, 10)