import numpy as np
import os
import cairo
from shapes import Straight_Line
from utils import white_background, write_png

FILENAME = os.path.basename(__file__).strip(".py")
EXT = "png"
WIDTH, HEIGHT = 1000, 1000
LINE_WIDTH = 0.1

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)


def main():
    white_background(ctx)
    for n in range(30000):
        x = np.random.random(2) * WIDTH
        y = (np.random.random(2) ** 0.25) * WIDTH
        p0 = [x[0], y[0]]
        p1 = [x[1], y[1]]
        Straight_Line(p0, p1, LINE_WIDTH).draw(ctx)

    write_png(surface, FILENAME, EXT)


if __name__ == "__main__":
    main()
