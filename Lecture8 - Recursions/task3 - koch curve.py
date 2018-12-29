import turtle


def koch_curve(length, n):
    side = length / 3
    if n == 1:
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.right(120)
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
    else:
        for i in range(1):
            koch_curve(length / 3, n - 1)
            turtle.left(60)
            koch_curve(length / 3, n - 1)
            turtle.right(120)
            koch_curve(length / 3, n - 1)
            turtle.left(60)
            koch_curve(length / 3, n - 1)


if __name__ == '__main__':
    koch_curve(1500, 5)