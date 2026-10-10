# Write a program to convert temperature in Celsius to Fahrenheit using map function.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(celsius_to_fahrenheit, celsius))

print("Celsius temperatures:", celsius)
print("Fahrenheit temperatures:", fahrenheit)

print(list(map(lambda C: C*9/5+32, [25])))