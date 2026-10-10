""""Write a program to print sum of digits in a number"""
n=int(input("Enter a number: "))

sum=0
while n!=0:
    sum=sum+(n%10)
    n=n//10

print(f'sum of digits is  {sum}')


