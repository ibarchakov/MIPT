#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_30():
    def exit():
        while not wall_is_on_the_left():
            move_left()
    def find_way():
        boom = 0
        if not wall_is_beneath():
            move_down()
        else:
            while not wall_is_on_the_left():
                if not wall_is_beneath():
                    move_down()
                    boom = 0
                else:
                    move_left()
            else:
                boom += 1
                while not wall_is_on_the_right():
                    if not wall_is_beneath():
                        move_down()
                        boom = 0
                    else:
                        move_right()
                else:
                    boom += 1
        return boom

    boom = 0
    while boom < 2:
        boom = find_way()
    else:
        exit()

if __name__ == '__main__':
    run_tasks()
