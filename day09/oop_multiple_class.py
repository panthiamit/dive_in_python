class Phone():
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('buying a phone')

    def return_phone(self):
        print('returning a phone')


class Product():

    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def review(self):
        print('customer review')

class Smartphone(Product,Phone):
    pass


s = Smartphone(20000,'apple',12)

s.buy()
s.review()
price = s.price
print(price)