def chocolate():
    print("Chocolate")

def decorator(func):
    def wrapper():
        print("Wrapper up side")
        func()
        print("Wrapper down side")
    return wrapper

chocolate = decorator(chocolate)
chocolate()