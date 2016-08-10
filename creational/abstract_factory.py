class Product(object):
    def __init__(self, name='iPhone', price=0.0, expiration_date=None, out_of_stock=False):
        self.name = name
        self.price = price
        self.expiration_date = expiration_date
        self.out_of_stock = out_of_stock

    def is_product_availiable(self):
        pass


class Shop(object):
    def get_availiable_product(self, name):
        pass


class Order(object):
    def __init__(self, ProductClass, ShopClass):
        self.product = ProductClass()
        self.shop = ShopClass()

    def get_order(self):
        return self.shop.get_availiable_product(self.product)


class Phone(Product):
    def is_product_availiable(self):
        if not self.out_of_stock:
            return True
        return False


class InternetShop(Shop):
    def __init__(self, *args, **kwargs):
        self.availiable_product = []
        iphone = Product('iPhone', '620')
        self.availiable_product.append(iphone.name)

    def get_availiable_product(self, product):
        if product.name in self.availiable_product and product.is_product_availiable():
            return product
        raise Exception('Product doesn`t availiable ')


order = Order(Phone, InternetShop)
print(order.get_order())
