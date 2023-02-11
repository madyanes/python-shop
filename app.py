import pdb

class Product:
    def __init__(self, **kwargs):
        self.name = kwargs.setdefault('name', None)
        self.stock = kwargs.setdefault('stock', 0)
        self.price = kwargs.setdefault('price', 0)

    def __repr__(self):
        return f'{self.name}'

class Person:
    cart = []
    purchase_history = []
    
    def __init__(self, **kwargs):
        self.name = kwargs.setdefault('name', None)
        self.money = kwargs.setdefault('money', 0)

    def buy(self, *product_list):
        '''Purchasing process.'''
        print(f'{self.name} wants to buy {product_list}.')
        self.cart.extend(product_list)
        products = self.cart.copy()  # shallow copy
        for product in products:
            if product.stock <= 0:
                # product with 0 stock is removed from the cart
                print(f'{product} is currently unavailable. Removed from the cart.')
                self.cart.remove(product)
                continue
            # calculate available products only
            product.stock = product.stock - 1
            if not self.charge(product): continue
        self.log()
    
    def charge(self, product):
        '''Is the money enough to buy?'''
        if self.money <= 0 or (self.money - product.price) < 0:
            self.cart.remove(product)
            print(f'{self.name} does not have enough money to buy {product}. ==> (money = {self.money}, required = {[product.price]})')
            return False
        print(f'{self.name} purchased {product} successfully.')
        self.money = self.money - product.price
        self.purchase_history.append(product)
        self.cart.remove(product)
    
    def log(self):
        print(f'{self.name} buys {self.purchase_history}')

#####################

# Products
tolak_angin = Product(name='Tolak Angin', stock=0, price=2500)
fanta = Product(name='Fanta', stock=10, price=5000)
better = Product(name='Better', stock=10, price=2000)

# People
olive = Person(name='Olivia', money=5000)

olive.buy(tolak_angin, fanta, better)
# Olivia wants to buy (Tolak Angin, Fanta, Better).
# Tolak Angin is currently unavailable. Removed from the cart.
# Olivia purchased Fanta successfully.
# Olivia does not have enough money to buy Better. ==> (money = 0, required = [2000])
# Olivia buys [Fanta]

print(vars(olive))  # {'name': 'Olivia', 'money': 0}
