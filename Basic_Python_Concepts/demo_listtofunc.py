scores = [1,2,3,4,5]

def add(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

result = add(scores)
print(result)
