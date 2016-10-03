""" Python supports named parameters, so builder doesn`t make any sence . """

from collections import namedtuple

IMMUTABLE_OBJECT_FIELDS = ['required_function_result', 'required_parameter', 'default_parameter']


class ImmutableObjectBuilder(object):
    def __init__(self, required_function, required_parameter, default_parameter="foo"):
        self.required_function = required_function
        self.required_parameter = required_parameter
        self.default_parameter = default_parameter

    def build(self):
        return ImmutableObject(self.required_function(self.required_parameter),
                               self.required_parameter,
                               self.default_parameter)


class ImmutableObject(namedtuple('ImmutableObject', IMMUTABLE_OBJECT_FIELDS)):
    __slots__ = ()

    @property
    def foo_property(self):
        return self.required_function_result + self.required_parameter

    def foo_function(self):
        return self.required_function_result - self.required_parameter

    def __str__(self):
        return str(self.__dict__)


my_builder = ImmutableObjectBuilder(lambda x: x + 1, 2)
obj1 = my_builder.build()
my_builder.default_parameter = "bar"
my_builder.required_parameter = 1
obj2 = my_builder.build()
my_builder.required_function = lambda x: x - 1
obj3 = my_builder.build()

print(obj1)
print(obj1.required_function_result)
print(obj1.foo_property)
print(obj1.foo_function())
print(obj2)
print(obj3)
