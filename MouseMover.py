""" 
An automagic mouse mover for your Mac, for when you definitely should just be online, working.
"""

import pyautogui as pg
import random as r
import time as t
screen_width, screen_height = pg.size()


sleep_time = float(input("How many seconds should the program wait until the mouse moves again?\n"))

runtime = float(input("How long should the program run for? Input a decimal of minutes.\n"))

t_end = t.time() + (runtime * 60)


while t.time() < t_end:
    x = r.randint(0,screen_width)
    y = r.randint(0,screen_height)
    pg.moveTo(x,y, duration=1)
    t.sleep(sleep_time)

print("Get back on your computer!")

