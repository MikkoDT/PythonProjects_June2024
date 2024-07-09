def remove_duplicates(numbers):
    new_list=[]
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list


ids = [1,2,3,4,5,2,1,7,8,9]
result = remove_duplicates(ids)
print(result)