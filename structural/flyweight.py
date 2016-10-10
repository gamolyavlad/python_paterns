"""
 A flyweight is an object that minimizes memory use by sharing as much data as possible with other similar objects;
 it is a way to use objects in large numbers when a simple repeated representation would use an unacceptable amount of
 memory. Often some parts of the object state can be shared, and it is common practice to hold them in external data
 structures and pass them to the flyweight objects temporarily when they are used.

 Python has weakref module to create weak references to objects.
"""


class Human(object):
    __slots__ = ['gender', 'age', 'first_name']

    def __init__(self, gender, age, first_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name

    def info(self, id):
        return self.gender, self.age, self.first_name, id


if __name__ == '__main__':
    assembly = [(1, Human('male', '12', 'John')),
                (2, Human('female', '32', 'Helen')),
                (3, Human('male', '43', 'Dave'))]
    print(assembly)
