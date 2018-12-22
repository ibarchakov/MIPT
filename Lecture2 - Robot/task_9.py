#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    for i in range(28):
        if wall_is_above() == False and wall_is_on_the_right() == False:
            fill_cell()
            move_right()
        if wall_is_above() == True and wall_is_on_the_right() == False:
            move_right()
        if wall_is_above() == False and wall_is_on_the_right() == True:
            fill_cell()
        if wall_is_above() == True and wall_is_on_the_right() == True:
            pass


if __name__ == '__main__':
    run_tasks()
