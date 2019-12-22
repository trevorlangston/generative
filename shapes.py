import math


class Straight_Line:
    def __init__(self, p0, p1, width):
        self.p0 = p0
        self.p1 = p1
        self.width = width

    def draw(self, ctx):
        ctx.set_line_width(self.width)
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.move_to(self.p0[0], self.p0[1])
        ctx.line_to(self.p1[0], self.p1[1])
        ctx.stroke()


class Point:
    def __init__(self, p0, width):
        self.p0 = p0
        self.width = width

    def draw(self, ctx):
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.arc(self.p0[0], self.p0[1], self.width, 0, 2*math.pi)
        ctx.stroke()
