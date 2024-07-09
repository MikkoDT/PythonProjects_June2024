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
"""F String"""
print("Simple interest on the principal amount $"+str(principal)+". For a period of "+str(years)+" years at the rate of "+str(rate)+"% is $ "+str(interest)+".")
print(f"Simple interest on the principal amount ${principal}. For a period of {years} years at the rate of {rate}% is ${interest}.")