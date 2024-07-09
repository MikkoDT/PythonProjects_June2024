def decorator(func):
    def wrapper():
        print("Wrapper up side")
        func()
        print("Wrapper down side")
    return wrapper

@decorator
def chocolate():
    print("Chocolate")

@decorator
def cake():
    print("Cake")

chocolate()
cake()