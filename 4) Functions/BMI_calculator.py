def BMI(w,h):
    result = w / (h * h)
    return result

w = float(input('Enter weight in Kgs: '))
h = float(input('Enter in height in meters: '))
x = BMI(w,h)
print(x)
