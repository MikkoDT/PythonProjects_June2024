def decorator(func):
    def wrapper(*args,**kwargs):
        print("Wrapper up side")
        func(*args,**kwargs)
        print("Wrapper down side")
    return wrapper

@decorator
def chocolate():
    print("Chocolate")

@decorator
def cake(name):
    print("Cake " +name)

#chocolate()
cake("apple")