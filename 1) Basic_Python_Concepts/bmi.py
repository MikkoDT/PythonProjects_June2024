"""BMI formula
BMI = weight in kg / (height in m)^2
"""

weight = float(input("Your weight in kg?: "))
height = float(input("Your height in m?: "))

BMI = weight / height**2

print(f"Your BMI is {BMI} kg/m^2")