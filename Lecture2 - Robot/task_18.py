#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    def search_left():
        while wall_is_on_the_left() == False:
            move_left()
            check()
            if check():
                exit()
                return True
    def search_right():
        while wall_is_on_the_right() == False:
            move_right()
            check()
            if check():
                exit()
                return True
    def check():
        if wall_is_above() == False:
            return True
    def exit():
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()

    if check():
        exit()
    else:
        if search_left():
            pass
        else:
            search_right()


if __name__ == '__main__':
    run_tasks()
