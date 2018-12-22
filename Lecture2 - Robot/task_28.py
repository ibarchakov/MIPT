#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    count = 0
    while count != 4:
        if cell_is_filled():
            count += 1
            move_right()
        else:
            move_right()
    else:
        while not cell_is_filled():
            move_right()


if __name__ == '__main__':
    run_tasks()
