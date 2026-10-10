#Write a program to filter out the odd elements of the Fibonacci series for the first n term
n=int(input("Enter a number of terms: "))
fib=[]
a, b = 0, 1

for i in range(n):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci series:", fib)
odd = list(filter(lambda x: x % 2 != 0, fib))
print("Odd elements:", odd)