class Product:
    def __init__(self, **kwargs):
        self.name = kwargs.setdefault('name', None)
        self.stock = kwargs.setdefault('stock', 0)
        self.price = kwargs.setdefault('price', 0)

    def __repr__(self):
        return f'{self.name}'

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.setdefault('name', None)
        self.gender = kwargs.setdefault('gender', None)
        self.money = kwargs.setdefault('money', 0)
        self.cart = []

    def buy(self, *product_list):
        self.cart.extend(product_list)
    
    def log(self):
        print(f'{self.name} buys {self.cart}.')

#####################

# Products
tolak_angin = Product(name='Tolak Angin', stock='10', price=2500)
fanta = Product(name='Fanta', stock='10', price=5000)
better = Product(name='Better', stock='10', price=2000)

# People
olive = Person(name='Olivia', gender='woman', money=10000)

olive.buy(tolak_angin, fanta)
olive.buy(better)
olive.log()
