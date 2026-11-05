import re

pattern = r'^(00[0-9]|0[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

number = input("Enter a 3-digit integer between 000 and 255: ")

if re.fullmatch(pattern, number):
    print("Valid input")
else:
    print("Invalid input")
