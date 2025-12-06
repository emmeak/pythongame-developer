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
        sounds.eep.play()
        message = "Winners get 2125!"
    else:
        message = "Losers get 4963..."

def update():
    littlealien.x += 9
    if littlealien.x > 605:
        littlealien.x = 0
        littlealien.y = random.randint(60, 470)
pgzrun.go()