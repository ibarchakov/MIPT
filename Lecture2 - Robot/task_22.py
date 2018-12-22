#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    def fill_right():
        while wall_is_on_the_right() is False:
            fill_cell()
            move_right()
        fill_cell()
        if wall_is_beneath():
            exit()
        else:
            move_down()
    def fill_left():
        while wall_is_on_the_left() is False:
            fill_cell()
            move_left()
        fill_cell()
        if wall_is_beneath():
            exit()
        else:
            move_down()
    def exit():
        while wall_is_on_the_left() is False:
            move_left()
    while cell_is_filled() is False:
        fill_right()
        fill_left()

if __name__ == '__main__':
    run_tasks()
