"""
def square(x):
    return x**2

print(square(9))
"""

result1 = (lambda x: x**2)(7)
print("result1 = ",result1)

result2 = (lambda x,y: x+y)(2,3)
print("result2 = ",result2)