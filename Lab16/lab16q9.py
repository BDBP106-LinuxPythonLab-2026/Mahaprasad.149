""""Write a program to reverse a number and print the reversed number"""

# take input of a number from user

n=int(input("Enter a number: "))

original= n
rev=0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)