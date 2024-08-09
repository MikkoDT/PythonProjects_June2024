class Student:
    #class variable
    category = "student"

    def __init__(self, name):
        # instance variable
        self.name = name

    # instance method
        print(f"Hello my name is {self.name}.")

    # instance method
    def name_length(self):
        return len(self.name)

    @classmethod
    def info(cls):
        print(f"This is a method of the class {cls.category}.")

student1 = Student("John")
#student1.hello()
#length = student1.name_length()
#print(length)
Student.info()