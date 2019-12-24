import os
import random
import cairo
from shapes import Straight_Line
from utils import white_background, write_png

FILENAME = os.path.basename(__file__).strip(".py")
EXT = "png"
WIDTH, HEIGHT = 1000, 1000
LINE_WIDTH = 1
SPACING = 10

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)


def make_row(y0):
    if y0 / SPACING % 2 == 0:
        n = 0
        bottom_y = y0 + SPACING
    else:
        n = 1
        y0 += SPACING
        bottom_y = y0

    x0 = 0
    ctx.move_to(x0, y0)

    while x0 < WIDTH:
        if n % 2 == 0:
            x1 = x0 + SPACING / 2
            y1 = y0 + SPACING
        else:
            x1 = x0 + SPACING / 2
            y1 = y0 - SPACING

        a = (x0 + x1) / 2 + random.randrange(-10, 10)
        b = (y0 + y1) / 2 + random.randrange(-10, 10)
        ctx.set_line_width(1)
        ctx.curve_to(x0, y0, a, b, x1, y1)
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.stroke()

        #  Straight_Line([x0, y0], [x1, y1], 1).draw(ctx)
        x0, y0 = x1, y1
        n += 1

    Straight_Line([0, bottom_y], [WIDTH, bottom_y], 1).draw(ctx)


def make_grid():
    for i in range(0, HEIGHT, SPACING):
        make_row(i)


def main():
    white_background(ctx)
    make_grid()
    write_png(surface, FILENAME, EXT)


if __name__ == "__main__":
    main()
