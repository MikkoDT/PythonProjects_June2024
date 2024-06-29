"""Simple Interest Formula
SI = P * N * R / 100
P = principal
N = years
R = rate

"""

principal = int(input("Enter the amount borrowed: "))
years = int(input("Enter the period in years: "))
rate = int(input("Enter rate of interest: "))

interest = principal * years * rate / 100
print("interest = ", interest)