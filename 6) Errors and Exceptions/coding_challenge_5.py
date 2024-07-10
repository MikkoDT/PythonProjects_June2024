def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Cannot divide a number by zero.')
    finally:
        print('This code will be executed no matter what.')

    #return print('Cannot divide a number by zero.')

print("result = ",divide(0,0))



