import random
import os
import cairo
from shapes import Rectangle
from utils import white_background, write_png

FILENAME = os.path.basename(__file__).strip(".py")
EXT = "png"
WIDTH, HEIGHT = 1000, 1000
LINE_WIDTH = 1

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)


def main():
    white_background(ctx)
    recurse(Rectangle([100, 100], 350, 400, LINE_WIDTH), 40)
    recurse(Rectangle([100, 550], 400, 350, LINE_WIDTH), 30)
    recurse(Rectangle([550, 500], 350, 400, LINE_WIDTH), 20)
    recurse(Rectangle([500, 100], 400, 350, LINE_WIDTH), 10)
    write_png(surface, FILENAME, EXT)


def recurse(rect, stop):
    rect.draw(ctx)
    if rect.width < stop or rect.height < stop:
        return

    flip = random.randint(0, 1)
    offset = random.randrange(stop / -2.0, stop / 2.0)
    if flip == 0:
        p0_height = rect.height
        p1_height = rect.height
        p0_width = rect.width / 2.0 + offset
        p1_width = rect.width - p0_width
        p1 = [rect.p0[0] + p0_width, rect.p0[1]]
    else:
        p0_height = rect.height / 2.0 + offset
        p1_height = rect.height - p0_height
        p0_width = rect.width
        p1_width = rect.width
        p1 = [rect.p0[0], rect.p0[1] + p0_height]

    recurse(Rectangle(rect.p0, p0_width, p0_height, LINE_WIDTH), stop)
    recurse(Rectangle(p1, p1_width, p1_height, LINE_WIDTH), stop)


if __name__ == "__main__":
    main()
