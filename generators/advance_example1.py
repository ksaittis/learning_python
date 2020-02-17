import random
import sys
import time

sys.path.insert(0, '..')
from generators.gameworld import Animal, draw_grid, move


def cats():
    cat = Animal(2, 2)
    while True:
        mouse = yield cat
        if mouse.row > cat.row:
            cat = move(cat, row=1)
        elif mouse.row < cat.row:
            cat = move(cat, row=-1)
        if mouse.col > cat.col:
            cat = move(cat, col=1)
        elif mouse.col < cat.col:
            cat = move(cat, col=-1)


def mice():
    mouse = Animal(7, 7)
    while True:
        cat = yield mouse
        if mouse.col == cat.col and mouse.row == cat.row:
            raise StopIteration('Mouse has been got by the cat')
        if mouse.row > cat.row:
            mouse = move(mouse, row=1)
        elif mouse.row < cat.row:
            mouse = move(mouse, row=-1)
        else:
            mouse = move(mouse, row=random.choice([-1, 1]))
        if mouse.col > cat.col:
            mouse = move(mouse, col=1)
        elif mouse.col < cat.col:
            mouse = move(mouse, col=-1)
        else:
            mouse = move(mouse, col=random.choice([-1, 1]))


icat = cats()
imouse = mice()
cat = icat.send(None)
mouse = imouse.send(None)
if __name__ == '__main__':
    while True:
        draw_grid(cat, mouse)
        time.sleep(.4)
        try:
            cat = icat.send(mouse)
            mouse = imouse.send(cat)
        except StopIteration:
            print('Completed')
            break
    draw_grid(cat, mouse)
