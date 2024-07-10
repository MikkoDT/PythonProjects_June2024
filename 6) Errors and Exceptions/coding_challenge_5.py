def divide(x,y):
    result = x / y
    try:
        result = x / y
    except ZeroDivisionError:
        print('Cannot divide a number by zero.')
    finally:
        print('This code will be executed no matter what.')

    return result


print("result = ",divide(5,0))



