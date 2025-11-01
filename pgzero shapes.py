import pgzrun
from random import randint
WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill("white")
    screen.draw.circle((250,250), 68, "dark green")
    screen.draw.line((0,0),(500,500), "dark red")
    screen.draw.text("chicken noodle soup", (100,200), fontname = "frscript", fontsize = 45, color = "orange")
    w = 500
    h = 150
    for i in range(10):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        shape = Rect((0,0),(w,h))
        shape.center = (250,250)
        screen.draw.rect(shape, (r, g, b))
        w -= 10
        h += 10

pgzrun.go()