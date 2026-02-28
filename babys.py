import pgzrun
import random
from time import time

WIDTH = 1000
HEIGHT = 700

satellite = []
for i in range(12):
    bbs = Actor("babysatellite")
    bbs.pos = random.randint(171, 969), random.randint(252, 696)
    satellite.append(bbs)

starttime = 0
totaltime = 0

print(time())