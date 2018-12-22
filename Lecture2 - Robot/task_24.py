#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right(n = 2)
    for i in range(3):
        move_down()
        fill_cell()
    move_right(n = 2)
    move_up()
    for i in range(3):
        move_left()
        fill_cell()
    move_up()

if __name__ == '__main__':
    run_tasks()
