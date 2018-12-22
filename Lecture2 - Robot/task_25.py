#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    def cross():
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_down(n = 2)
        fill_cell()
        move_up()
        fill_cell()
        move_right()
        fill_cell()


    move_down(n = 2)
    for i in range(4):
        cross()
        move_right(n = 2)
    cross()
    move_up()
    move_left(n = 2)


if __name__ == '__main__':
    run_tasks()
