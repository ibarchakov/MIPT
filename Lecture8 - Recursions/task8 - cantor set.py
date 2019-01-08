import turtle


def cantor_set(x, y, height, length, level, depth):
    if level == 1:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fd(length)
        cantor_set(x, y - height, height, length / 3, level + 1, depth)
        cantor_set(x + length * 2 / 3, y - height, height, length / 3, level + 1, depth)
    elif level < depth:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fd(length)
        cantor_set(x, y - height, height, length / 3, level + 1, depth)
        cantor_set(x + length * 2 / 3, y - height, height, length / 3, level + 1, depth)
    elif level == depth:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fd(length)
        turtle.penup()
        turtle.goto(x + length / 3, y)
        turtle.pendown()
        turtle.fd(length)
        return
    return


if __name__ == '__main__':
    cantor_set(-150, 0, 20, 300, 1, 5)
