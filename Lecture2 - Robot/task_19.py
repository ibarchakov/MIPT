#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    def check():
        if wall_is_above() == False:
            return True
    def search_left():
        while wall_is_on_the_left() == False :
            move_left()
    def search_right():
        while wall_is_on_the_right() == False:
            move_right()
    def exit():
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()
    search_left()
    if check():
        exit()
    else:
        search_right()
        if check():
            exit()
        else:
            pass

if __name__ == '__main__':
    run_tasks()
