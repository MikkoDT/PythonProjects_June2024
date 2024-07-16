numbers = [1,2,3,4,5]
"""
def square(x):
    return x*x

for number in numbers:
    print(square(number))
"""

def square(x):
    return x*x

new_list = list(map(square,numbers))
print(new_list)