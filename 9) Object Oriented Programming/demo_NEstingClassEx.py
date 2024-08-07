class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self,name,species):
        animal = self.Animal(name,species)
        self.animals.append(animal)

    class Animal:
        def __init__(self,name,species):
            self.name = name
            self.species = species

        def display_info(self):
            print(f"Name:{self.name}, Species:{self.species}")

#creating a zoo
my_Zoo = Zoo()

#add animals to the zoo
my_Zoo.add_animal("Lion","Mammal")
my_Zoo.add_animal("Eagle","Bird")
my_Zoo.add_animal("Crocodile","Reptile")

for animal in my_Zoo.animals:
    animal.display_info()