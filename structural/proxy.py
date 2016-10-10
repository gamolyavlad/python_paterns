"""
A proxy is a wrapper or agent object that is being called by the client to access
the real serving object behind the scenes.
For the client, usage of a proxy object is similar to using the real object, because both implement the same interface.
"""


class Image(object):
    def __init__(self, filename):
        self._filename = filename
        self._loaded = False

    def load(self):
        print("loading {}".format(self._filename))
        self._loaded = True

    def display(self):
        if not self._loaded:
            self.load()
        print("displaying {}".format(self._filename))


class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxystate = None


class ProxyImage(Proxy):
    def display_image(self):
        if self._proxystate == None:
            self._subject.load()
            self._proxystate = 1
        print("display " + self._subject._filename)


proxy_image1 = ProxyImage(Image("HiRes_10Mb_Photo1"))
proxy_image2 = ProxyImage(Image("HiRes_10Mb_Photo2"))

proxy_image1.display_image()  # loading necessary
proxy_image1.display_image()  # loading unnecessary
proxy_image2.display_image()  # loading necessary
proxy_image2.display_image()  # loading unnecessary
proxy_image1.display_image()  # loading unnecessary
