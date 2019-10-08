#1task
class Mathematician:

    def square_nums(self, sqnums):
        return [n**2 for n in sqnums]

    def remove_positives(self, nopositive):
        return [n for n in nopositive if n < 0]

    def filter_leaps(self, leaps):
        return [n for n in leaps if n%2 == 0]

m = Mathematician()

#2task
class Product:
    def __init__(self, type1, name, price, quantity):
        self.type = type1
        self.name = name
        self.price = price
        self.quantity = quantity

    def add(self, quantity):
        self.quantity += quantity
        return self.quantity

    def set_disqount(self, price):
        self.price -= price * self.price / 100
        return self.price

p = Product('Sport', 'Football T-Shirt', 100, 30)




