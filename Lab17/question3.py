""""Write a script to check if a given number, N, is prime or not"""
#input number from user
n=int(input("Enter a number: "))

for i in range(2,n):
    if n % i==0:
        print("Not Prime")
        break
else:
    print("Prime")




