"""
Define an interface for creating an object , but let subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses
"""


class Genre(object):
    @staticmethod
    def factory(type):
        if type == "Adventure":
            return Adventure()
        elif type == "Drama":
            return Drama()
        raise Exception('invalid type {}'.format(type))


class Adventure(Genre):
    def drive(self):
        print("Adventure class")


class Drama(Genre):
    def drive(self):
        print("Drana class.")

"""Example from book"""


class Culture:
    def __repr__(self):
        return self.__str__()


class Democracy(Culture):
    def __str__(self):
        return 'Democracy'


class Dictatorship(Culture):
    def __str__(self):
        return 'Dictatorship'


class Government:
    culture = ''

    def __str__(self):
        return self.culture.__str__()

    def __repr__(self):
        return self.culture.__repr__()

    def set_culture(self):
        raise AttributeError('Not Implemented Culture')


class GovernmentA(Government):
    def set_culture(self):
        self.culture = Democracy()


class GovernmentB(Government):
    def set_culture(self):
        self.culture = Dictatorship()


if __name__ == "__main__":
    obj = Genre.factory("Adventure")
    obj.drive()

    g1 = GovernmentA()
    g1.set_culture()
    print(str(g1))

    g2 = GovernmentB()
    g2.set_culture()
    print(str(g2))
