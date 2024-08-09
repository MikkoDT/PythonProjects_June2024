class Parent:
    def __init__(self):
        self.balance=50000

    def display_balance(self):
        print(f"Parent's balance is {self.balance}.")

class Child(Parent):
    pass

Mike = Child()
Mike.display_balance()