import numpy as np
import os
import cairo
from shapes import Straight_Line

FILENAME = os.path.basename(__file__).strip(".py")
EXT = "png"
WIDTH, HEIGHT = 1000, 1000
LINE_WIDTH = 0.1

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)


def white_background():
    ctx.set_source_rgba(1.0, 1.0, 1.0, 1.0)
    ctx.paint()


def write(filename, ext):
    surface.write_to_png("images/{}.{}".format(filename, ext))


def main():
    white_background()
    for n in range(30000):
        x = np.random.random(2) * WIDTH
        y = (np.random.random(2) ** 0.25) * WIDTH
        p0 = [x[0], y[0]]
        p1 = [x[1], y[1]]
        Straight_Line(p0, p1, LINE_WIDTH).draw(ctx)

    write(FILENAME, EXT)


if __name__ == "__main__":
    main()
