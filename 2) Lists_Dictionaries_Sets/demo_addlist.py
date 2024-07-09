products = ['phone','tablet','laptop','journal']

# displaying products
print(f"Current list of items :{products}")

#
add_item = input("Enter product to add: ")

add_after = input(f"After which product do you want to place {add_item} ")

index = products.index(add_after)
products.insert(index+1,add_item)

print(f"Current list of items :{products}")