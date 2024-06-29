"""Simple Interest Formula
SI = P * N * R / 100
P = principal
N = years
R = rate

"""

principal = float(input("Enter the amount borrowed: "))
years = float(input("Enter the period in years: "))
rate = float(input("Enter rate of interest: "))

interest = principal * years * rate / 100
print("interest = "+ str(interest))