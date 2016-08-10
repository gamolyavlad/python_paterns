"""
Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't
otherwise because of incompatible interfaces.
"""


class Png(object):
    def draw_png_image(self):
        return "Draw png image"


class Jpg(object):
    def draw_jpg_image(self):
        return "Draw jpg image"


class Photo(Png):
    def draw_image(self):
        return self.draw_png_image()


class Gradient(Jpg):
    def draw_image(self):
        return self.draw_jpg_image()


class Gallery:
    def __init__(self, source):
        self.source = source

    def show_picture(self):
        return self.source.draw_image()


p = Photo()
g = Gradient()
photo_images = Gallery(p)
gradient_background = Gallery(g)
print(photo_images.show_picture())
print(gradient_background.show_picture())


# class Target:
#     @staticmethod
#     def meth1(p1, p2):
#
#         print(p1 + ", " + p2)
#
#
# class Adapter:
#     @staticmethod
#     def meth2(p1, p2, p3):
#
#         Target.meth1(p1, p2 + " and " + p3)
#
#
# Adapter.meth2('here', 'there', 'everywhere')
