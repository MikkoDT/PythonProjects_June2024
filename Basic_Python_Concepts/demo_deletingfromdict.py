products = {'phone':100,'tablet':200,'laptop':400,'journal':40}

print(products)

deleted_products = input("Enter the name of product to be deleted: ")
del products[deleted_products]

print(f"Product deleted, here are updated products {products}.")
