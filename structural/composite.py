"""
Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual
objects and compositions of objects uniformly.
"""
#  Created using diagramm

class Component(object):
    def __init__(self, *args, **kw):
        pass

    def component_function(self):
        pass


class Leaf(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)

    def component_function(self):
        print("some function")


class Composite(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        map(lambda x: x.component_function(), self.children)


c = Composite()
l = Leaf()
l_two = Leaf()
l_three = Leaf()
c.append_child(l)
c.append_child(l_two)
c.append_child(l_three)
print(c.children)
