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
        products_obj = [product['product'] for product in product_list]  # get `product` only from a tuple of dictionary
        print(f'{self.name} wants to buy {products_obj}.')
        self.cart.extend(products_obj)
        products = self.cart.copy()  # shallow copy
        for product in products:
            qty = product_list[products.index(product)]['qty']
            if not self.calc_product(product, qty): continue
            self.charge(product, qty)
        self.log()
    
    def calc_product(self, product, qty):
        '''Calculate the product'''
        if product.stock <= 0:  # calculate available products only
            # product with 0 stock is removed from the cart
            print(f'{product} is currently unavailable. Removed from the cart.')
            self.cart.remove(product)
            return False
        product.stock = product.stock - qty
        return product
    
    def charge(self, product, qty):
        '''Is the money enough to buy?'''
        if self.money <= 0 or (self.money - (product.price * qty)) < 0:
            self.cart.remove(product)
            print(f'{self.name} does not have enough money to buy {qty} {product}. ==> (money = {self.money}, qty = {qty}, required = {[product.price * qty]})')
            return False
        print(f'{self.name} purchased {qty} {product} successfully.')
        self.money = self.money - (product.price * qty)
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
olive = Person(name='Olivia', money=11000)

olive.buy({'product': tolak_angin, 'qty': 1}, {'product': fanta, 'qty': 2}, {'product': better, 'qty': 1})
# Olivia wants to buy [Tolak Angin, Fanta, Better].
# Tolak Angin is currently unavailable. Removed from the cart.
# Olivia purchased 2 Fanta successfully.
# Olivia does not have enough money to buy 1 Better. ==> (money = 1000, qty = 1, required = [2000])
# Olivia buys [Fanta]

print(vars(olive))  # {'name': 'Olivia', 'money': 1000}
