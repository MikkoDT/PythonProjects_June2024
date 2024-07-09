cart = []

while True:
    choice = input("Do you want to add item to the cart? ")
    if choice == "yes":
        item = input("Enter the item you want to add: ")
        cart.append(item)
        print(f"Current cart contents are {cart}")
    else:
        break