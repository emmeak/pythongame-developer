import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 600

satellite = []
for i in range(12):
    bbs = Actor("babysatellite")
    bbs.pos = random.randint(50, 750), random.randint(50, 550)
    satellite.append(bbs)

starttime = 0
totaltime = 0
next_sat = 0
total_sat = 12

def draw():
    screen.blit("thebigspace", (0,0))
    bbsn = 1
    for i in satellite:
        i.draw()
        screen.draw.text(str(bbsn), (i.pos[0], i.pos[1] + 20))
        bbsn +=1
    for i in satlines:
        screen.draw.line(i[0], i[1], "white")

def update():
    pass

satlines = []
def on_mouse_down(pos):
    global next_sat, satlines
    if next_sat < total_sat:
        if satellite[next_sat].collidepoint(pos):
            if next_sat:
                satlines.append((satellite[next_sat-1].pos, satellite[next_sat].pos))
            next_sat += 1
        else:
            satlines = []
            next_sat = 0

pgzrun.go()