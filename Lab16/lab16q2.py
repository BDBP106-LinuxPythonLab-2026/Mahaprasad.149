""" Find simple interest and amount with simple interest included."""
import math


amount=int(input("Enter a amount: "))
interest=float(input("Enter rate of interest: "))
time=float(input("Enter time in years: "))

simple_interest= ((amount*time*interest)/100)
print(simple_interest)