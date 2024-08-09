class Product:
    quantity = 200

    def __init__(self,name,price):
        self.name = name
        self.price = price

    #def summer_discount(self):
        #self.price = self.price - self.price * 5/100

    def summer_discount(self,discount_percent):
        self.price = self.price - self.price * discount_percent/100

p1 = Product("Tshirt",10)
print(p1.name)
print(p1.price)
p1.summer_discount(10)
print(p1.name)
print(p1.price)

p2 = Product("Phone",400)
p2.summer_discount(20)
print(p2.name)
print(p2.price)