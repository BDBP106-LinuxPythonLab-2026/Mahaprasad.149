""""Write a script to convert the binary number B into decimal."""""
b=int(input("Enter a binary number: "))

decimal=0
power=0

while b>0:
    digit=b%10
    decimal=decimal+digit*(2**power)
    b=b//10
    power=power+1
print(decimal)
