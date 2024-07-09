def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

print(add(2,3,5,10,1,2,3,4,5))