from copy import deepcopy


class BasicClass(object):
    def __init__(self):
        self.a = 1488

    def get_a(self):
        return self.a


class Prototype:
    def __init__(self):
        self._objs = {}

    def registerObject(self, name, obj):
        self._objs[name] = obj

    def unregisterObject(self, name):
        del self._objs[name]

    def clone(self, name, **attr):
        obj = deepcopy(self._objs[name])
        obj.__dict__.update(attr)
        return obj


p = Prototype()
basic_instance = BasicClass()
print(p.registerObject('basic_instance', basic_instance))
obj = p.clone('basic_instance', new_attr=42)
print(dir(obj))
