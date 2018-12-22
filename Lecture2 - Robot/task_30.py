#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    def fill_perimeter():
        move_right()
        colored = 0
        while not wall_is_on_the_right():
            fill_cell()
            colored += 1
            move_right()
        move_down()
        while not wall_is_beneath():
            fill_cell()
            move_down()
        move_left()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        move_up()
        while not wall_is_above():
            fill_cell()
            move_up()
        return colored
    def fill_rest(count):
        move_right()
        move_down()
        move_right()
        for i in range(count - 2):
            fill_cell()
            move_right()
        move_down()
        for i in range(count - 2):
            fill_cell()
            move_down()
        move_left()
        for i in range(count - 2):
            fill_cell()
            move_left()
        move_up()
        for i in range(count - 2):
            fill_cell()
            move_up()



    count = fill_perimeter()
    while count != 1:
        fill_rest(count)
        count -= 2
    else:
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_beneath():
            move_down()

if __name__ == '__main__':
    run_tasks()
