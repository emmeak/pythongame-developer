import pgzrun
import random

WIDTH = 567
HEIGHT = 543

lil_bb = Actor("littlebumblebee")
lil_bb.pos = (555,252)
sunflower = Actor("sunflower")
sunflower.pos = (543,345)

score = 0
game_over = False

def draw():
    screen.blit("bg",(0,0))
    lil_bb.draw()
    sunflower.draw()
    screen.draw.text("Score:" + str(score), center = (252,252), fontname = "forte.ttf", fontsize = 21)

def update():
    if keyboard.left:
        lil_bb.x -= 5
    if keyboard.right:
        lil_bb.x += 5
    if keyboard.down:
        lil_bb.y += 5
    if keyboard.up:
        lil_bb.y -= 5
        
    global score

    if lil_bb.colliderect(sunflower):
        sunflower.pos = random.randint(25,525), random.randint(52,525)
        score += 7

def timer():
    global game_over
    game_over = True

clock.schedule(timer, 21)

pgzrun.go()