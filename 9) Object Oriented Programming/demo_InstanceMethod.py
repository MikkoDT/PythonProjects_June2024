class Student:
    def __init__(self,name):
        #instance variable
        self.name = name
        
    # instance method
    def hello(self):
        print(f"Hello my name is {self.name}.")

    #instance method
    def name_length(self):
        return len(self.name)

student1 = Student("John")
student1.hello()
length = student1.name_length()
print(length)