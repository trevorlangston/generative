def white_background(ctx):
    ctx.set_source_rgba(1.0, 1.0, 1.0, 1.0)
    ctx.paint()


def write_png(surface, filename, ext):
    surface.write_to_png("images/{}.{}".format(filename, ext))
