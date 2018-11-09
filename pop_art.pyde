from random import randint

def setup():
    size(800, 800)
    frameRate(2)

def draw():
    for x in range(10):
        for y in range(10):
            fill(color(randint(0,255),randint(0,255),randint(0,255)))
            rect(x * 80, y * 80,80,80)
