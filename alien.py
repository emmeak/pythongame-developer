import random
import pgzrun
TITLE = "ATTACK the little alien!"
WIDTH = 605
HEIGHT = 506
littlealien = Actor("littlealien")
littlealien.pos = 390,231

message = ""

def draw():
    screen.clear()
    screen.fill("dark blue")
    littlealien.draw()
    screen.draw.text(message, center = (477,12), fontname = "gabriola.ttf", fontsize = 29)

def on_mouse_down(pos):
    global message
    if littlealien.collidepoint(pos):
        littlealien.x = random.randint(50,550)
        littlealien.y = random.randint(40,440)
        message = "Winners get 2125!"
    else:
        message = "Losers get 4963..."
pgzrun.go()