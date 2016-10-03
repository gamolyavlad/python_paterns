from copy import deepcopy


class Product(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Shop(object):
    """Prototype class."""
    def __init__(self):
        self._product = {}

    def register_product(self, product_name, product_obj):
        self._product[product_name] = product_obj

    def unregister_product(self, name):
        del self._product[name]

    def clone(self, name, **attr):
        obj = deepcopy(self._product[name])
        obj.__dict__.update(attr)
        return obj

if __name__ == "__main__":
    BestBye = Shop()
    phone = Product('phone')
    BestBye.register_object('phone', phone)
    print(BestBye._product)
    TV = BestBye.clone('LG', name='TV')
    print(TV)
