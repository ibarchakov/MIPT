#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    def three_in_a_row():
        count = 0
        while not wall_is_on_the_right():
            while count != 2:
                if cell_is_filled():
                    count += 1
                    move_right()
                else:
                    count = 0
                    move_right()
            else:
                if cell_is_filled():
                    break
                else:
                    three_in_a_row()


    three_in_a_row()


if __name__ == '__main__':
    run_tasks()
