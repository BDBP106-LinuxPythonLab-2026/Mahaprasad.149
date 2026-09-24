"""""Write a script that computes power - raise base to the n-th power. Eg. power(2, 5).Here base is 2 and n-th power is 5."""""

a=int(input("Enter a number: "))
b=int(input("Enter the power you want of the number: "))

result=1
for i in range(b):
    result= result * a
print(result)