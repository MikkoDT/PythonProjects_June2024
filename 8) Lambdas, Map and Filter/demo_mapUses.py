numbers = ["1","2","3","4","5"]
print(numbers)

new_list = list(map(int,numbers))
print(new_list)

prices = [100,200,300,400,500]

new_prices = list(map(lambda x: x - x*5/100,prices))
print(new_prices)

names = ['john','rob','mike']

cap_names = list(map(str.capitalize,names))
print(cap_names)

cap_names = list(map(str.upper,names))
print(cap_names)