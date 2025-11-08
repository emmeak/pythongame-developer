import random
import pgzrun
TITLE = "ATTACK the little alien!"
WIDTH = 605
HIGHT = 506
littlealien = Actor("littlealien")
littlealien.pos = 390,231

def draw():
    screen.clear()
    screen.fill("dark blue")
    littlealien.draw()

pgzrun.go()