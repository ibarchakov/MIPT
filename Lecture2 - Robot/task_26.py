#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
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
    def back_cross():
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_down(n = 2)
        fill_cell()
        move_up()
        fill_cell()
        move_left()
        fill_cell()

    move_down()
    for _ in range(2):
        for i in range(9):
            cross()
            move_right(n = 2)
        cross()
        move_down(n = 4)
        for i in range(9):
            back_cross()
            move_left(n = 2)
        back_cross()
        move_down(n=4)
    for i in range(9):
        cross()
        move_right(n=2)
    cross()
    move_up()
    while not wall_is_on_the_left():
        move_left()

if __name__ == '__main__':
    run_tasks()
