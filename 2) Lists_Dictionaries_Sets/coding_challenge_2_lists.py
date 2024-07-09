food = ['spaghetti','ramen','lomi','caldereta','banana']
print(food)

print(f"3rd element in the list: {food[2]}")

added_food = input(f"add new food: ")
add_after = input(f"After which product do you want to place {added_food}? ")


index = food.index(add_after)
food.insert(index+1,added_food)

print(f"Current list of items :{food}")

add_taco = 'tacos'
add_after = input(f"After which product do you want to place {add_taco}? ")

index = food.index(add_after)
food.insert(index+1,add_taco)

print(f"Current list of items :{food}")

"""
food = ['spaghetti','ramen','lomi','caldereta','banana']
 
print(food[2])
 
food.append('fries')
 
print(food)
 
food.insert(3, 'tacos')
 
print(food)
"""

