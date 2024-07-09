def remove_duplicates(numbers):
    return list(set(numbers))


ids = [1,2,3,4,5,2,1,7,8,9]
result = remove_duplicates(ids)
print(result)