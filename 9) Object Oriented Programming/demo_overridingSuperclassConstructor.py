class Parent:
    def __init__(self):
        self.balance = 50000

    def display_balance(self):
        print(f"Parent's balance is {self.balance}.")

class Child(Parent):
    def __init__(self):
        self.balance = 20000

    def display_balance(self):
        print(f"Child's balance is: {self.balance}.")

Mike = Child()
Mike.display_balance()