#Fahrenheit (F) = (Temperature in degrees Celsius (C) * 9/5) + 32
celsius_temp = [25, 30, 15, 10, 35]
fahrenheit_temp =list(map(lambda c: (c * 9/5)+32,celsius_temp))
print(fahrenheit_temp)