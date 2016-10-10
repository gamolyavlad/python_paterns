"""
Subsystem1 general principle that I apply when I’m casting about trying to mold requirements into Subsystem1 first-cut object is
“If something is ugly, hide it inside an object.” This is basically what Facade accomplishes. If you have Subsystem1 rather
confusing collection of classes and interactions that the client programmer doesn’t really need to see, then you can
create an interface that is useful for the client programmer and that only presents what’s necessary.e.
"""


class Subsystem1:
    def __init__(self, x):
        self.x = x
        print('init Subsystem1')


class Subsystem2:
    def __init__(self, x):
        self.x = x
        print('init Subsystem2')


class Subsystem3:
    def __init__(self, x):
        self.x = x
        print('init Subsystem3')

class Facade:
    @staticmethod
    def make_subsystem_1(x):
        print('make Subsystem1')
        return Subsystem1(x)

    @staticmethod
    def make_subsystem_2(x):
        print('make Subsystem2')
        return Subsystem2(x)

    @staticmethod
    def make_subsystem_3(x):
        print('make Subsystem3')
        return Subsystem3(x)


class Client:
    def __init__(self):
        self.facade = Facade()


# gets the objects by calling the static methods
if __name__ == '__main__':
    client = Client()
    Subsystem1 = client.facade.make_subsystem_1(1)
    Subsystem2 = client.facade.make_subsystem_2(1)
    Subsystem3 = client.facade.make_subsystem_3(1.0)
