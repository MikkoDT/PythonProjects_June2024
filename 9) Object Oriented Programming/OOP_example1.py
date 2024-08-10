#Creating a Class
class Vehicle:
    #Creating a constructor
    def __init__(self,name,color):
        #Instance Variables
        self.name=name
        self.color=color

    #Instance method
    def display_info(self):
        print(f"Name: {self.name}, Color: {self.color}")

class Car(Vehicle):
    pass

#Create an object
vehicle = Vehicle("Cool Car","Red")
#print(f"{vehicle.color} {vehicle.name}")
vehicle.display_info()

car = Car("Luxury Car", "Black")
car.display_info()