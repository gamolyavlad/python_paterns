#!/usr/bin/python
"""
Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual
objects and compositions of objects uniformly.
"""


class Component(object):
    def __init__(self, *args, **kw):
        pass

    def component_function(self):
        raise NotImplemented


class Leaf(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)

    def component_function(self):
        print("component_function {}".format(self))


class Composite(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        [x.component_function() for x in self.children]


if __name__ == "__main__":
    composite = Composite()
    l = Leaf()
    l_two = Leaf()
    l_three = Leaf()
    composite.append_child(l)
    print(composite.children)
    composite.append_child(l_two)
    composite.append_child(l_three)
    print(composite.children)
    composite.component_function()
