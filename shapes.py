import math


class Straight_Line:
    def __init__(self, p0, p1, line_width):
        self.p0 = p0
        self.p1 = p1
        self.line_width = line_width

    def draw(self, ctx):
        ctx.set_line_width(self.line_width)
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.move_to(self.p0[0], self.p0[1])
        ctx.line_to(self.p1[0], self.p1[1])
        ctx.stroke()


class Rectangle:
    def __init__(self, p0, width, height, line_width):
        self.width = width
        self.height = height
        self.p0 = p0
        self.p1 = [self.p0[0] + self.width, self.p0[1]]
        self.p2 = [self.p0[0] + self.width, self.p0[1] + self.height]
        self.p3 = [self.p0[0], self.p0[1] + self.height]
        self.line_width = line_width

    def draw(self, ctx):
        Straight_Line(self.p0, self.p1, self.line_width).draw(ctx)
        Straight_Line(self.p1, self.p2, self.line_width).draw(ctx)
        Straight_Line(self.p2, self.p3, self.line_width).draw(ctx)
        Straight_Line(self.p3, self.p0, self.line_width).draw(ctx)


class Point:
    def __init__(self, p0, size):
        self.p0 = p0
        self.size = size

    def draw(self, ctx):
        ctx.set_source_rgba(0, 0, 0, 1)
        ctx.arc(self.p0[0], self.p0[1], self.size, 0, 2*math.pi)
        ctx.stroke()
