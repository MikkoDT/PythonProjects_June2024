products = [{"name":"Smartphone","price":500,"description":"A handheld device"},
            {"name":"Laptop","price":1000,"description":"A portable computer"},
            {"name":"Headphones","price":50,"description":"A pair of earphones"},
            {"name":"Smartwatch","price":300,"description":"A wearable device"},
            {"name":"Bluetooth speaker","price":100,"description":"A portable speaker"}
            ]

cart = []

while True:
    choice = input("Do you want to continue shopping? ")

    if choice == "yes":
        print('Here is a list of products and their prices')
        for index,product in enumerate(products):
            print(f"{product['name']} : {product['description']} : {product['price']}")
        product_id = int(input("Enter the ID of the product you want to add to the cart."))
        cart.append()
