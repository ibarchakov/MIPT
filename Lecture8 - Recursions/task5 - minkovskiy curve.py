import turtle


def minkovskiy_curve(length, n):
    if n == 0:
        turtle.forward(length)
        return
    if n == 1:
        turtle.forward(length / 4)
        turtle.left(90)
        turtle.forward(length / 4)
        turtle.right(90)
        turtle.forward(length / 4)
        turtle.right(90)
        turtle.forward(length / 4)
        turtle.forward(length / 4)
        turtle.left(90)
        turtle.forward(length / 4)
        turtle.left(90)
        turtle.forward(length / 4)
        turtle.right(90)
        turtle.forward(length / 4)
    else:
        minkovskiy_curve(length / 4, n - 1)
        turtle.left(90)
        minkovskiy_curve(length / 4, n - 1)
        turtle.right(90)
        minkovskiy_curve(length / 4, n - 1)
        turtle.right(90)
        minkovskiy_curve(length / 4, n - 1)
        minkovskiy_curve(length / 4, n - 1)
        turtle.left(90)
        minkovskiy_curve(length / 4, n - 1)
        turtle.left(90)
        minkovskiy_curve(length / 4, n - 1)
        turtle.right(90)
        minkovskiy_curve(length / 4, n - 1)


if __name__ == '__main__':
    minkovskiy_curve(800, 3)