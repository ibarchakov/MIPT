#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    j = 13
    while j > 1:
        for i in range(j):
            move_right()
            move_down()
            fill_cell()
        move_down()
        for i in range(j - 1):
            move_left()
            move_up()
            fill_cell()
        move_left()
        j -= 2
    else:
        move_right()
        move_down()
        fill_cell()
        move_down()


if __name__ == '__main__':
    run_tasks()
