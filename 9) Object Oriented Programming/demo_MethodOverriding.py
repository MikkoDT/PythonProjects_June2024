class Food:
    def type(self):
        print('Food')

class Fruit(Food):
    #def type(self):
        #print('Fruit')
    def welcome(self):
        print('Fruit')

apple = Fruit()
print(apple.type())